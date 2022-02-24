import pytest
from test.utils import dict_list_to_tuple_list
from app.chess_board import ChessPiece, Pawn, ChessBoard


def test_get_possible_moves(pawn):
    chessboard = pawn.chess_board
    pawn.row, pawn.col = 3, 3

    # Possible first move when it's black pawn with no oponent
    pawn.is_black_piece = True
    pawn.is_first_move = True
    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = dict_list_to_tuple_list([
        {"row": 2, "col": 3},
        {"row": 1, "col": 3}
    ])
    assert possible_moves == expected_possible_moves

    # Possible first move when it's white pawn with no oponent
    pawn.is_black_piece = False
    pawn.is_first_move = True
    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = dict_list_to_tuple_list([
        {"row": 4, "col": 3},
        {"row": 5, "col": 3}
    ])
    assert possible_moves == expected_possible_moves

    # Possible non-first move when it's black pawn with no oponent
    pawn.is_black_piece = True
    pawn.is_first_move = False
    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = dict_list_to_tuple_list([
        {"row": 2, "col": 3},
    ])
    assert possible_moves == expected_possible_moves

    # Possible non-first move when it's white pawn with no oponent
    pawn.is_black_piece = False
    pawn.is_first_move = False
    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = dict_list_to_tuple_list([
        {"row": 4, "col": 3},
    ])
    assert possible_moves == expected_possible_moves

    # Possible first moves with ally oponent on its non-attack path
    pawn.is_black_piece = True
    pawn.is_first_move = True
    chessboard.board[2][3] = ChessPiece(
        id="lol", row=2, col=3, is_black_piece=pawn.is_black_piece, chess_board=chessboard)

    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = []
    assert possible_moves == expected_possible_moves

    # Possible first moves with ally oponent on its attack path
    pawn.is_black_piece = True
    pawn.is_first_move = True
    chessboard.clear_board()
    chessboard.board[2][2] = ChessPiece(
        id="lol", row=2, col=2, is_black_piece=pawn.is_black_piece, chess_board=chessboard)

    possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    expected_possible_moves = [
        {"row": 4, "col": 3},
        {"row": 5, "col": 3}
    ]
    assert possible_moves == expected_possible_moves
