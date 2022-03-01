from app.chess_board import ChessBoard, ChessPiece, Pawn, GodPiece
import pytest


@pytest.fixture(scope="function")
def chessboard() -> ChessBoard:
    return ChessBoard()

@pytest.fixture(scope="function")
def chesspiece() -> ChessPiece:
    chessboard = ChessBoard()
    chesspiece = ChessPiece(id="", row=0, col=0, is_black_piece=False, chess_board=chessboard)
    chessboard.board[0][0] = chesspiece
    return chesspiece

@pytest.fixture(scope="function")
def pawn(chessboard) -> Pawn:
    pawn_piece = Pawn(row=0, col=0, is_black_piece=False, chess_board=chessboard)
    chessboard.clear_board()
    chessboard.board[0][0] = pawn
    return pawn_piece

@pytest.fixture(scope="function")
def god(chessboard) -> GodPiece:
    god_piece = GodPiece(row=0, col=0, is_black_piece=False, chess_board=chessboard)
    chessboard.clear_board()
    chessboard.board[0][0] = GodPiece
    return god_piece
