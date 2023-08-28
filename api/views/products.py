from api.views import app_views
from models.user import User
from models.product import Product
from models.review import Review
from models.order import Order
from flask import make_response, jsonify, request


@app_views.route('/products', strict_slashes=False)
def get_products():
    return jsonify(Product.all_records())


@app_views.route('/product/<id>', strict_slashes=False)
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        return jsonify(product.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/product/<id>/categories', strict_slashes=False)
def get_product_categories(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        categories = product.categories
        categories = [category.to_dict() for category in categories]
        return jsonify(categories)
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/product/<id>/reviews', strict_slashes=False)
def get_product_reviews(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        reviews = product.reviews
        reviews = [review.to_dict() for review in reviews]
        return jsonify(reviews)
    else:
        return make_response({"Error": "Not Found"}, 404)
