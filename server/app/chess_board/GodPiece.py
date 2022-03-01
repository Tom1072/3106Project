from app.chess_board.ChessPiece import ChessPiece, ChessBoard


class GodPiece(ChessPiece):
    def __init__(self, row: int, col: int, is_black_piece: bool, chess_board: ChessBoard):
        super().__init__("g", row, col, is_black_piece, chess_board)

    def get_possible_moves(self) -> list:
        possible_moves = []
        for row in range(8):
            for col in range(8):
                if (row != self.row or col != self.col):
                    possible_moves.append({"row": row, "col": col})
        return possible_moves


