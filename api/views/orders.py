from api.views import app_views
from models.user import User
from models.product import Product
from models.review import Review
from models.order import Order
from flask import make_response, jsonify, request


@app_views.route('/orders')
def get_orders():
    return jsonify(Order.all_records())


@app_views.route('/order/<id>', strict_slashes=False)
def get_order(id):
    order = Order.query.filter_by(id=id).first()
    if order:
        return jsonify(order.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)

@app_views.route('/order/<id>/products', strict_slashes=False)
def get_order_products(id):
    order = Order.query.filter_by(id=id).first()
    if order:
        products = order.products
        products = [product.to_dict() for product in products]
        return jsonify(products)
    else:
        return make_response({"Error": "Not Found"}, 404)
