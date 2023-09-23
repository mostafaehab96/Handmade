from web_flask.views import app_views
from flask import render_template, jsonify
from flask_login import login_required, current_user
from models import storage
from models.order import Order


@app_views.route("/checkout")
@login_required
def checkout():
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        products = user.cart.products
        total_price = sum([product.price for product in products])
        order = Order(address=user.address,
                      total_price=total_price,
                      user_id=user.id
                      )
        order.products = products
        order.save()
        user.cart.products = []
        storage.save()
        return jsonify({"status": "ok", "order_id": order.id})
    else:
        return jsonify({"status": 403}), 403


@app_views.route("/orders")
@login_required
def view_orders():
    user = storage.get("User", current_user.get_id())
    return render_template("orders.html", orders=user.orders, logged_in=current_user.is_active)
