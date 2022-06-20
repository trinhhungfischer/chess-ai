import chess
from scripts.chess_ai.ChessAI import ai_mapping

ai_module = "Minimax"
search_depth = 1


def print_board(board: chess.Board, isPalyerWhite : bool):
  # if isPalyerWhite:
    print(board)
  # else:
  #   print(board.transform(chess.flip_vertical))

def game():
  board = chess.Board('8/8/6Q1/8/8/1K6/8/k7 w - - 0 1')
  # board = chess.Board()
  n = 0

  side = input('Choose side: White (W), Black (B): ')
  if side == 'W':
    isPalyerWhite = True
  else: isPalyerWhite = False

  print_board(board = board, isPalyerWhite = isPalyerWhite)

  while True:
    if n%2 != isPalyerWhite:
      move = input("Enter move: ")
      move = chess.Move.from_uci(str(move))
      board.push(move)
    else:
      print("Computers Turn:")
      move = ai_mapping[ai_module](search_depth, board, True, not isPalyerWhite)
      print('Last move :', move)
      move = chess.Move.from_uci(str(move))
      board.push(move)

    print_board(board = board, isPalyerWhite = isPalyerWhite)
    n += 1