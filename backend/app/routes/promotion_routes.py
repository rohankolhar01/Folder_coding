from flask import Blueprint, jsonify

promotion_bp = Blueprint('promotion_bp', __name__)

@promotion_bp.route('/', methods=['GET'])
def get_promotions():
    return jsonify({'message': 'List promotions'})
