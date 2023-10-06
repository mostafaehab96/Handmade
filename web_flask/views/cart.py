from web_flask.views import app_views
from flask import render_template, jsonify, make_response
from flask_login import login_required, current_user
from models import storage


@app_views.route('/add_cart/<product_id>')
def add_cart(product_id):
    if current_user.is_active:
        product = storage.get("Product", product_id)
        user = storage.get("User", current_user.get_id())
        if product not in user.cart.products:
            user.cart.products.append(product)
            storage.save()
        return jsonify({"status": "OK"}), 200
    else:
        return jsonify({"status": "Login"})


@app_views.route("/cart/count")
def cart_count():
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        product_ids = [product.id for product in user.cart.products]
        count = len(product_ids)
        return jsonify({"count": f"{count}", "product_ids": product_ids}), 200
    return jsonify({"count": 0})


@app_views.route('/cart', methods=["GET", "POST"])
def cart():
    selected_products = []
    total_price = 0
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        selected_products = user.cart.products
        total_price = sum([product.price for product in selected_products])

    response = make_response(render_template("cart-details.html",
                                             products=selected_products,
                                             price=total_price,
                                             logged_in=current_user.is_active))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app_views.route('/cart/remove/<product_id>')
@login_required
def cart_remove(product_id):
    user = storage.get("User", current_user.get_id())
    product = storage.get("Product", product_id)
    user.cart.products.remove(product)
    storage.save()

    return jsonify({"status": "ok"}), 200
