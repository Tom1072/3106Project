from app.chess_board import ChessBoard
import pytest


@pytest.fixture(scope="module")
def chessboard() -> ChessBoard:
    chessboard = ChessBoard()
    return chessboard
