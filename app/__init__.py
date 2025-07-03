from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from config import Config

mail = Mail()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    csrf.init_app(app)

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    from app.errors import register_error_handlers
    register_error_handlers(app)

    return app
