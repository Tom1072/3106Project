import chess
from app.algorithms.SearchInterface import SearchInterface

class MinimaxSearch(SearchInterface):
    def __init__(self) -> None:
        super().__init__()
        self.max_depth = self.MAX_DEPTH

    def next_move(self, initial_state: chess.Board) -> chess.Move:
        """Return the best move from the state "initial_state"
        Args:
            initial_state (chess.Board): _description_
        Returns:
            chess.Move: the best move
        """
        print("Minimax AI Playing...")
        return self.minimax(initial_state, self.max_depth)

    def to_move(self, state: chess.Board) -> chess.COLORS:
        """The player whose turn it is to move in state "state"
        Args:
            state (chess.Board): the current state of the game
        Returns:
            chess.COLORS: the player whose turn it is to move
        """
        return state.turn
    
    def action(self, state: chess.Board) -> list[chess.Move]:
        """the set of possible moves in state "state"

        Args:
            state (chess.Board): the current state of the game
        Returns:
            list[chess.Move]: the set of possible moves
        """
        return state.legal_moves

    def result(self, state: chess.Board, action: chess.Move) -> chess.Board:
        """The transion model which defines the state resulting 
        from taking the action "action" in state "state"

        Args:
            state (chess.Board): the current state of the game
            action (chess.Move): the action to be taken
        Returns:
            chess.Board: the resulting state
        """
        resulting_state = state.copy()
        resulting_state.push(action)
        return resulting_state

    def is_terminal(self, board: chess.Board, depth: int) -> bool:
        """Return True if the state "board" is a terminal state,
        False otherwise
        """
        if depth == 0 or board.is_game_over():
            return True
        return False

    def utility(self, board: chess.Board) -> int:
        wp = len(board.pieces(chess.PAWN, chess.WHITE))
        bp = len(board.pieces(chess.PAWN, chess.BLACK))
        wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(board.pieces(chess.ROOK, chess.WHITE))
        br = len(board.pieces(chess.ROOK, chess.BLACK))
        wq = len(board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    
        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
        
        pawnsq = sum([self.PAWN_TABLE[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
        pawnsq= pawnsq + sum([-self.PAWN_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.PAWN, chess.BLACK)])
        knightsq = sum([self.KNIGHT_TABLE[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
        knightsq = knightsq + sum([-self.KNIGHT_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.KNIGHT, chess.BLACK)])
        bishopsq= sum([self.BISHOP_TABLE[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
        bishopsq= bishopsq + sum([-self.BISHOP_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.BISHOP, chess.BLACK)])
        rooksq = sum([self.ROOK_TABLE[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
        rooksq = rooksq + sum([-self.ROOK_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.ROOK, chess.BLACK)])
        queensq = sum([self.QUEEN_TABLE[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
        queensq = queensq + sum([-self.QUEEN_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.QUEEN, chess.BLACK)])
        kingsq = sum([self.KING_TABLE[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
        kingsq = kingsq + sum([-self.KING_TABLE[chess.square_mirror(i)] 
                                        for i in board.pieces(chess.KING, chess.BLACK)])
        
        boardvalue = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
        if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999

        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0
        
        eval = boardvalue
        if board.turn:
            return eval
        else:
            return -eval

    def minimax(self, board: chess.Board, depth: int) -> chess.Move:
        """Return the minimax value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
        Returns:
            chess.Move: the best move
        """
        (_, move) = self.max_value(board, depth)
        return move if move != None else chess.Move.null()

    def max_value(self, board: chess.Board, depth: int) -> tuple:
        """Return the max value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
        Returns:
            tuple(int, chess.Move): the max value of the state and the move that leads to it
        """
        if self.is_terminal(board, depth):
            return (self.utility(board), None)
        v = -float('inf')
        move = None
        for a in self.action(board):
            (v2, _) = self.min_value(self.result(board, a), depth - 1)
            if v2 > v:
                (v, move) = (v2, a)
        return (v, move)

    def min_value(self, board: chess.Board, depth: int) -> tuple:
        """Return the min value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
        Returns:
            tuple(int, chess.Move): the min value of the state and the move that leads to it
        """
        if self.is_terminal(board, depth):
            return (self.utility(board), None)
        v = float('inf')
        move = None       
        for a in self.action(board):
            (v2, _) = self.max_value(self.result(board, a), depth - 1)
            if v2 < v:
                (v, move) = (v2, a)
        return (v, move)