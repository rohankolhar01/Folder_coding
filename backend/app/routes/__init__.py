from flask import Blueprint

def register_routes(app):
    from .auth_routes import auth_bp
    from .user_routes import user_bp
    from .general_routes import general_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(general_bp, url_prefix='/')