from flask import Flask
from configure import Config    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes_main import main_bp
    app.register_blueprint(main_bp)

    return app