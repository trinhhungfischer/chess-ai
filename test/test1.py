import chess
import chess.pgn as pgn

board = chess.Board()
print('Luot di nay la: ', board.turn)
print(board.uci)
board.push_uci('e2e4')
print('Luot di nay la: ', board.turn)
print(board.uci)
board.push_uci('d7d5')
board.push_uci('e4d5')

print(board.pieces(chess.PAWN, chess.BLACK))
board.pop()
print(len(board.pieces(chess.PAWN, chess.BLACK)))


