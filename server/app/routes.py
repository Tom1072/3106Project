from flask import Blueprint, request
from app.chess_board import ChessBoard

routes = Blueprint("routes", __name__)
chess_board = ChessBoard(is_god_board=True)


@routes.route('/move', methods=['GET', 'POST'])
def handle_get_move():
    print(request)
    if request.method == 'GET':
        row, col = int(request.args.get("row")), int(request.args.get("col"))
        possible_moves = chess_board.get_possible_moves(row, col)
        response_payload = {
            "availablePositions": possible_moves,
        }

        return response_payload

    elif request.method == 'POST':
        org_post = request.json["prev"]
        dest_post = request.json["next"]
        org_row, org_col = org_post["row"], org_post["col"]
        dest_row, dest_col = dest_post["row"], dest_post["col"]

        response_payload = {}
        if chess_board.move(org_row, org_col, dest_row, dest_col):
            response_payload = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": dest_row, "col": dest_col},
                "board": chess_board.get_board()
            }
        else:
            # No change
            response_payload = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": org_row, "col": org_col},
                "board": chess_board.get_board()
            }

        return response_payload
