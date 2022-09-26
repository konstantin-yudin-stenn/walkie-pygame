import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = ((size[0] + 200) / 2, (size[1] + 200) / 2)
