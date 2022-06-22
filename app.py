import traceback
from flask import Flask, render_template, request, jsonify, Response
from scripts.chess_game import ChessGame

app = Flask(__name__, template_folder='templates')

# game_board = chess.Board()
chessGame = ChessGame('Minimax', 3)

@app.route('/')
def index():
  return render_template('index.html')

# Display Board
@app.route("/board.svg/")
def board():
  return Response(chessGame.getBoardSVG(), mimetype='image/svg+xml')

# New Game
@app.route("/game/", methods=['POST'])
def newGame():
  chessGame.resetBoard()
  return index()

# Human Move
@app.route("/move/", methods=['GET', 'POST'])
def move():
  try:
    move = request.args.get('move', default="")
    gameState = chessGame.humanMove(move)
    print(gameState)
    # if gameState == 3 & gameState == 4:
    if gameState == 3:
      render_template('index.html')
    return index()
  except:
    traceback.print_exc()

# Bot Move
@app.route("/dev/", methods=['GET', 'POST'])
def dev():
  try:
    gameState = chessGame.botMove()
    # if gameState == 3 & gameState == 4:
    if gameState == 3:
      render_template('index.html')  
    return index()
  except:
    traceback.print_exc()
    
# Undo move
@app.route("/undo/", methods=['POST'])
def undo():
  chessGame.undoMove()
  return index()


if __name__ == '__main__':
    app.run(debug=False) 