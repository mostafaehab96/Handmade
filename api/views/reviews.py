from api.views import app_views
from flask import jsonify, make_response
from models import storage


@app_views.route("/reviews", strict_slashes=False)
def get_reviews():
    reviews = storage.all("Review")
    reviews = [review.to_dict() for review in reviews]
    return jsonify(reviews)


@app_views.route("/review/<id>", strict_slashes=False)
def get_review(id):
    review = storage.get("Review", id)
    if review:
        return jsonify(review.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)
