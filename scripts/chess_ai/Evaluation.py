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
  while i <= 63:
    try:
      x = bool(board.piece_at(i).color)
    except AttributeError as e:
      x = x

    evaluation = evaluation + (getPieceValue(str(board.piece_at(i)))
                               if x else -getPieceValue(str(board.piece_at(i))))
    i += 1
  
  return evaluation
