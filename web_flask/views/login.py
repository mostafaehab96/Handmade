from web_flask.views import app_views
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user
from models import storage
from models.user import User
from models.cart import Cart
from web_flask.forms import SignupForm, LoginFrom
from werkzeug.security import check_password_hash


@app_views.route('/signup', methods=["GET", "POST"])
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
            return redirect(url_for('app_views.signup'))
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


@app_views.route('/login', methods=["GET", "POST"])
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
                return redirect(url_for('app_views.login'))
        else:
            flash("This email doesn't exist signup if you don't have an account")
            return redirect(url_for('app_views.login'))
    return render_template('login.html', form=login_form)


@app_views.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
