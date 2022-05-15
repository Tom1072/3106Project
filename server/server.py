from app import routes
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="../client/build/", static_url_path="")
CORS(app)

app.config["SECRET_KEY"] = "secret_key"
app.config["CORS_HEADERS"] = "Content-Type"

app.register_blueprint(routes, url_prefix="/api")

@app.route("/")
@cross_origin()
def serve_react():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
