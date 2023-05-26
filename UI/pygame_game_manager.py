import string
import time

import keyboard
import pygame

from UI.game_field import Field
from core.game import Game

WIDTH = 800
HEIGHT = 600


class GameManager:

    def __init__(self, game):
        self.field_size = game.MAX_SIZE
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.field = Field((WIDTH - 200, HEIGHT - 200), game.field)
        self.game = Game(self.field_size)

    def drow_field(self):
        myfont = pygame.font.SysFont("monospace", 20)
        pos = (100, 100)
        new = ''.join(filter(str.isalnum, str(self.field)))
        for index, item in enumerate(new):
            if index > 0 and index % 10 == 0:
                pos = (100, pos[1] + 20)
            label = myfont.render(str(item), False, (255, 255, 255))
            self.screen.blit(label, pos)
            pos = (pos[0] + 20, pos[1])
        pygame.display.update()

    def start_game(self):
        running = True

        while running:
            self.drow_field()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.game.move_player(keyboard.read_key())
            self.screen.fill(pygame.Color("black"))
            self.field = Field((WIDTH - 200, HEIGHT - 200), self.game.field)

            time.sleep(0.2)

        pygame.quit()
