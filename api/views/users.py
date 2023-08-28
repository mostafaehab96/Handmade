"""Handles users RESTFUL API"""
from api.views import app_views
from models.user import User
from flask import make_response, jsonify


@app_views.route('/users', strict_slashes=False)
def get_users():
    """Returns all users, or Add new user"""
    return jsonify(User.all_records())


@app_views.route('user/<id>', strict_slashes=False)
def get_user(id):
    """Return one user by id"""
    user = User.query.filter_by(id=id).first()
    if user:
        user = user.to_dict()
        return jsonify(user)
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('user/<id>/products', strict_slashes=False)
def get_user_products(id):
    """Retrieve all products for a user"""
    user = User.query.filter_by(id=id).first()
    if user:
        products = user.products
        products = [product.to_dict() for product in products]
        return jsonify(products)
    else:
        return make_response({"Error": "Not Found"}, 404)


@app_views.route('user/<id>/orders', strict_slashes=False)
def get_user_orders(id):
    """Retrieve all orders for a user"""
    user = User.query.filter_by(id=id).first()
    if user:
        orders = user.orders
        orders = [order.to_dict() for order in orders]
        return jsonify(orders)
    else:
        return make_response({"Error": "Not Found"}, 404)
