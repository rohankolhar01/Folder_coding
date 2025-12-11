from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify({'message': 'User registration endpoint'})

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'message': 'User login endpoint'})
