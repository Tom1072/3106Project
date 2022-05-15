import chess
from app.services.AlgorithmService import AlgorithmService

BOARD_DIMENSION = 8


class ChessService:
    def __init__(self):
        self.board = chess.Board()

    def get_possible_moves(self, row: int, col: int) -> list:
        """Return a list of possible move form a possition

        Args:
            row (int)
            col (int)

        Returns:
            list: list of possible moves [{"row": 2, "col": 1}, {"row": 3, "col": 1}]
        """
        possible_moves = []
        for move in list(self.board.legal_moves):
            if move.from_square == self._convert_to_square(row, col):
                (dest_row, dest_col) = self._convert_to_row_col(move.to_square)
                possible_moves.append({"row": dest_row, "col": dest_col})
        return possible_moves

    def move(self, org_row: int, org_col: int, dest_row: int, dest_col: int) -> bool:
        """"
        Make a move from (org_row, org_col) to (dest_row, dest_col)

        Args:
            org_row (int): original row
            org_col (int): original col
            dest_row (int): destination row
            dest_col (int): destination col

        Returns:
            bool: true if the move is successful(legal), false otherwise
        """
        new_move = self.board.find_move(
            self._convert_to_square(org_row, org_col),
            self._convert_to_square(dest_row, dest_col))

        if new_move in self.board.legal_moves:
            self.board.push(new_move)
            return True
        else:
            return False

    def ai_move(self, algorithm_service: AlgorithmService) -> dict:
        """"
        Make an AI move 

        Args:
            algorithm_service (AlgorithmService): the service handle the AI algorithms

        Returns:
            dict: the dictionary contains 
        """
        new_move = self._parse_move(algorithm_service.get_next_move(self.board))
        org_row, org_col = new_move["org"]
        dest_row, dest_col = new_move["dest"]
        if self.move(org_row, org_col, dest_row, dest_col):
            return {
                "prev": { "row": org_row, "col": org_col },
                "next": { "row": dest_row, "col": dest_col }
            }


    def get_board(self) -> list:
        """Return the current board state

        Returns:
            list: current board state with the following format
            [
                ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
                ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"]
            ]
        """
        board_str = self.board.__str__()
        board_ls = [row.split(" ") for row in board_str.split("\n")]
        for row in range(BOARD_DIMENSION):
            for col in range(BOARD_DIMENSION):
                entry = board_ls[row][col]
                if (entry == "."):
                    board_ls[row][col] = ""
                elif (entry.isupper()):
                    board_ls[row][col] = "w" + entry.lower()
                elif (entry.islower()):
                    board_ls[row][col] = "b" + entry

        # reverse for the frontend
        board_ls.reverse()
        return board_ls

    def is_black_turn(self) -> bool:
        return True if self.board.turn == chess.BLACK else False

    def get_game_outcome(self) -> str:
        """Checks if the game is over due to checkmate, stalemate, insufficient material, the seventyfive-move
        rule, fivefold repetition, or a variant end condition. Returns the chess.Outcome if the game has ended,
        otherwise None.

        Returns:
            str: the outcome
        """
        outcome = self.board.outcome(claim_draw=False)
        if not outcome:
            return None
        return str(outcome.result())

    def reset(self):
        """Reset the board to the orginal state (with all piece back to its starting position)
        """
        self.board.reset()

    def _convert_to_square(self, row: int, col: int) -> chess.Square:
        return chess.SQUARES[row*BOARD_DIMENSION + col]

    def _convert_to_row_col(self, square: chess.Square) -> tuple:
        index = chess.SQUARES.index(square)
        col, row = index % BOARD_DIMENSION, index//BOARD_DIMENSION
        return (row, col)
    
    def _dict_list_to_tuple_list(dict_list: list):
        output = []
        for i in range(len(dict_list)):
            output.append(dict_list[i].items())

        output.sort()
        return output

    def _parse_move(self, move: chess.Move) -> dict:
        return {
            "org": self._convert_to_row_col(move.from_square),
            "dest": self._convert_to_row_col(move.to_square)
        }
