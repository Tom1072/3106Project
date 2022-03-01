from flask import Flask
from app.routes import routes
from flask_cors import CORS, cross_origin

cors = CORS()

def create_app():
    app = Flask(__name__, template_folder="./templates")
    app.config["SECRET_KEY"] = "secret_key"
    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(routes)

    cors.init_app(app)

    return app
