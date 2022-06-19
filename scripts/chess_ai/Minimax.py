import chess
from scripts.chess_ai.Evaluation import evaluation
from scripts.utils.Helper import Helper


class Minimax:

  def __init__(self) -> None:
    pass

    
  def minimaxRoot(self, depth, board: chess.Board, isMaximizing):
    possibleMoves = board.legal_moves
    
    bestMoveValue = -99999

    bestMoveFinal = None

    if (len(list(possibleMoves)) == 0):
      if (board.is_checkmate()):
        print("You win")
      elif (board.is_stalemate()):
        print("Draw")
      return


    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      value = max(bestMoveValue, self.minimax(depth - 1, board, not isMaximizing))
      board.pop()
      if(value > bestMoveValue):
        bestMoveValue = value
        bestMoveFinal = move

    return bestMoveFinal

  def minimax(self, depth, board, is_maximizing):

    possibleMoves = board.legal_moves

    if (depth == 0) | (len(list(possibleMoves)) == 0):
      return evaluation(board, is_maximizing) * (1 if is_maximizing else -1)

    if(is_maximizing):
      bestMove = -99999
      for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        bestMove = max(bestMove, self.minimax(depth - 1, board, not is_maximizing))
        board.pop()
      return bestMove
    else:
      bestMove = 99999
      for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        bestMove = min(bestMove, self.minimax(depth - 1, board, not is_maximizing))
        board.pop()
      return bestMove
    