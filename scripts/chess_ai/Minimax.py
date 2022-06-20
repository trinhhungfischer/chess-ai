import chess
from scripts.chess_ai.Evaluation import evaluation
from scripts.utils.Helper import Helper


class Minimax:

  def __init__(self) -> None:
    pass

    
  def minimaxRoot(self, depth, board: chess.Board, isMaximizing: bool, isWhitePlayer: bool):
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
      
      print('-----------------------------------------------------')
      print('Nuoc di dau tien ', move)
      value = max(bestMoveValue, self.minimax(depth - 1, board, not isMaximizing, isWhitePlayer))

      board.pop()
      if(value > bestMoveValue):
        bestMoveValue = value
        bestMoveFinal = move

    return bestMoveFinal

  def minimax(self, depth, board, isMaximizing: bool, isWhitePlayer: bool):

    possibleMoves = board.legal_moves

    if (depth == 0) | (len(list(possibleMoves)) == 0):
      return evaluation(board, isMaximizing, isWhitePlayer)

    if(isMaximizing):
      bestMove = -99999
      for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        bestMove = max(bestMove, self.minimax(depth - 1, board, not isMaximizing, isWhitePlayer))
        print(x, '  ', depth, '  ', bestMove)
        board.pop()
      
      return bestMove
    else:
      bestMove = 99999
      for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        bestMove = min(bestMove, self.minimax(depth - 1, board, not isMaximizing, isWhitePlayer))
        print(x, '  ', depth, '  ', bestMove)
        board.pop()
    
      return bestMove
    