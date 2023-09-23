from web_flask.views import app_views
from flask import render_template, url_for, redirect, request, jsonify
from flask_login import current_user, login_required
from models import storage
from models.product import Product
from models.review import Review
from web_flask.forms import AddProductForm
import requests


@app_views.route('/products/<product_id>')
def show_product(product_id):
    product = storage.get("Product", product_id)
    editable = current_user.is_active and product in current_user.products
    count = len(product.reviews) if len(product.reviews) > 0 else 1
    rating = round(sum([review.rating for review in product.reviews]) / count)
    return render_template('product_details.html',
                           product=product,
                           logged_in=current_user.is_active,
                           editable=editable,
                           rating=rating
                           )


@app_views.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    add_form = AddProductForm()

    if add_form.validate_on_submit():
        name = add_form.name.data
        price = add_form.price.data
        image = validate_image(add_form.image.data)
        description = add_form.description.data
        user = storage.get("User", current_user.get_id())
        product = Product(name=name,
                          price=price,
                          image=image,
                          description=description
                          )
        user.products.append(product)
        storage.save()
        return redirect(url_for('app_views.account'))
    else:
        return render_template("add_product.html", form=add_form, logged_in=True)


@app_views.route("/edit_product/<product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = storage.get("Product", product_id)
    edit_form = AddProductForm(name=product.name,
                               price=product.price,
                               image=product.image,
                               description=product.description)
    if edit_form.validate_on_submit():
        if "delete" in request.form:
            storage.delete(product)
            storage.save()
        else:
            product.name = edit_form.name.data
            product.price = edit_form.price.data
            product.image = validate_image(edit_form.image.data)
            product.description = edit_form.description.data
            product.save()
        return redirect(url_for('app_views.account'))
    return render_template("add_product.html", logged_in=True, form=edit_form, editing=True)


@app_views.route("/add_review", methods=["POST"])
@login_required
def add_review():
    rating = int(request.form.get('rating'))
    text = request.form.get('text')
    product_id = request.form.get('product_id')
    review = Review(text=text,
                    rating=rating,
                    user_id=current_user.get_id(),
                    product_id=product_id)

    review.save()
    return jsonify({"rating": rating, "text": text, "product_id": product_id})


def validate_image(url):
    try:
        response = requests.head(url)
        if response.status_code // 100 != 2:
            return "https://shorturl.at/iltB4"
        content_type = response.headers.get('Content-Type', '')
        if content_type.startswith('image/'):
            return url
        else:
            return "https://shorturl.at/iltB4"
    except requests.exceptions.RequestException:
        return "https://shorturl.at/iltB4"
