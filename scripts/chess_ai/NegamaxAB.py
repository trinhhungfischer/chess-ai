import sys

import chess

from scripts.chess_ai.Evaluation import evaluation

class NegamaxAB:

  def __init__(self) -> None:
    pass

  def searchRoot(self, depth, board, isMaximizing: bool, isWhitePlayer: bool, debug = False):
    possibleMoves = board.legal_moves
    bestMove = -99999
    bestMoveFinal = None
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)

      value = max(
        bestMove, -self.negamaxAB(
          depth - 1, board, -10000, 10000, not isMaximizing, isWhitePlayer))
        
      board.pop()
      if(value > bestMove):
        bestMove = value
        bestMoveFinal = move
    return bestMoveFinal

  def negamaxAB(self, depth, board, alpha, beta, isMaximizing: bool, isWhitePlayer: bool, debug = False):
  
    possibleMoves = board.legal_moves
    
    if (depth == 0) | (len(list(possibleMoves)) == 0):
      return -evaluation(board, isMaximizing, isWhitePlayer)
    
    # Fail-soft alpha-beta pruning
    
    bestMove = -99999
    for x in possibleMoves:
      move = chess.Move.from_uci(str(x))
      board.push(move)
      bestMove = max(bestMove, -self.negamaxAB(depth - 1, board, -beta, -alpha, not isMaximizing, not isWhitePlayer)) 
      board.pop()
      
      alpha = max(alpha, bestMove)
      
      if (beta <= alpha):
        return bestMove
    
    return bestMove
