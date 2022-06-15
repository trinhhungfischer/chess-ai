import chess

from scripts.chess_ai.Evaluation import evaluation


class Negamax:

  def __init__(self) -> None:
    pass

  def minimaxRoot(self, depth, board, isMaximizing):
    possibleMoves = board.legal_moves

    bestMove = -99999
    bestMoveFinal = None
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      value = max(bestMove, self.minimax(depth - 1, board, not isMaximizing))
      board.pop()
      if(value > bestMove):
        print("Best score: ", str(bestMove))
        print("Best move: ", str(bestMoveFinal))
        bestMove = value
        bestMoveFinal = move
    return bestMoveFinal

  def minimax(self, depth, board, is_maximizing):
    if(depth == 0):
      return -evaluation(board, is_maximizing)

    possibleMoves = board.legal_moves


    bestMove = -99999
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      bestMove = max(bestMove, -self.minimax(depth - 1, board, not is_maximizing))
      board.pop()
    return bestMove
