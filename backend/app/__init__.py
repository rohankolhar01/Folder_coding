from flask import Flask

# Initialize the Flask app
def create_app():
    app = Flask(__name__)

    # Register Blueprints here
    from .routes import main_bp, auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
