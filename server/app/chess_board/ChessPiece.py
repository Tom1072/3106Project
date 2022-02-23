class ChessPiece:
    def __init__(self, id, row, col, is_black_piece, chess_board):
        self.id = id 
        self.row = row
        self.col = col
        self.is_black_piece = is_black_piece
        self.chess_board = chess_board

    def get_possible_moves(self):
        return []
    
    def move(self, dest_row, dest_col):
        if (dest_row, dest_col) in self.get_possible_moves():
            self.row, self.col = dest_row, dest_col
            return True
        else:
            return False
    
    def is_out_of_bound(row, col):
        return row >= 0 and row <= 7 and col >= 0 and col <= 7
    
    def is_occupied_by_ally(row, col):
        return False
    
    def is_occupied_by_opponent(row, col):
        return True
    
    def __str__(self):
        return ("b" if self.is_black_piece else "w") + self.id
            