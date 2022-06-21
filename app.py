import traceback
from flask import Flask, render_template, request, jsonify, Response
from scripts.chess_game import ChessGame

app = Flask(__name__, template_folder='templates')

# game_board = chess.Board()
chessGame = ChessGame('Minimax', 3)

@app.route('/')
def main():
  return render_template('index.html')

# Display Board
@app.route("/board.svg/")
def board():
  return Response(chessGame.getBoardSVG(), mimetype='image/svg+xml')

# New Game
@app.route("/game/", methods=['POST'])
def newGame():
  chessGame.setBoard()
  return main()

# Human Move
@app.route("/move/")
def move():
  try:
    move = request.args.get('move', default="")
    board.push_uci(move)
  except:
    traceback.print_exc()

  return main()

if __name__ == 'main':
    app.run(debug=False) 