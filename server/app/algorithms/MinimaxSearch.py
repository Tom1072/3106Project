import chess
from app.algorithms.SearchInterface import SearchInterface

class MinimaxSearch(SearchInterface):
    # def next_move(self, board, chess_service):
    #     print("Alpha-Beta Moved")
    #     pass

    def get_move(self, initial_state: chess.Board) -> chess.Move:
        """Return the best move from the state "initial_state"
        Args:
            initial_state (chess.Board): _description_
        Returns:
            chess.Move: the best move
        """
        return self.minimax(initial_state, self.MAX_DEPTH)

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

    def utility(self, board: chess.Board, player: chess.COLORS) -> int:
        """Return the utility/objective/heuristic value of the state "board" for the
        player "player" when the game is over

        Args:
            board (chess.Board): the current state of the game
            player (chess.COLORS): the player who holds the turn in the terminal state
        
        Returns:
            int: the utility/objective value of the state
            (positive for a win, negative for a loss, 0 for a draw)
        """
        total_value = 0
        for i in range(0, 8):
            for j in range(0, 8):
                square = board.piece_at(self._convert_to_square(i, j))
                if (square != None and square.color == player):
                    # Get the piece type
                    piece_type = square.piece_type
                    # Get the piece value
                    piece_value = self.VALUE_MAP[chess.PIECE_SYMBOLS[piece_type]]
                    # Add the piece value to the total value
                    total_value += piece_value
                elif (square != None and square.color != player):
                    # Get the piece type
                    piece_type = square.piece_type
                    # Get the piece value
                    piece_value = self.VALUE_MAP[chess.PIECE_SYMBOLS[piece_type]]
                    # Subtract the piece value from the total value
                    total_value -= piece_value
        return total_value

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
            return (self.utility(board, self.to_move(board)), None)
        v = -float('inf')
        move = None
        for a in self.action(board):
            (v2, a2) = self.min_value(self.result(board, a), depth - 1)
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
            return (self.utility(board, self.to_move(board)), None)
        v = float('inf')
        move = None       
        for a in self.action(board):
            (v2, a2) = self.max_value(self.result(board, a), depth - 1)
            if v2 < v:
                (v, move) = (v2, a)
        return (v, move)

    def _convert_to_square(self, row: int, col: int) -> chess.Square:
        return chess.SQUARES[row * self.BOARD_DIMENSION + col]