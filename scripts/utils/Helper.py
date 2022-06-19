
import chess
from numpy import char


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
      
    
  
  def getCellIdFromPos(cellName: str, row = None) -> int:
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = list(range(1, 9))

    if row == None:
      column = cellName[0]
      row = int(cellName[1])
    else:
      column = cellName

    
    try:
      cellId = columns.index(column.lower()) + rows.index(row) * 8
      return cellId
    except:
      print('Invalid columns and rows')
  
if __name__ == '__main__':

  print(Helper.getCellIdFromPos('a1'))
  
  
    
  
      
    
  
  