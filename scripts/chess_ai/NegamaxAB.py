import sys

import chess

from scripts.chess_ai.Evaluation import evaluation

class NegamaxAB:

  def __init__(self) -> None:
    pass

  def minimaxRoot(self, depth, board, isMaximizing):
    possibleMoves = board.legal_moves
    print(list(possibleMoves))
    bestMove = -99999
    bestMoveFinal = None
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)

      value = max(
        bestMove, self.alphabeta(
          depth - 1, board, -10000, 10000, not isMaximizing))
      board.pop()
      if(value > bestMove):
        print("Best score: ", str(bestMove))
        print("Best move: ", str(bestMoveFinal))
        bestMove = value
        bestMoveFinal = move
    return bestMoveFinal

  def alphabeta(self, depth, board, alpha, beta, is_maximizing):
    if(depth == 0):
      return -evaluation(board, is_maximizing)
    possibleMoves = board.legal_moves
    
    # Fail-soft alpha-beta pruning
    
    bestMove = -99999
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      bestMove = max(bestMove, self.alphabeta(depth - 1, board, -beta, -alpha, not is_maximizing)) 
      board.pop()
      
      alpha = max(alpha, bestMove)
      if (beta <= alpha):
        return bestMove
    
    return bestMove
    
  def calculateMove(board):
    possible_moves = board.legal_moves
    if(len(possible_moves) == 0):
      print("No more possible moves...Game Over")
      sys.exit()
    bestMove = None
    bestValue = -99999
    n = 0

    for x in possible_moves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      boardValue = -evaluation(board)
      board.pop()
      if(boardValue > bestValue):
        bestValue = boardValue
        bestMove = move

    return bestMove
