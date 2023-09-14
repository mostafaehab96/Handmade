from views import app_views
from models import storage
from flask import Flask, make_response, jsonify

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_dp(error):
    """Closes storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles 404 not found error"""
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5001)
