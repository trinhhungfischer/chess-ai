import chess
from chess_ai.ChessAI import ai_mapping

ai_module = "Alphabeta"

def game():
    board = chess.Board()
    n = 0
    print(board)
    while n < 100:
      if n%2 == 1:
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
        move = ai_mapping[ai_module](3,board,True)
        move = chess.Move.from_uci(str(move))
        board.push(move)
      print(board.king(color=True))
      n += 1

if __name__ == "__main__":
  game()