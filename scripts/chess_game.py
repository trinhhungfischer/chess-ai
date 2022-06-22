import chess
import chess.svg
from scripts.chess_ai.ChessAI import ai_mapping


class ChessGame:
  def __init__(self, aiModule, depthSearch, board = None, isWhitePlayer = True) -> None:
    self.__aiModule = aiModule
    self.__depthSearch = depthSearch
    if board == None:
      self.__board = chess.Board()
    
    self.__isPlayerWhite = isWhitePlayer
    
    self.__turn = 1

  def getBoard(self):
    return self.__board
  
  def setBoard(self, fen = None):
    if fen == None:
      self.__board = chess.Board()
      return  
    self.__board = chess.Board(fen)
    
  def resetBoard(self):
    self.__board = chess.Board()
    
  def getBoardSVG(self):
    return chess.svg.board(board = self.__board, size=700)
  
  def printBoard(self):
    if self.__isPlayerWhite:
      print(self.__board)
    else:
      print(self.board.transform(chess.flip_vertical))

  def runGame(self):

    self.printBoard()

    while True:
      if self.__turn % 2 != self.__isPlayerWhite:
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
        move = ai_mapping[self.__aiModule](self.__depthSearch, self.__board, True, not self.__isPlayerWhite)
        if move != None:
          print('Last move :', move)
          move = chess.Move.from_uci(str(move))
          self.__board.push(move)
        else:
          if self.__board.is_checkmate():        
            print('You win')
          elif self.__board.is_stalemate():
            print('You Draw Stale Mate')
          break
      
      if (self.__board.is_insufficient_material()):
        print("Draw because insufficient material")      

      self.__turn += 1
  
  '''
  @dev 
  @param
  @return Game Board State with 0 is Checkmate, 1 is Stalemate, 2 is Draw, 3 is Move, 4 is Invalid move  
  '''
  def humanMove(self, move: str):
    if self.__board.is_insufficient_material():
      return 2

    if self.__turn % 2 == self.__isPlayerWhite:
      possibleMoves = self.__board.legal_moves
      
      if move not in list(map(str, possibleMoves)):
        return 4
      
      if (len(list(possibleMoves)) != 0):
        move = chess.Move.from_uci(str(move))
        self.__board.push(move)
        self.__turn += 1
        return 3
      else:
        # TODO: 
        if self.__board.is_checkmate():        
          return 0
        elif self.__board.is_stalemate():
          return 1
    else:
      return 4
  
  '''
  @dev 
  @param
  @return Game Board State with 0 is Checkmate, 1 is Stalemate, 2 is Draw, 3 is Move  
  '''
  def botMove(self):
    if self.__turn % 2 != self.__isPlayerWhite:
      possibleMoves = self.__board.legal_moves
      
      if (len(list(possibleMoves)) != 0):
        move = ai_mapping[self.__aiModule](self.__depthSearch, self.__board, True, not self.__isPlayerWhite)
        move = chess.Move.from_uci(str(move))
        self.__board.push(move)
        self.__turn += 1
        return 3
      else:
        if self.__board.is_checkmate():        
          return 0
        elif self.__board.is_stalemate():
          return 1

  def isPlayerTurn(self):
    return self.__turn % 2 == self.__isPlayerWhite
  
  def undoMove(self):
    print(self.__turn)
    if (self.__turn > 2) & (self.isPlayerTurn()):
      self.__board.pop()
      self.__board.pop()
      self.__turn -= 2
    elif (self.__turn > 1):
      self.__board.pop()
      self.__turn -= 1