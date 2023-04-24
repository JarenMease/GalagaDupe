import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((2, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()

    def add(self, sprite_group):
        sprite_group.add(self)
