"""Handles the root and status routes"""
from api.views import app_views
from flask import make_response, jsonify



@app_views.route('/', strict_slashes=False)
def status():
    return make_response(jsonify({'status': 200}), 200)