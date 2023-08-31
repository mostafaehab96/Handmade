from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    products = storage.all("Product")
    return render_template("home.html", products=products)



if __name__ == "__main__":
    app.run()

