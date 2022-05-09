from chess_ai.Alphabeta import Alphabeta
from chess_ai.Minimax import Minimax

ai_mapping = {
  "Alphabeta": Alphabeta().minimaxRoot,
  "Minimax": Minimax().minimaxRoot}
