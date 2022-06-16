from scripts.chess_ai.Alphabeta import Alphabeta
from scripts.chess_ai.Minimax import Minimax
from scripts.chess_ai.Negamax import Negamax
from scripts.chess_ai.NegamaxAB import NegamaxAB


ai_mapping = {
  "Alphabeta": Alphabeta().minimaxRoot,
  "Minimax": Minimax().minimaxRoot,
  "Negamax": Negamax().minimaxRoot,
  "NegamaxAB": NegamaxAB().minimaxRoot,
  
}
