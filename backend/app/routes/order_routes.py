from flask import Blueprint, jsonify

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/', methods=['GET'])
def get_orders():
    return jsonify({'message': 'List user orders'})
