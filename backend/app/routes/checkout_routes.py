from flask import Blueprint, jsonify

checkout_bp = Blueprint('checkout_bp', __name__)

@checkout_bp.route('/', methods=['POST'])
def checkout():
    return jsonify({'message': 'Checkout endpoint'})
