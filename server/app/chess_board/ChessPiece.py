from app.chess_board import ChessBoard


class ChessPiece:
    def __init__(self, id: str, row: int, col: int, is_black_piece: bool, chess_board: ChessBoard):
        self.id = id
        self.row = row
        self.col = col
        self.is_black_piece = is_black_piece
        self.chess_board = chess_board

    def get_possible_moves(self) -> list:
        return []

    def move(self, dest_row: int, dest_col: int):
        """Set location of this chess piece
        """
        self.row, self.col = dest_row, dest_col

    def is_in_range(self, row: int, col: int) -> bool:
        return self.chess_board.is_in_range(row, col)

    def is_occupied(self, row: int, col: int) -> bool:
        return self.chess_board.get_piece(row, col) is not None

    def is_occupied_by_ally(self, row: int, col: int) -> bool:
        piece = self.chess_board.get_piece(row, col)
        if piece is not None:
            return piece.is_black_piece == self.is_black_piece
        else:
            return False

    def is_occupied_by_opponent(self, row: int, col: int) -> bool:
        piece = self.chess_board.get_piece(row, col)
        if piece is not None:
            return piece.is_black_piece != self.is_black_piece
        else:
            return False

    def is_blocked_by_ally(self, row: int, col: int) -> bool:
        pass
        
    def __str__(self):
        return ("b" if self.is_black_piece else "w") + self.id
