from app.chess_board.Pawn import Pawn
from app.chess_board.ChessPiece import ChessPiece

BOARD_DIMENSION = 8


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_DIMENSION)]
                      for _ in range(BOARD_DIMENSION)]

        black_pawn_row = 6
        for black_pawn_col in range(BOARD_DIMENSION):
            self.board[6][black_pawn_col] = Pawn(
                row=black_pawn_row, col=black_pawn_col, is_black_piece=True, chess_board=self)

        white_pawn_row = 1
        for white_pawn_col in range(BOARD_DIMENSION):
            self.board[1][white_pawn_col] = Pawn(
                row=white_pawn_row, col=white_pawn_col, is_black_piece=False, chess_board=self)

    def get_piece(self, row: int, col: int) -> ChessPiece:
        """Get a chess piece on the board

        Args:
            row (int): row of the board
            col (int): column of the board

        Returns:
            ChessPiece: the chess piece on the board at the input location
        """
        if self.is_in_range(row, col):
            return self.board[row][col]
        else:
            return None  # No piece

    def set_piece(self, row: int, col: int, piece: ChessPiece) -> ChessPiece:
        """Set a chess piece on the board, replace and return the existing one

        Args:
            row (int): column of the board
            col (int): row of the board
            piece (ChessPiece): chess piece to set

        Returns:
            ChessPiece: the previous chess piece at that location
        """
        if self.is_in_range(row, col):
            old_piece = self.board[row][col]
            self.board[row][col] = piece
            return old_piece
        else:
            return None

    def remove_piece(self, row: int, col: int) -> ChessPiece:
        """Remove and return a chess piece from the board

        Args:
            row (int): column of the board
            col (int): row of the board

        Returns:
            ChessPiece: the previous chess piece at that location
        """
        piece = self.get_piece(row, col)
        self.set_piece(row, col, None)
        return piece

    def get_possible_moves(self, row: int, col: int) -> list:
        """Find the possible move of a chess piece on the board at the provided location

        Args:
            row (int): row of the board
            col (int): column of the board

        Returns:
            list: a list [{"row": dest_row, "col": dest_col}] that represents possible moves fromt the input
            position
        """
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.get_possible_moves()
        else:
            return []  # No possible moves from an non-existing chess piece

    def move(self, org_row: int, org_col: int, dest_row: int, dest_col: int) -> bool:
        """Move a chess piece on the board at the provided location to the destination position

        Args:
            org_row (int): row of the chess piece at the original position
            org_col (int): column of the chess piece at the original position
            dest_row (int): row of the destination position
            dest_col (int): column of the destination position

        Returns:
            bool: True if the move succeeded, False otherwise
        """
        piece = self.get_piece(org_row, org_col)
        if piece is not None and self.is_in_range(dest_row, dest_col):
            piece.set_location(dest_row, dest_col)

            # Remove the piece from the org position
            self.remove_piece(org_row, org_col)

            # Set destination position to be that removed piece
            self.set_piece(dest_row, dest_col, piece)
            return True
        else:
            return False

    def get_board(self):
        board = []
        for row in self.board:
            board_row = []
            for entry in row:
                board_row.append(
                    entry.__str__() if entry is not None else "  ")
            board.append(board_row)
        return board

    def is_in_range(_, row: int, col: int) -> bool:
        """ Find out if the position is inside the chessboard
        """
        return row >= 0 and row < BOARD_DIMENSION and col >= 0 and col < BOARD_DIMENSION
