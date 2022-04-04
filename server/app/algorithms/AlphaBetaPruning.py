import chess
from app.algorithms.SearchInterface import SearchInterface


class AlphaBetaPruning(SearchInterface):
    def next_move(self, initial_state: chess.Board) -> chess.Move:
        """Return the best move from the state "initial_state"
        Args:
            initial_state (chess.Board): _description_
        Returns:
            chess.Move: the best move
        """
        print("Alpha-Beta Pruning AI Playing...")
        return self.alpha_beta_search(initial_state, self.MAX_DEPTH)

    def to_move(self, state: chess.Board) -> chess.COLORS:
        """The player whose turn it is to move in state "state"
        Args:
            state (chess.Board): the current state of the game
        Returns:
            chess.COLORS: the player whose turn it is to move
        """
        return state.turn

    def action(self, state: chess.Board) -> list:
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
                    total_value = piece_value
        return total_value

    def alpha_beta_search(self, board: chess.Board, depth: int) -> chess.Move:
        """Return the minimax value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
        Returns:
            chess.Move: the best move
        """
        (_, best_move) = self.max_value_alpha_beta(
            board, depth, -float('inf'), float('inf'))
        return best_move if best_move != None else chess.Move.null()

    def max_value_alpha_beta(self, board: chess.Board, depth: int, alpha: int, beta: int) -> tuple:
        """Return the max value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
            alpha (int): the alpha value
            beta (int): the beta value
        Returns:
            tuple(int, chess.Move): the max value of the state and the move that leads to it
        """
        if self.is_terminal(board, depth):
            return (self.utility(board, self.to_move(board)), None)
        v = -float('inf')
        move = None
        for a in self.action(board):
            (v2, _) = self.min_value_alpha_beta(
                self.result(board, a), depth - 1, alpha, beta)
            if v2 > v:
                (v, move) = (v2, a)
            if v2 > beta:
                return (v2, move)
            alpha = max(alpha, v2)
        return (v, move)

    def min_value_alpha_beta(self, board: chess.Board, depth: int, alpha: int, beta: int) -> tuple:
        """Return the min value of the state "board" with depth "depth"
        Args:
            board (chess.Board): the current state of the game
            depth (int): the depth of the search tree
            alpha (int): the alpha value
            beta (int): the beta value
        Returns:
            tuple(int, chess.Move): the min value of the state and the move that leads to it
        """
        if self.is_terminal(board, depth):
            return (self.utility(board, self.to_move(board)), None)
        v = float('inf')
        move = None
        for a in self.action(board):
            (v2, _) = self.max_value_alpha_beta(
                self.result(board, a), depth - 1, alpha, beta)
            if v2 < v:
                (v, move) = (v2, a)
            if v2 < alpha:
                return (v2, move)
            alpha = min(alpha, v2)
        return (v, move)

    def _convert_to_square(self, row: int, col: int) -> chess.Square:
        return chess.SQUARES[row * self.BOARD_DIMENSION + col]

    # def minimaxRoot(depth, board,isMaximizing):
    #     possibleMoves = []
    #     for move in list(self.board.legal_moves):
    #         (org_row, org_col) = self._convert_to_row_col(move.from_square)
    #         (dest_row, dest_col) = self._convert_to_row_col(move.to_square)
    #         possibleMoves.append({"org_row": org_row, "org_col": org_col, "dest_row": dest_row, "dest_col": dest_col})

    #     bestMove = -9999
    #     bestMoveFinal = None
    #     for x in possibleMoves:
    #         move = chess.Move.from_uci(str(x))
    #         board.push(move)
    #         value = max(bestMove, minimax(depth - 1, board,-10000,10000, not isMaximizing))
    #         board.pop()
    #         if( value > bestMove):
    #             print("Best score: " ,str(bestMove))
    #             print("Best move: ",str(bestMoveFinal))
    #             bestMove = value
    #             bestMoveFinal = move
    #     return bestMoveFinal

    # def minimax(depth, board, alpha, beta, is_maximizing):
    #     if(depth == 0):
    #         return -evaluation(board)
    #     possibleMoves = board.legal_moves
    #     if(is_maximizing):
    #         bestMove = -9999
    #         for x in possibleMoves:
    #             move = chess.Move.from_uci(str(x))
    #             board.push(move)
    #             bestMove = max(bestMove,minimax(depth - 1, board,alpha,beta, not is_maximizing))
    #             board.pop()
    #             alpha = max(alpha,bestMove)
    #             if beta <= alpha:
    #                 return bestMove
    #         return bestMove
    #     else:
    #         bestMove = 9999
    #         for x in possibleMoves:
    #             move = chess.Move.from_uci(str(x))
    #             board.push(move)
    #             bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not is_maximizing))
    #             board.pop()
    #             beta = min(beta,bestMove)
    #             if(beta <= alpha):
    #                 return bestMove
    #     return bestMove

    # def evaluation(board):
    #     i = 0
    #     evaluation = 0
    #     x = True
    #     try:
    #         x = bool(board.piece_at(i).color)
    #     except AttributeError as e:
    #         x = x
    #     while i < 63:
    #         i += 1
    #         evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    #     return evaluation

    # def getPieceValue(piece):
    #     if(piece == None):
    #         return 0
    #     value = 0
    #     if piece == "P" or piece == "p":
    #         value = 10
    #     if piece == "N" or piece == "n":
    #         value = 30
    #     if piece == "B" or piece == "b":
    #         value = 30
    #     if piece == "R" or piece == "r":
    #         value = 50
    #     if piece == "Q" or piece == "q":
    #         value = 90
    #     if piece == 'K' or piece == 'k':
    #         value = 900
    #     #value = value if (board.piece_at(place)).color else -value
    #     return value
