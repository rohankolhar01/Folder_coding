from flask import Blueprint, jsonify

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/', methods=['GET'])
def get_reviews():
    return jsonify({'message': 'List product reviews'})
