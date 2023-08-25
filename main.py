from models import app
from models.user import User
from models.product import Product
from models.order import Order
from models.review import Review
from flask import jsonify

@app.route('/', strict_slashes=False)
def hello():
    return "Hello, World!"

@app.route('/first_user', strict_slashes=False)
def first_user():
    first = User.query.first()
    return jsonify(first.to_dict())



if __name__ == "__main__":
    app.run()

