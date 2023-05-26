from UI.pygame_game_manager import GameManager
from core.game import Game

FIELD_SIZE = 10

if __name__ == '__main__':
    game = Game(FIELD_SIZE)
    manager = GameManager(game)
    manager.start_game()


