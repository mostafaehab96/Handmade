from flask import Flask, render_template, redirect, url_for, request
from models import storage
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_manager, logout_user, current_user
from models.user import User
from models.product import Product
from forms import SignupForm, LoginFrom
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
login_manager = LoginManager()
login_manager.init_app(app)
bootstrap = Bootstrap5(app)

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
    return render_template("home.html", products=products, logged=logged_in)


@app.route('/products/<product_id>')
def show_product(product_id):
    product = storage.get("Product", product_id)
    print(product)
    return render_template('product_details.html', product=product)


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
        user = User(name=name,
                    email=email,
                    password=password,
                    address=address,
                    postal_code=postal_code,
                    about=about
                    )
        user.save()
        login_user(user)
        return redirect(url_for('home'))

    return render_template('signup.html', form=sign_form)


@app.route('/login')
def login():
    login_form = LoginFrom()
    return render_template('login.html', form=login_form)


@app.route('/cart', methods=["GET", "POST"])
def cart():
    product_ids = request.args.get('productIds').split(',')
    products = storage.all("Product")
    selected_products = [product for product in products if product.id in product_ids]
    total_price = sum([product.price for product in selected_products])
    return render_template("cart-details.html", products=selected_products, price=total_price)



if __name__ == "__main__":
    app.run()
