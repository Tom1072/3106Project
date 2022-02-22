from flask import Blueprint

routes = Blueprint("routes", __name__)


@routes.route('/')
def func():
    return "This is an endpoint"