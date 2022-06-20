import chess


blackPawnPScore = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,

                   5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,

                   1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,

                   0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,

                   0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,

                   0.5, 0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,

                   0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,

                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

blackKnightPScore = [-5.0, -4.0, -3.0, 3.0, 3.0, 3.0, -4.0, -5.0,

                     -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,

                     -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,

                     -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,

                     -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,

                     -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,

                     -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,

                     -5.0, -4.0, 3.0, 3.0, 3.0, 3.0, -4.0, -5.0]

blackBishopPScore = [-2.0, -1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -2.0,

                     -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,

                     -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, 1.0,

                     -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, 1.0,

                     -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0,

                     -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,

                     -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0,

                     -2.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -2.0]

blackRookPScore = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,

                   0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,

                   -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,

                   -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,

                   -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,

                   -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,

                   -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,

                   0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]

blackQueenPScore = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,

                    -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,

                    -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 1.0,

                    -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,

                    0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,

                    -1.0, 0.3, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,

                    -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0,

                    -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

blackKingPScore = [-3.0, -4.0, -4.0, -5.0, -5.0, 4.0, -4.0, -3.0,

                   -3.0, 4.0, 4.0, -5.0, -5.0, -4.0, -4.0, -3.0,

                   -3.0, -4.0, -4.0, -5.0, -5.0, 4.0, -4.0, -3.0,

                   -3.0, -4.0, 4.0, -5.0, -5.0, -4.0, -4.0, -3.0,

                   -2.0, 3.0, 3.0, -4.0, 4.0, -3.0, -3.0, -2.0,

                   -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, 1.0,

                   2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,

                   2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2]

whitePawnPScore = blackPawnPScore[::-1]
whiteKnightPScore = blackKnightPScore[::-1]
whiteBishopPScore = blackBishopPScore[::-1]
whiteRookPScore = blackRookPScore[::-1]
whiteQueenPScore = blackQueenPScore[::-1]
whiteKingPScore = blackKingPScore[::-1]

positionValueMaping = {'p': blackPawnPScore, 'n': blackKnightPScore, 'b': blackBishopPScore,
                       'r': blackRookPScore, 'q': blackQueenPScore, 'k': blackKingPScore,
                       'P': whitePawnPScore, 'N': whiteKnightPScore, 'B': whiteBishopPScore,
                       'R': whiteRookPScore, 'Q': whiteQueenPScore, 'K': whiteKingPScore}


def getPieceValue(piece, position):
  if(piece is None):
    return 0
  value = 0

  chess_pieces = {'P': 10, 'N': 30, 'B': 30,
                  'R': 50, 'Q': 90, 'K': 900}
  if (piece != 'None'):
    value = chess_pieces[piece.upper()] + positionValueMaping[piece][position]

  return value


def evaluation(board: chess.Board, isMaximizing: bool, isWhitePlayer: bool):
  i = 0
  evaluation = 0
  x = True

  # print('Luot di cua ', ('trang' if board.turn else 'den'))

  # print('Board is checkmate ', board.is_checkmate())
  
  if board.is_checkmate():
    return 99999 * (-1 if board.turn == isWhitePlayer else 1)


  if board.is_stalemate():
    return 0

  if board.is_insufficient_material():
    return 0

  while i <= 63:
    try:
      x = bool(board.piece_at(i).color)

      evaluation = evaluation + (getPieceValue(str(board.piece_at(i)), i)
                                 if x else -getPieceValue(str(board.piece_at(i)), i))      
    except AttributeError as e:
      pass
    
    i += 1

  return evaluation * (1 if isWhitePlayer else -1)
