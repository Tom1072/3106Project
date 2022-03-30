class SearchInterface():
    BOARD_DIMENSION = 8
    MAX_DEPTH = 4
    VALUE_MAP = {
        "p": 10,
        "n": 30,
        "b": 30,
        "r": 50,
        "q": 90,
        "k": 900
    }

    def next_move(self, board):
        pass