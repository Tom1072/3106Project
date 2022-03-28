from app.algorithms import Algorithms
from app.algorithms.AlphaBeta import AlphaBeta
from app.algorithms.AlphaBetaPruning import AlphaBetaPruning

class AlgorithmService:
    def __init__(self):
        self.algorithm = AlphaBeta()
    
    def switchAlgorithm(self, algorithm_code):
        if algorithm_code == Algorithms.ALPHA_BETA.value:
            self.algorithm = AlphaBeta() 
        elif algorithm_code == Algorithms.ALPHA_BETA_PRUNING.value:
            self.algorithm = AlphaBetaPruning() 
        
    # Method for making the next move based on the current broad
    def get_next_move(self, board, chess_service):
        return self.algorithm.next_move(board, chess_service)
