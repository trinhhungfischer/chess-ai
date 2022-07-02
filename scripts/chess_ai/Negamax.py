import chess

from scripts.chess_ai.Evaluation import evaluation


class Negamax:

  def __init__(self) -> None:
    pass

  def searchRoot(self, depth, board, isMaximizing: bool, isWhitePlayer: bool):
    possibleMoves = board.legal_moves

    bestMove = -99999
    bestMoveFinal = None
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      value = max(bestMove, self.negamax(depth - 1, board, not isMaximizing, isWhitePlayer))
      board.pop()
      if(value > bestMove):
        bestMove = value
        bestMoveFinal = move
      
    return bestMoveFinal

  def negamax(self, depth, board, isMaximizing: bool, isWhitePlayer: bool):

    possibleMoves = board.legal_moves

    if (depth == 0) | (len(list(possibleMoves)) == 0):
      return evaluation(board, isMaximizing, isWhitePlayer)

    bestMove = -99999
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      bestMove = max(bestMove, -self.negamax(depth - 1, board, not isMaximizing, isWhitePlayer))
      board.pop()
    return bestMove
