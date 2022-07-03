# chess-ai
A Chess AI bot for AI Introduction Project

# Install requirement and setup environment
You can use pip install directly but I recommend you should use a virtual environment to interact with pip and python. You can easily install requirements by command if you had python and pip.
```
pip install -r requirement.txt
```
However, to avoid some conflicts, you should create a python virtual enviroment and activate it. If this package is not installed, please download Python and [this package](https://pypi.org/project/virtualenv/) with Linux OS.
```
virtualenv .venv
source .venv/bin/activate
```
or to create and activate a virtual environment on Windows, run command
```
python -m venv venv
venv\Scripts\activate.bat
```
After enviroment activation, you must install requirement by this command.
```
.venv/bin/pip install -r requirements.txt
```

or in Window
```
pip install -r requirements.txt
```

# Usage
## Analysis
First, you must unzip chess.zip to get data. This data I used is derived from [Chess-Game-From-12-Top-Player](https://www.kaggle.com/datasets/liury123/chess-game-from-12-top-players)

Second, you can run the notebook scripts in the analysis folder with this activated virtual environment to get our analysis.


## About AI Modules
The AI module is written in [./script/chess_ai](./scripts/chess_ai/) with the algorithm mapping file is [ChessAI](./scripts/chess_ai/ChessAI.py). You can use it to call AI algorithms from this file.
Now, there are 2 algorithms in this moudule:
1. Minimax 
2. Minimax with Alpha Beta Pruning
3. Negamax
4. Negamax with ALpha Beta Pruning

You can run a game with bot with run [main.py](./main.py) python file or run it in terminal by command in window
```
python main.py -h
```
or in linux 
```
python3 main.py -h
```
To get some help about how to running this game in terminal and custom your algorithm parameters like depth, ... 

## About Chess App
The chess app is written by Flask and could played in localhost. You can use it by run [app.py](./app.py) python file by terminal by command in window
```
python app.py
```
or in linux 
```
python3 app.py
```
After that, you can open browser with [127.0.0.1:5000](127.0.0.1:5000) to start chess app
