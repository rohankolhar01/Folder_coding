from flask import Blueprint, jsonify

general_bp = Blueprint('general', __name__)

@general_bp.route('/about', methods=['GET'])
def about():
    return jsonify({'message': 'About endpoint'})