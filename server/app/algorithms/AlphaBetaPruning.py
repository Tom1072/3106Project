from app.algorithms.SearchInterface import SearchInterface

class AlphaBetaPruning(SearchInterface):
    def next_move(self, board, chess_service):
        print("Alpha-Beta Pruning Moved")
        pass

    def minimaxRoot(depth, board,isMaximizing):
        possibleMoves = []
        for move in list(self.board.legal_moves):
            (org_row, org_col) = self._convert_to_row_col(move.from_square)
            (dest_row, dest_col) = self._convert_to_row_col(move.to_square)
            possibleMoves.append({"org_row": org_row, "org_col": org_col, "dest_row": dest_row, "dest_col": dest_col})
        
        bestMove = -9999
        bestMoveFinal = None
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            value = max(bestMove, minimax(depth - 1, board,-10000,10000, not isMaximizing))
            board.pop()
            if( value > bestMove):
                print("Best score: " ,str(bestMove))
                print("Best move: ",str(bestMoveFinal))
                bestMove = value
                bestMoveFinal = move
        return bestMoveFinal

    def minimax(depth, board, alpha, beta, is_maximizing):
        if(depth == 0):
            return -evaluation(board)
        possibleMoves = board.legal_moves
        if(is_maximizing):
            bestMove = -9999
            for x in possibleMoves:
                move = chess.Move.from_uci(str(x))
                board.push(move)
                bestMove = max(bestMove,minimax(depth - 1, board,alpha,beta, not is_maximizing))
                board.pop()
                alpha = max(alpha,bestMove)
                if beta <= alpha:
                    return bestMove
            return bestMove
        else:
            bestMove = 9999
            for x in possibleMoves:
                move = chess.Move.from_uci(str(x))
                board.push(move)
                bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not is_maximizing))
                board.pop()
                beta = min(beta,bestMove)
                if(beta <= alpha):
                    return bestMove
        return bestMove

    def evaluation(board):
        i = 0
        evaluation = 0
        x = True
        try:
            x = bool(board.piece_at(i).color)
        except AttributeError as e:
            x = x
        while i < 63:
            i += 1
            evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
        return evaluation


    def getPieceValue(piece):
        if(piece == None):
            return 0
        value = 0
        if piece == "P" or piece == "p":
            value = 10
        if piece == "N" or piece == "n":
            value = 30
        if piece == "B" or piece == "b":
            value = 30
        if piece == "R" or piece == "r":
            value = 50
        if piece == "Q" or piece == "q":
            value = 90
        if piece == 'K' or piece == 'k':
            value = 900
        #value = value if (board.piece_at(place)).color else -value
        return value