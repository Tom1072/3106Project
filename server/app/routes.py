from flask import Blueprint, request
from app.ChessService import ChessService

routes = Blueprint("routes", __name__)
chess_service = ChessService()

search_algorithm = None


@routes.route('/move', methods=['GET', 'POST'])
def handle_get_move():
    print(request)
    if request.method == 'GET':
        row, col = int(request.args.get("row")), int(request.args.get("col"))
        # possible_moves = chess_board.get_possible_moves(row, col)
        possible_moves = chess_service.get_possible_moves(row, col)
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
        # if chess_board.move(org_row, org_col, dest_row, dest_col):
        if chess_service.move(org_row, org_col, dest_row, dest_col):
            # keep track of the board after player makes a move
            boardAfterMove = chess_service.get_board()
            # computer turn using AI model
            """
                comp_move = chess_service.minimaxRoot(3,board,True)
                org_comp_post = comp_move["prev"]
                dest_comp_post = comp_move["next"]
                org_comp_row, org_comp_col = org_comp_post["row"], org_comp_post["col"]
                dest_comp_row, dest_comp_col = dest_comp_post["row"], dest_comp_post["col"]

                
                chess_service.move(org_comp_row, org_comp_col, dest_comp_row, dest_comp_col)
                
            """

            response_payload = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": dest_row, "col": dest_col},
                "board": chess_service.get_board(),
                "is_black_turn": chess_service.is_black_turn(),
                "outcome": chess_service.get_game_outcome()
            }

        else:
            # No change
            response_payload = {
                "prev": {"row": org_row, "col": org_col},
                "next": {"row": org_row, "col": org_col},
                "board": chess_service.get_board(),
                "is_black_turn": chess_service.is_black_turn(),
                "outcome": chess_service.get_game_outcome()
            }

        print(response_payload)
        return response_payload


@routes.route('/reset', methods=['POST'])
def handle_reset():
    print(request)
    chess_service.reset()
    response_payload = {
        "board": chess_service.get_board(),
        "is_black_turn": chess_service.is_black_turn(),
        "outcome": chess_service.get_game_outcome()
    }
    return response_payload
