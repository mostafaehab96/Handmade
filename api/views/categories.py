from api.views import app_views
from flask import make_response, jsonify
from models.category import Category


@app_views.route('/categories', strict_slashes=False)
def get_categories():
    return jsonify(Category.all_records())


@app_views.route('/category/<id>', strict_slashes=False)
def get_category(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        return jsonify(category.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/category/<id>/products', strict_slashes=False)
def get_products_category(id):
    category = Category.query.filter_by(id=id).first()
    if category:
        products = category.products
        products = [product.to_dict() for product in products]
        return jsonify(products)
    else:
        return make_response({"Error": "Not Found"}, 404)
