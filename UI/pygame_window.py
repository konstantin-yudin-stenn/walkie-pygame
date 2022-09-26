import time

import keyboard
import pygame

from UI.pygame_field import Field
from UI.pygame_player import Player
from UI.pygame_room import Rooms

WIDTH = 800
HEIGHT = 600

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class GameManager:

    def __init__(self, game):
        self.field_size = game.MAX_SIZE
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.OrderedUpdates()
        field = Field((WIDTH-200, HEIGHT-200))
        rooms = Rooms(game, field)
        player = Player((field.rect.w / self.field_size, field.rect.h / self.field_size))
        self.all_sprites.add(field)

        self.all_sprites.add(player)
        for item in rooms.list_of_rooms:
            self.all_sprites.add(item)

    def drow_sprites(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def start_game(self, game):
        running = True
        self.drow_sprites()

        while running:
            self.clock.tick(30)

            # Ввод процесса (события)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # logic
            direction = keyboard.read_key()
            game.move_player(direction)
            self.all_sprites.update(field=game.field,
                                    button=direction)
            self.drow_sprites()
            time.sleep(0.2)

        pygame.quit()
