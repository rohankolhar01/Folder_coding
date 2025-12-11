from flask import Blueprint

def register_blueprints(app):
    from app.routes.user_routes import user_bp
    from app.routes.product_routes import product_bp
    from app.routes.cart_routes import cart_bp
    from app.routes.checkout_routes import checkout_bp
    from app.routes.order_routes import order_bp
    from app.routes.review_routes import review_bp
    from app.routes.promotion_routes import promotion_bp
    from app.routes.analytics_routes import analytics_bp
    from app.routes.support_routes import support_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(cart_bp, url_prefix='/api/cart')
    app.register_blueprint(checkout_bp, url_prefix='/api/checkout')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(review_bp, url_prefix='/api/reviews')
    app.register_blueprint(promotion_bp, url_prefix='/api/promotions')
    app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
    app.register_blueprint(support_bp, url_prefix='/api/support')
