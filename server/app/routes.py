from flask import Blueprint, request
from app.chess_board import ChessBoard

routes = Blueprint("routes", __name__)
chess_board = ChessBoard()


@routes.route('/api/mouse-clicked', methods=['POST'])
def handle_mouse_clicked():
    row, col = request.json["position"]["row"], request.json["position"]["col"]

    response_payload = {
        "board": chess_board.get_board()
    }
    return response_payload



@routes.route('/api/', methods=['GET'])
def handle_test():
    return "<h1>Hello world</h1>"
