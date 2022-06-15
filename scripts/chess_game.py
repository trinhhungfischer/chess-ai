import chess
from scripts.chess_ai.ChessAI import ai_mapping

ai_module = "NegamaxAB"

def print_board(board: chess.Board, isWhite : bool):
  if isWhite:
    print(board)
  else:
    print(board.transform(chess.flip_vertical))

def game():
  board = chess.Board()
  n = 0

  side = input('Choose side: White (W), Black (B): ')
  if side == 'W':
    isWhite = True
  else: isWhite = False

  print_board(board = board, isWhite = isWhite)

  while n < 100:
    if n%2 != isWhite:
      print('Board turn is ', board.turn)
      move = input("Enter move: ")
      move = chess.Move.from_uci(str(move))
      board.push(move)
    else:
      print('Board turn is ', board.turn)
      print("Computers Turn:")
      move = ai_mapping[ai_module](5, board, True)
      print('Last move :', move)
      move = chess.Move.from_uci(str(move))
      board.push(move)

    print_board(board = board, isWhite = isWhite)
    n += 1