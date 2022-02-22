from flask import Flask
from flask_socketio import SocketIO
from app.routes import routes


socketio = SocketIO()


def create_app():
    app = Flask(__name__, template_folder="./templates")
    app.config["SECRET_KEY"] = "secret_key"
    app.config["CORS_HEADERS"] = "Content-Type"
    app.register_blueprint(routes)

    socketio.init_app(app)

    return app