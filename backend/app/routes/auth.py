from . import auth_bp
from flask import request, jsonify

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({'message': 'Login endpoint', 'data': data})

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    return jsonify({'message': 'Signup endpoint', 'data': data})
