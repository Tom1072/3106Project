from flask import Blueprint, request
from app.chess_board import ChessBoard

routes = Blueprint("routes", __name__)
chess_board = ChessBoard()


@routes.route('/move', methods=['GET', 'POST'])
def handle_get_move():
    print("REQUEST:", request.json)
    return "Requested"
    if request.method == 'GET':
        row, col = request.json["position"]["row"], request.json["position"]["col"]

        possible_moves = chess_board.get_possible_moves(row, col)
        response_payload = {
            "availablePositions": possible_moves,
        }

        return response_payload

    elif request.method == 'POST':
        org_post = request.json["move"]["prev"]
        dest_post = request.json["move"]["next"]
        org_row, org_col = org_post["row"], org_post["col"]
        dest_row, dest_col = dest_post["row"], dest_post["col"]

        response_payload = {}
        if chess_board.move(org_row, org_col, org_row, org_col):
            response_payload["move"] = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": dest_row, "col": dest_col}
            }
        else:
            # No change
            response_payload["move"] = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": org_row, "col": org_col}
            }

        return response_payload
