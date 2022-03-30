import chess
from app.algorithms import Algorithms
from app.algorithms.MinimaxSearch import MinimaxSearch
from app.algorithms.AlphaBetaPruning import AlphaBetaPruning

class AlgorithmService:
    def __init__(self):
        self.algorithm = MinimaxSearch()
    
    def switchAlgorithm(self, algorithm_code: str):
        if algorithm_code == Algorithms.MINIMAX.value:
            self.algorithm = MinimaxSearch() 
        elif algorithm_code == Algorithms.ALPHA_BETA_PRUNING.value:
            self.algorithm = AlphaBetaPruning() 
        
    # Method for making the next move based on the current broad
    def get_next_move(self, board: chess.Board):
        move = self.algorithm.next_move(board)
        return move
