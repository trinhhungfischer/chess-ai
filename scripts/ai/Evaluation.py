def getPieceValue(piece):
  if(piece == None):
      return 0
  chess_pieces = ['P', 'N', 'B', 'R', 'Q', 'K']
  values = [10, 30, 30, 50, 90, 900]

  return values[chess_pieces.index(piece.upper())]

  #value = value if (board.piece_at(place)).color else -value
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
        evaluation = evaluation + (getPieceValue(str(board.piece_at(i))) if x else -getPieceValue(str(board.piece_at(i))))
    return evaluation