import chess
from chess_ai.ChessAI import ai_mapping

ai_module = "Minimax"

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
      print(board.legal_moves)
      move = input("Enter move: ")
      move = chess.Move.from_uci(str(move))
      board.push(move)
      if (len(list(board.legal_moves)) == 0):
        if (board.is_checkmate() == True):
          print("You win!!")
        else:
          print("Stale Mate")
        break

    else:
      print("Computers Turn:")
      move = ai_mapping[ai_module](3, board, True)
      move = chess.Move.from_uci(str(move))
      board.push(move)
    print_board(board = board, isWhite = isWhite)
    n += 1

if __name__ == "__main__":
  game()
