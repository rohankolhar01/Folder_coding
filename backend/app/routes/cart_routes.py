from flask import Blueprint, jsonify

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/', methods=['GET'])
def get_cart():
    return jsonify({'message': 'Get cart items'})
