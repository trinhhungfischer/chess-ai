import chess
import chess.svg
from scripts.chess_ai.ChessAI import ai_mapping


class ChessGame:
  def __init__(self, aiModule, depthSearch, board = None, isWhitePlayer = True) -> None:
    self.aiModule = aiModule
    self.depthSearch = depthSearch
    if board == None:
      self.__board = chess.Board()
    
    self.isPlayerWhite = isWhitePlayer

  def getBoard(self):
    return self.__board
  
  def setBoard(self, fen = None):
    if fen == None:
      self.__board = chess.Board()
      return  
    self.__board = chess.Board(fen)

  def getBoardSVG(self):
    return chess.svg.board(board = self.__board, size=700)
  
  
  def printBoard(self):
    # if self.isPlayerWhite:
      print(self.__board)
    # else:
    #   print(board.transform(chess.flip_vertical))

  def runGame(self):
    # board = chess.Board('8/8/6Q1/8/8/1K6/8/k7 w - - 0 1')
    n = 0

    side = input('Choose side: White (W), Black (B): ')
    if side == 'W':
      self.isPlayerWhite = True
    else: self.isPlayerWhite = False

    self.printBoard()

    while True:
      if n%2 != self.isPlayerWhite:
        possibleMoves = self.__board.legal_moves
        
        if (len(list(possibleMoves)) != 0):
          move = input("Enter move: ")
          move = chess.Move.from_uci(str(move))
          self.__board.push(move)
        else:
          # TODO: 
          if self.__board.is_checkmate():        
            print('You lose')
          elif self.__board.is_stalemate():
            print('You Draw Phew')
          break
      else:
        print("Computers Turn:")
        move = ai_mapping[self.aiModule](self.depthSearch, self.__board, True, not self.isPlayerWhite)
        if move != None:
          print('Last move :', move)
          move = chess.Move.from_uci(str(move))
          self.__board.push(move)
        else:
          break

      self.printBoard()
      n += 1
