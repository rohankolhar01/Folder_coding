from . import main_bp
from flask import jsonify

@main_bp.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask backend API!'})
