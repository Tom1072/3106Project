from app.chess_board.ChessPiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, row, col, is_black_piece, chess_board):
        super().__init__("p", row, col, is_black_piece, chess_board)
        self.is_first_move = True
    
    def get_possible_moves(self):
        attack_moves = None
        non_attack_moves = None
        
        if self.is_black_piece:
            # Move downward
            non_attack_moves = [(-1, 0)]
            attack_moves = [(-1, -1), (-1, 1)]
        else:
            # Move upward
            non_attack_moves = [(1, 0)]
            attack_moves = [(1, -1), (1, 1)]

        non_attack_dests = []
        for non_attack_move in non_attack_moves:
            dest_row, dest_col = self.row + non_attack_move[0], self.col + non_attack_move[1]
            if not self.is_out_of_bound(dest_row, dest_col) and not self.is_occupied_by_allies(dest_row, dest_col):
                non_attack_dests.append((dest_row, dest_col))
        
        attack_dests = []
        for attack_move in attack_moves:
            dest_row, dest_col = self.row + attack_move[0], self.col + attack_move[1]
            if not self.is_out_of_bound(dest_row, dest_col) and self.is_occupied_by_oppenent(dest_row, dest_col):
                attack_dests.append((dest_row, dest_col))
        
        return {
            "attack_dests": attack_dests,
            "non_attack_dests": non_attack_dests
        }
    
    

         
    
