from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    from app.routes import register_blueprints
    register_blueprints(app)

    return app
