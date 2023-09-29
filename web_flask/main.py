from flask import Flask, render_template, redirect, url_for, flash, jsonify
from models import storage
from flask_login import LoginManager, current_user
from web_flask.forms import ContactForm
import smtplib
import os
from web_flask.views import app_views

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
login_manager = LoginManager()
login_manager.init_app(app)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@login_manager.user_loader
def load_user(user_id):
    return storage.get("User", user_id)


@app.route("/status")
def status():
    if current_user.is_active:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "login"})


@app.route('/', strict_slashes=False)
def home():
    products = storage.all("Product")
    if current_user.is_active:
        user = storage.get("User", current_user.get_id())
        products = [product for product in products
                    if product not in user.products]
    logged_in = current_user.is_active
    return render_template("home.html", products=products, logged_in=logged_in)


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_active)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        message = contact_form.message.data
        try:
            send_message(name, email, message)
            return redirect(url_for('home'))
        except:
            flash("Some Error Happened! Message wasn't sent")
            return redirect(url_for('contact'))

    return render_template("contact.html",
                           form=contact_form,
                           logged_in=current_user.is_active)


def send_message(name, email, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        my_email = os.getenv('MY_EMAIL')
        app_passwd = os.getenv('APP_PASSWD')
        all_message = f"Sender:{name}\nemail:{email}\nmessage:{message}"
        connection.login(user=my_email, password=app_passwd)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:New Handmade message\n\n {all_message}")


if __name__ == "__main__":
    app.run()
