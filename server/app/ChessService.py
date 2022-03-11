import chess

BOARD_DIMENSION = 8


class ChessService:
    def __init__(self):
        self.board = chess.Board()

    def get_possible_moves(self, row: int, col: int) -> list:
        possible_moves = []
        for move in list(self.board.legal_moves):
            if move.from_square == self._convert_to_square(row, col):
                (dest_row, dest_col) = self._convert_to_row_col(move.to_square)
                possible_moves.append({"row": dest_row, "col": dest_col})
        return possible_moves

    def move(self, org_row: int, org_col: int, dest_row: int, dest_col: int) -> bool:
        new_move = chess.Move(self._convert_to_square(org_row, org_col), self._convert_to_square(dest_row, dest_col))
        if new_move in self.board.legal_moves:
            self.board.push(new_move)
            print(self.board)
            return True
        else:
            return False

    def get_board(self) -> list:
        pass

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

    def reset(self):
        self.board.reset()
