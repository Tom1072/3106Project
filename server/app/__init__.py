from flask import Flask
from flask_cors import CORS
from app.routes import routes


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config["SECRET_KEY"] = "secret_key"
    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(routes, url_prefix="/api")

    return app
