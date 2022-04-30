# chess-ai
A Chess AI bot for AI Introduction Project

# Usage
## Analysis
First, you must unzip chess.zip to get data.

Second you should create a python virtual enviroment and activate it. If this package is not installed, please download Python and [this package](https://pypi.org/project/virtualenv/).
```
virtualenv .venv
source .venv/bin/activate
```
After enviroment activation, you must install requirement by this command.
```
.venv/bin/pip install -r requirement.txt
```
Now you can run the scripts in the analysis folder with this virtual environment.


## About AI Modules
The AI module is written in [./script/chess_ai](./scripts/chess_ai/) with the algorithm mapping file is [ChessAI](./scripts/chess_ai/ChessAI.py). You can use it to call AI algorithms from this file.
Now, there are 2 algorithms in this moudule:
1. Minimax 
2. Minimax with Alpha Beta Pruning