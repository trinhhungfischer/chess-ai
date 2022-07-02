from scripts.chess_ai.Alphabeta import Alphabeta
from scripts.chess_ai.Minimax import Minimax
from scripts.chess_ai.Negamax import Negamax
from scripts.chess_ai.NegamaxAB import NegamaxAB


ai_mapping = {
  "Alphabeta": Alphabeta().searchRoot,
  "Minimax": Minimax().searchRoot,
  "Negamax": Negamax().searchRoot,
  "NegamaxAB": NegamaxAB().searchRoot,
  
}
