from api.views import app_views
from flask import make_response, jsonify
from models.category import Category



@app_views.route('/categories', strict_slashes=False)
def get_categories():
    return jsonify(Category.all_records())



