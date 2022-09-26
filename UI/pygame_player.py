import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, size: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (100+(size[0]/2), 100+(size[1]/2))
        self.speed = size

    def update(self, *args, **kwargs):
        speedx = 0
        speedy = 0
        if kwargs['button'] == 'left':
            speedx = -self.speed[0]
        if kwargs['button'] == 'right':
            speedx = self.speed[0]
        if kwargs['button'] == 'up':
            speedy = -self.speed[1]
        if kwargs['button'] == 'down':
            speedy = self.speed[1]

        self.rect.x += speedx
        self.rect.y += speedy

        if self.rect.right > 800 - 100:
            self.rect.right = 800 - 100
        if self.rect.left < 0 + 100:
            self.rect.left = 0 + 100

        if self.rect.bottom > 600 - 100:
            self.rect.bottom = 600 - 100
        if self.rect.top < 0 + 100:
            self.rect.top = 0 + 100
