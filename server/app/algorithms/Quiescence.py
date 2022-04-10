import chess
import chess.engine
import random
import chess.svg
from app.algorithms.SearchInterface import SearchInterface


class QuiescenceSearch(SearchInterface):
    def __init__(self):
        self.init_alpha = -100000
        self.init_beta = 100000
        self.max_depth = 10

    def next_move(self, board: chess.Board) -> chess.Move:
        """Return the best move from the state "initial_state"
        Args:
            initial_state (chess.Board): _description_
        Returns:
            chess.Move: the best move
        """
        best_move_score = -100000
        best_move = None
        is_max_player = bool(random.getrandbits(1))

        for legal_move in board.legal_moves:
            move = chess.Move.from_uci(str(legal_move))
            board.push(move)
            move_score, nodes_per_depth = self.quiescence_search(board, self.max_depth, is_max_player, self.init_alpha, self.init_beta, {})
            score = max(best_move_score, move_score)
            board.pop()

            if score > best_move_score:
                best_move_score = score
                best_move = move

        # return (best_move, nodes_per_depth)
        print("Quiescence AI Playing...")
        return best_move

    def get_piece_val(self, board: chess.Board, pos: tuple[int, int]):
        piece_type = board.piece_type_at(self._convert_to_square(*pos))
        return 0 if not piece_type else self.VALUE_MAP[chess.PIECE_SYMBOLS[piece_type]]

    def static_eval(self, board: chess.Board):
        evaluation = 0
        x = True

        try:
            x = bool(board.piece_at(i).color)
        except Exception as e:
            x = x

        for i in range(0, 8):
            for j in range(0, 8):
                evaluation += self.get_piece_val(board, (i, j)) * (1 if x else -1)

        return evaluation

    def is_favorable_move(self, board: chess.Board, move: chess.Move) -> bool:
        if move.promotion is not None:
            return True
        
        # print(move)
        # print(move.from_square)
        # print(move.to_square)

        if board.is_capture(move) and not board.is_en_passant(move):
            org_piece_symbol = chess.PIECE_SYMBOLS[board.piece_type_at(move.from_square)]
            dest_piece_symbol = chess.PIECE_SYMBOLS[board.piece_type_at(move.to_square)]
            current_player_attackers = board.attackers(board.turn, move.to_square)
            next_player_attackers = board.attackers(not board.turn, move.to_square)

            if self.VALUE_MAP[org_piece_symbol] < self.VALUE_MAP[dest_piece_symbol] or \
               len(current_player_attackers) > len(next_player_attackers):
                return True
        
        return False

    def quiescence_search(self, board: chess.Board, current_depth: int, is_max_player: bool, alpha: int, beta: int, nodes_per_depth: int) -> tuple[int, int]:
        # This if else code block is only used for analysis of algorithm, by counting number of nodes explored
        if self.max_depth - current_depth in nodes_per_depth:
            nodes_per_depth[self.max_depth - current_depth] += 1
        else:
            nodes_per_depth[self.max_depth - current_depth] = 1

        if current_depth == 0:
            leaf_node_score = self.static_eval(board)
            return (leaf_node_score, nodes_per_depth)

        if self.max_depth - current_depth > 3:
            all_possible_capture_moves = [move for move in board.legal_moves if self.is_favorable_move(board, move)]
        else:
            all_possible_capture_moves = board.legal_moves

        best_score = -100000 if is_max_player else 100000

        for legal_move in all_possible_capture_moves:
            move = chess.Move.from_uci(str(legal_move))

            # pushing the current move to the board
            board.push(move)

            # calculating node score, if the current node will be the leaf node, then score will be calculated by static evaluation;
            # score will be calculated by finding max value between node score and current best score.
            node_score, nodes_per_depth = self.quiescence_search(board, current_depth - 1, not is_max_player, alpha, beta, nodes_per_depth)

            # calculating best score by finding max value between current best score and node score

            # calculating alpha for current MAX node
            if is_max_player:
                best_score = max(best_score, node_score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, node_score)
                beta = min(beta, best_score)

            # undoing the last move, so as to explore new moves while backtracking
            board.pop()

            # beta cut off
            if beta <= alpha:
                return (best_score, nodes_per_depth)

        return (best_score, nodes_per_depth)
