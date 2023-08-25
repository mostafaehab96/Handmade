"""Handles users RESTFUL API"""
from api.views import app_views
from models.user import User
from models.product import Product
from models.review import Review
from models.order import Order
from flask import make_response, jsonify

@app_views.route('/users', strict_slashes=False)
def get_users():
    """Returns all users"""
    users = User.query.all()
    users = [user.to_dict() for user in users]
    return jsonify(users)
