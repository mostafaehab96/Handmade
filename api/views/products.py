from api.views import app_views
from flask import make_response, jsonify
from models import storage


@app_views.route('/products', strict_slashes=False)
def get_products():
    products = storage.all("Product")
    products = [product.to_dict() for product in products]
    return jsonify(products)


@app_views.route('/product/<id>', strict_slashes=False)
def get_product(id):
    product = storage.get("Product", id)
    if product:
        return jsonify(product.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/product/<id>/categories', strict_slashes=False)
def get_product_categories(id):
    product = storage.get("Product", id)
    if product:
        categories = product.categories
        categories = [category.to_dict() for category in categories]
        return jsonify(categories)
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/product/<id>/reviews', strict_slashes=False)
def get_product_reviews(id):
    product = storage.get("Product", id)
    if product:
        reviews = product.reviews
        reviews = [review.to_dict() for review in reviews]
        return jsonify(reviews)
    else:
        return make_response({"Error": "Not Found"}, 404)
