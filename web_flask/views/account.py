from web_flask.views import app_views
from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user
from models import storage


@app_views.route('/account')
@login_required
def account():
    user = storage.get("User", current_user.get_id())
    return render_template('user_profile.html', user=user, logged_in=True)


@app_views.route("/edit_user/<user_id>", methods=["POST"])
@login_required
def edit_user(user_id):
    user = storage.get("User", user_id)
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    postal_code = request.form['postal_code']
    about = request.form['about']
    user.name = name
    user.email = email
    user.address = address
    user.postal_code = postal_code
    user.about = about
    user.save()
    return redirect(url_for('app_views.account'))
