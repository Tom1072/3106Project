import pytest
from app.chess_board import ChessBoard, BOARD_DIMENSION, ChessPiece


def test_getboard(chessboard: ChessBoard):
    assert chessboard.get_board() == [
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ]


def test_set_piece(chessboard: ChessBoard):
    # not oob test
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            new_piece = ChessPiece("lol", row, col, True, chessboard)
            old_piece = chessboard.set_piece(row, col, new_piece)
            assert chessboard.board[row][col] == new_piece

            chessboard.set_piece(row, col, old_piece)
            assert old_piece == chessboard.board[row][col]

    # oob test
    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]
    for (row, col) in oob_positions:
        old_piece = chessboard.set_piece(
            row, col, ChessPiece("lol", row, col, True, chessboard))
        assert old_piece is None


def test_get_piece(chessboard: ChessBoard):
    # not oob test
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            piece = chessboard.get_piece(row, col)
            assert piece == chessboard.board[row][col]

    # oob test
    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]
    for (row, col) in oob_positions:
        piece = chessboard.get_piece(row, col)
        assert piece is None


def test_move(chessboard: ChessBoard):
    # not oob test
    for row in range(BOARD_DIMENSION-1):
        for col in range(BOARD_DIMENSION-1):
            piece = chessboard.board[row][col]
            if piece is None:
                # we shouldn't be able to move a "None" piece
                status = chessboard.move(row, col, row+1, col+1)
                assert status is False
            else:
                status = chessboard.move(row, col, row+1, col+1)
                assert status is True
                assert chessboard.board[row+1][col+1] == piece
            # regardless, aftermove, the original position should be "None"
            assert chessboard.board[row][col] is None

    # oob test
    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]

    # original position is oob
    for (row, col) in oob_positions:
        assert chessboard.move(row, col, 0, 0) is False

    # destination is oob
    for (row, col) in oob_positions:
        chessboard.board[0][0] = ChessPiece("lol", row, col, True, chessboard)
        assert chessboard.move(0, 0, row, col) is False


def test_get_possible_moves(chessboard: ChessBoard):
    # only test the data structure returned, regardless of whether the move is value

    # not oob test
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            possible_moves = chessboard.get_possible_moves(row, col)
            assert type(possible_moves) is list
            if len(possible_moves) > 0:
                for move in possible_moves:
                    assert type(move["row"]) is int
                    assert type(move["col"]) is int

    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]
    for (row, col) in oob_positions:
        possible_moves = chessboard.get_possible_moves(row, col)
        assert type(possible_moves) is list
        assert len(possible_moves) == 0


def test_is_in_range(chessboard: ChessBoard):
    # not oob test
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            assert chessboard.is_in_range(row, col) is True

    oob_positions = [(-1, -1), (8, 8), (-1, 0), (0, -1)]
    for (row, col) in oob_positions:
        assert chessboard.is_in_range(row, col) is False

def test_clear_board(chessboard: ChessBoard):
    chessboard.clear_board()
    for row in chessboard.board:
        for entry in row:
            assert entry is None
