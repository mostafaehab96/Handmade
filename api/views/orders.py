from api.views import app_views
from flask import make_response, jsonify
from models import storage


@app_views.route('/orders')
def get_orders():
    orders = storage.all("Order")
    orders = [order.to_dict() for order in orders]
    return jsonify(orders)


@app_views.route('/order/<id>', strict_slashes=False)
def get_order(id):
    order = storage.get("Order", id)
    if order:
        return jsonify(order.to_dict())
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('/order/<id>/products', strict_slashes=False)
def get_order_products(id):
    order = storage.get("Order", id)
    if order:
        products = order.products
        products = [product.to_dict() for product in products]
        return jsonify(products)
    else:
        return make_response({"Error": "Not Found"}, 404)
