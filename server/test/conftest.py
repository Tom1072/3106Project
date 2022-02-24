from app.chess_board import ChessBoard, ChessPiece
import pytest


@pytest.fixture(scope="module")
def chessboard() -> ChessBoard:
    return ChessBoard()

@pytest.fixture(scope="module")
def chesspiece() -> ChessPiece:
    return ChessPiece(id="", row=1, col=0, is_black_piece=False, chess_board=ChessBoard())

