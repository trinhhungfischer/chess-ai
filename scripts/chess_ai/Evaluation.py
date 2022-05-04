# def getPieceValue(piece):
#   if(piece == None):
#       return 0
#   values = [10, 30, 30, 50, 90, 900]

#   return values[chess_pieces.index(piece.upper())]

from pickle import NONE


def getPieceValue(piece):
  if(piece is None):
    return 0
  value = 0

  chess_pieces = {'P': 10, 'N': 30, 'B' :30, 
                  'R': 50, 'Q': 90, 'K': 900}
  if (piece != 'None'):
    value = chess_pieces[piece.upper()]

  return value


def evaluation(board):
  i = 0
  evaluation = 0
  x = True
  try:
    x = bool(board.piece_at(i).color)
  except AttributeError as e:
    x = x
  while i < 63:
    i += 1
    evaluation = evaluation + (getPieceValue(str(board.piece_at(i)))
                               if x else -getPieceValue(str(board.piece_at(i))))
  return evaluation
