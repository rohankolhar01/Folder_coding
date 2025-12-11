from flask import Blueprint, jsonify

support_bp = Blueprint('support_bp', __name__)

@support_bp.route('/', methods=['GET'])
def get_support_info():
    return jsonify({'message': 'Customer support info'})
