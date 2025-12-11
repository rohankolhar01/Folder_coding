from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Handle login logic
    return jsonify({'message': 'Login endpoint'})

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Handle signup logic
    return jsonify({'message': 'Signup endpoint'})