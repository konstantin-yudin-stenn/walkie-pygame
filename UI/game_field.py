import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, size, field):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.center = ((size[0] + 200) / 2, (size[1] + 200) / 2)
        self.field = field.field

    def __str__(self):
        items = [[row.status for row in rows] for rows in self.field]
        return str(items)
