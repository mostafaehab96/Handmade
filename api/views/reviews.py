from api.views import app_views
from models.review import Review
from flask import jsonify, make_response


@app_views.route("/reviews", strict_slashes=False)
def get_reviews():
    return jsonify(Review.all_records())


@app_views.route("/review/<id>", strict_slashes=False)
def get_review(id):
    review = Review.query.filter_by(id=id).first()
    if review:
        return jsonify(review.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)
