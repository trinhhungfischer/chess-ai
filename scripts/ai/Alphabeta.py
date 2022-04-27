import chess
# import sunfish
import sys
from Evaluation import evaluation


def minimaxRoot(depth, board,isMaximizing):
    possibleMoves = board.legal_moves
    bestMove = -9999
    bestMoveFinal = None
    for x in possibleMoves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(bestMove, minimax(depth - 1, board,-10000,10000, not isMaximizing))
        board.pop()
        if( value > bestMove):
            print("Best score: " ,str(bestMove))
            print("Best move: ",str(bestMoveFinal))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal

def minimax(depth, board, alpha, beta, is_maximizing):
    if(depth == 0):
        return -evaluation(board)
    possibleMoves = board.legal_moves
    if(is_maximizing):
        bestMove = -9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = max(bestMove,minimax(depth - 1, board,alpha,beta, not is_maximizing))
            board.pop()
            alpha = max(alpha,bestMove)
            if beta <= alpha:
                return bestMove
        return bestMove
    else:
        bestMove = 9999
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not is_maximizing))
            board.pop()
            beta = min(beta,bestMove)
            if(beta <= alpha):
                return bestMove
        return bestMove


def calculateMove(board):
    possible_moves = board.legal_moves
    if(len(possible_moves) == 0):
        print("No more possible moves...Game Over")
        sys.exit()
    bestMove = None
    bestValue = -9999
    n = 0
    for x in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        boardValue = -evaluation(board)
        board.pop()
        if(boardValue > bestValue):
            bestValue = boardValue
            bestMove = move

    return bestMove

def main():
    board = chess.Board("8/8/8/8/8/1K6/3Q4/k7 w - - 0 1")
    n = 0
    print(board)
    while n < 100:
        if n%2 == 0:
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
            move = minimaxRoot(3,board,True)
            print("Nuoc di la", move)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1


if __name__ == "__main__":
    main()