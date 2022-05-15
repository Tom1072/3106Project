import chess
from app.algorithms import ALGORITHMS

class AlgorithmService:
    def __init__(self):
        self.algorithm = ALGORITHMS["minmax"]
    
    def switchAlgorithm(self, algorithm_code: str):
        self.algorithm = ALGORITHMS[algorithm_code]
        
    # Method for making the next move based on the current broad
    def get_next_move(self, board: chess.Board):
        move = self.algorithm.next_move(board)
        return move
