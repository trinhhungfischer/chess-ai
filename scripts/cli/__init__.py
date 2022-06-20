import click
from scripts.chess_game import ChessGame

@click.version_option(version='0.1.3')
@click.command(context_settings=dict(help_option_names=['-h', '--help']), no_args_is_help=True)
@click.option('-a', '--algorithm', default='Minimax', show_default=True, type=str, help='The algorithms that was listed in readme')
@click.option('-d', '--depth-search', default=3, show_default=True, type=int, help='The depth of minimax searching tree')
@click.option('-s', '--start-board', type=str, help='The start board which you can use to solve chess puzzle')


def cli(algorithm = 'Minimax', depth_search = 3, start_board = None):
  game = ChessGame(aiModule=algorithm, depthSearch=depth_search, board=start_board)
  game.runGame()