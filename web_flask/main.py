
from flask import Flask, render_template, redirect, url_for, flash, jsonify
from models import storage
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models.product import Product
from forms import SignupForm, LoginFrom, AddProductForm
from models.user import User
from models.cart import Cart

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
login_manager = LoginManager()
login_manager.init_app(app)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@login_manager.user_loader
def load_user(user_id):
    return storage.get("User", user_id)


@app.route('/', strict_slashes=False)
def home():
    products = storage.all("Product")
    logged_in = current_user.is_active
    return render_template("home.html", products=products, logged_in=logged_in)


@app.route('/products/<product_id>')
def show_product(product_id):
    product = storage.get("Product", product_id)
    return render_template('product_details.html', product=product, logged_in=current_user.is_active)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    sign_form = SignupForm()

    if sign_form.validate_on_submit():
        name = sign_form.name.data
        email = sign_form.email.data
        password = sign_form.password.data
        address = sign_form.address.data
        postal_code = sign_form.postal_code.data
        about = sign_form.about.data

        if storage.filter("User", "email", email):
            flash("You already have an account login instead")
            return redirect(url_for('signup'))
        user = User(name=name,
                    email=email,
                    password=password,
                    address=address,
                    postal_code=postal_code,
                    about=about,
                    cart=Cart()
                    )
        user.save()
        login_user(user)
        return redirect(url_for('home'))

    return render_template('signup.html', form=sign_form)


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginFrom()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = storage.filter("User", "email", email)
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Wrong password please try again")
                return redirect(url_for('login'))
        else:
            flash("This email doesn't exist signup if you don't have an account")
            return redirect(url_for('login'))
    return render_template('login.html', form=login_form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_cart/<product_id>')
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


@app.route("/cart/count")
def cart_count():
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        product_ids = [product.id for product in user.cart.products]
        count = len(product_ids)
        return jsonify({"count": f"{count}", "product_ids": product_ids}), 200
    return jsonify({"count": 0})


@app.route('/cart', methods=["GET", "POST"])
def cart():
    selected_products = []
    total_price = 0
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        selected_products = user.cart.products
        total_price = sum([product.price for product in selected_products])
    return render_template("cart-details.html",
                           products=selected_products,
                           price=total_price,
                           logged_in=current_user.is_active)


@app.route('/cart/remove/<product_id>')
@login_required
def cart_remove(product_id):
    user = storage.get("User", current_user.get_id())
    product = storage.get("Product", product_id)
    user.cart.products.remove(product)
    storage.save()

    return jsonify({"status": "ok"}), 200


@app.route('/account')
@login_required
def account():
    user = storage.get("User", current_user.get_id())
    return render_template('user_profile.html', user=user, logged_in=True)


@app.route("/add_product", methods=["POST"])
@login_required
def add_product():
    add_form = AddProductForm()

    if add_form.validate_on_submit():
        name = add_form.name.data
        price = add_form.price.data
        image = add_form.image.data
        description = add_form.description.data
        user = storage.get("User", current_user.get_id())
        product = Product(name=name,
                          price=price,
                          image=image,
                          description=description
                          )
        user.products.append(product)
        storage.save()

    return redirect(url_for('account'))

@app.route("/orders")
@login_required
def view_orders():
    user = storage.get("User", current_user.get_id())
    return render_template("orders.html", orders=user.orders, logged_in=current_user.is_active)


if __name__ == "__main__":
    app.run()
