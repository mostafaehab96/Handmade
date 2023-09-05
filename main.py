from flask import Flask, render_template
from models import storage
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from flask_ckeditor import CKEditor, CKEditorField
from wtforms.validators import DataRequired, URL, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    email_confirm = EmailField('Confirm Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    about = CKEditorField('About', validators=[DataRequired()])
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


@app.route('/signup')
def signup():
    sign_form = SignupForm()

    return render_template('signup.html', form=sign_form)


@app.route('/login')
def login():
    login_form = LoginFrom()
    return render_template('login.html', form=login_form)

if __name__ == "__main__":
    app.run()
