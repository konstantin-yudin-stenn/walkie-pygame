from core.battlefield import Field
from core.controllers.player_move_controller import PlayerMoveController
from core.player import Player


class Game:

    def __init__(self, size):
        self.MAX_SIZE = size
        self.field = Field(self.MAX_SIZE)
        self.player = Player(self.MAX_SIZE)
        self.field[self.player.position_x][self.player.position_y].status = 'P'

    def move_player(self, direction):
        new_coordinate_x, new_coordinate_y = PlayerMoveController.move(self.field, direction)
        self.field[self.player.position_x][self.player.position_y].status = '1'
        self.player.position_x = new_coordinate_x
        self.player.position_y = new_coordinate_y
        self.field[self.player.position_x][self.player.position_y].status = 'P'

    def __str__(self):
        return str(self.field)
