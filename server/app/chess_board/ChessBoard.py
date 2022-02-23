from app.chess_board.Pawn import Pawn
from app.chess_board.ChessPiece import ChessPiece

BOARD_DIMENSION = 8


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]

        black_pawn_row = 6
        for black_pawn_col in range(BOARD_DIMENSION):
            self.board[6][black_pawn_col] = Pawn(
                row=black_pawn_row, col=black_pawn_col, is_black_piece=True, chess_board=self)

        white_pawn_row = 1
        for white_pawn_col in range(BOARD_DIMENSION):
            self.board[1][white_pawn_col] = Pawn(
                row=white_pawn_row, col=white_pawn_col, is_black_piece=False, chess_board=self)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_possible_moves(self, row, col):
        return self.board[row][col].get_possible_moves()

    def get_board(self):
        board = []
        for row in self.board:
            board_row = []
            for entry in row:
                board_row.append(
                    entry.__str__() if entry is not None else "  ")
            board.append(board_row)

        return board
