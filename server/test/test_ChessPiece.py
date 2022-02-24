import pytest
from app.chess_board import ChessPiece, BOARD_DIMENSION


def test_get_possible_moves(chesspiece: ChessPiece):
    assert chesspiece.get_possible_moves() == []


def test_set_location(chesspiece: ChessPiece):
    # doesn't matter if the location oob or not
    for row in range(-100, 100):
        for col in range(-100, 100):
            chesspiece.set_location(row, col)
            assert chesspiece.row == row and chesspiece.col == col
    chesspiece.row = 0
    chesspiece.col = 0


def test_is_in_range(chesspiece: ChessPiece):
    # not oob test
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            assert chesspiece.is_in_range(row, col) is True

    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]
    for (row, col) in oob_positions:
        assert chesspiece.is_in_range(row, col) is False


def test_is_occupied(chesspiece: ChessPiece):
    chesspiece.is_black_piece = False

    chesspiece.chess_board.board[0][0] = ChessPiece(
        "lol", 0, 0, True, chesspiece.chess_board)
    assert chesspiece.is_occupied(0, 0) is True
    assert chesspiece.is_occupied_by_ally(0, 0) is False
    assert chesspiece.is_occupied_by_opponent(0, 0) is True

    chesspiece.chess_board.board[0][0] = ChessPiece(
        "lol", 0, 0, False, chesspiece.chess_board)
    assert chesspiece.is_occupied(0, 0) is True
    assert chesspiece.is_occupied_by_ally(0, 0) is True
    assert chesspiece.is_occupied_by_opponent(0, 0) is False

    chesspiece.chess_board.board[0][0] = None
    assert chesspiece.is_occupied(0, 0) is False
    assert chesspiece.is_occupied_by_ally(0, 0) is False
    assert chesspiece.is_occupied_by_opponent(0, 0) is False


def test_str(chesspiece):
    chesspiece.is_black_piece = False
    assert chesspiece.__str__() == chesspiece.id + "w"

    chesspiece.is_black_piece = True
    assert chesspiece.__str__() == chesspiece.id + "b"
