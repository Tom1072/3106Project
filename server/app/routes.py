from flask import Blueprint, request
from app.chess_board import ChessBoard

routes = Blueprint("routes", __name__)
chess_board = ChessBoard()


@routes.route('/api/move', methods=['GET', 'POST'])
def handle_get_move():
    if request.method == 'GET':
        row, col = request.json["position"]["row"], request.json["position"]["col"]

        possible_moves = chess_board.get_possible_moves(row, col)
        response_payload = {
            "availablePositions": possible_moves,
            "request_body": request.json
        }

        return response_payload

    elif request.method == 'POST':
        org_post = request.json["move"]["prev"]
        dest_post = request.json["move"]["next"]
        org_row, org_col = org_post["row"], org_post["col"]
        dest_row, dest_col = dest_post["row"], dest_post["col"]


        response_payload = {
            "board": chess_board.get_board(),
            "request_body": request.json
        }
        return response_payload
