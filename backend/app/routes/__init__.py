from flask import Blueprint

# Blueprints for modular routes
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

from . import main, auth
