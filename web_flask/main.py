from flask import Flask, render_template, redirect, url_for, flash
from models import storage
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from flask_ckeditor import CKEditor, CKEditorField
from wtforms.validators import DataRequired, URL, Email, EqualTo
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, login_manager, logout_user
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return storage.get("User", user_id)


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    email_confirm = EmailField('Confirm Email',
                               validators=[DataRequired(), Email(), EqualTo('email', 'Email mismatch')])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', 'Password mismatch')])
    address = StringField('Address', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    about = StringField('About', validators=[DataRequired()])
    confirm = SubmitField('Confirm')


class LoginFrom(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Email()])
    login = SubmitField('Login')


@app.route('/', strict_slashes=False)
def home():
    products = storage.all("Product")
    return render_template("home.html", products=products)


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


if __name__ == "__main__":
    app.run()
