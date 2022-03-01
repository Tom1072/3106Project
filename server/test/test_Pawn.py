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

    # # Possible first moves with ally oponent on its non-attack path
    # pawn.is_black_piece = True
    # pawn.is_first_move = True
    # chessboard.board[2][3] = ChessPiece(
    #     id="lol", row=2, col=3, is_black_piece=pawn.is_black_piece, chess_board=chessboard)

    # possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    # expected_possible_moves = []
    # assert possible_moves == expected_possible_moves

    # Possible first moves with opponent on its attack path
    # chessboard.clear_board()

    # pawn.is_black_piece = True
    # pawn.is_first_move = False
    # pawn.row, pawn.col = 2, 2
    
    # chessboard.board[2][2] = pawn
    # chessboard.board[3][1] = ChessPiece(id="lol1", row=3, col=1, is_black_piece= not pawn.is_black_piece, chess_board=chessboard)
    # chessboard.board[3][3] = ChessPiece(id="lol2", row=3, col=3, is_black_piece= not pawn.is_black_piece, chess_board=chessboard)
    # print(chessboard.get_board())

    # possible_moves = dict_list_to_tuple_list(pawn.get_possible_moves())
    # expected_possible_moves = dict_list_to_tuple_list([
    #     {"row": 3, "col": 1},
    #     {"row": 3, "col": 2}
    # ])
    assert possible_moves == expected_possible_moves
