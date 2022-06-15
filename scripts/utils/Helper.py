
import chess


class Helper:
  
  '''
  @param board: 
  @return   
  '''
  def getBoardStateScore(board: chess.Board):
    if board.is_checkmate():
      return 99999

    if board.is_stalemate():
      return 0
    
    if board.is_insufficient_material():
      return 0

    
  def doBoardState(board: chess.Board, isPlayer: bool):
    if board.is_checkmate():
      pass
      
  
      
    
  
  