from flask import Blueprint, request, jsonify

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['GET'])
def list_products():
    return jsonify({'message': 'List all products'})
