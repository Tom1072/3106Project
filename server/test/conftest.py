from app.chess_board import ChessBoard, ChessPiece, Pawn
import pytest


@pytest.fixture(scope="module")
def chessboard() -> ChessBoard:
    return ChessBoard()

@pytest.fixture(scope="module")
def chesspiece() -> ChessPiece:
    chessboard = ChessBoard()
    chesspiece = ChessPiece(id="", row=0, col=0, is_black_piece=False, chess_board=chessboard)
    chessboard.board[0][0] = chesspiece
    return chesspiece

@pytest.fixture(scope="function")
def pawn(chessboard) -> Pawn:
    pawn = Pawn(row=0, col=0, is_black_piece=False, chess_board=chessboard)
    chessboard.clear_board()
    chessboard.board[0][0] = pawn
    return pawn
