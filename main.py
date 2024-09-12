from game import Game
from renderer import ConsoleRenderer

if __name__ == '__main__':
    new_game = Game(renderer_type=ConsoleRenderer)
    new_game.run()
