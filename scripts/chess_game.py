import chess
from scripts.chess_ai.ChessAI import ai_mapping


class ChessGame:
  def __init__(self, aiModule, depthSearch, board = None) -> None:
    self.aiModule = aiModule
    self.depthSearch = depthSearch
    if board == None:
      self.board = chess.Board()

  
  def printBoard(self, isPalyerWhite : bool):
    # if isPalyerWhite:
      print(self.board)
    # else:
    #   print(board.transform(chess.flip_vertical))

  def runGame(self):
    # board = chess.Board('8/8/6Q1/8/8/1K6/8/k7 w - - 0 1')
    n = 0

    side = input('Choose side: White (W), Black (B): ')
    if side == 'W':
      isPalyerWhite = True
    else: isPalyerWhite = False

    self.printBoard(isPalyerWhite = isPalyerWhite)

    while True:
      if n%2 != isPalyerWhite:
        possibleMoves = self.board.legal_moves
        
        if (len(list(possibleMoves)) != 0):
          move = input("Enter move: ")
          move = chess.Move.from_uci(str(move))
          self.board.push(move)
        else:
          # TODO: 
          if self.board.is_checkmate():        
            print('You lose')
          elif self.board.is_stalemate():
            print('You Draw Phew')
          break
      else:
        print("Computers Turn:")
        move = ai_mapping[self.aiModule](self.depthSearch, self.board, True, not isPalyerWhite)
        if move != None:
          print('Last move :', move)
          move = chess.Move.from_uci(str(move))
          self.board.push(move)
        else:
          break

      self.printBoard(isPalyerWhite = isPalyerWhite)
      n += 1
  


# ai_module = "Minimax"
# search_depth = 3


# def print_board(board: chess.Board, isPalyerWhite : bool):
#   # if isPalyerWhite:
#     print(board)
#   # else:
#   #   print(board.transform(chess.flip_vertical))

# def game():
#   # board = chess.Board('8/8/6Q1/8/8/1K6/8/k7 w - - 0 1')
#   board = chess.Board()
#   n = 0

#   side = input('Choose side: White (W), Black (B): ')
#   if side == 'W':
#     isPalyerWhite = True
#   else: isPalyerWhite = False

#   print_board(board = board, isPalyerWhite = isPalyerWhite)

#   while True:
#     if n%2 != isPalyerWhite:
#       possibleMoves = board.legal_moves
      
#       if (len(list(possibleMoves)) != 0):
#         move = input("Enter move: ")
#         move = chess.Move.from_uci(str(move))
#         board.push(move)
#       else:
#         # TODO: 
#         if board.is_checkmate():        
#           print('You lose')
#         elif board.is_stalemate():
#           print('You Draw Phew')
#         break
#     else:
#       print("Computers Turn:")
#       move = ai_mapping[ai_module](search_depth, board, True, not isPalyerWhite)
#       if move != None:
#         print('Last move :', move)
#         move = chess.Move.from_uci(str(move))
#         board.push(move)
#       else:
#         break

#     print_board(board = board, isPalyerWhite = isPalyerWhite)
#     n += 1