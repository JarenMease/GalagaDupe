import pygame
import galaga


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/enemy_image.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.enemy_width, galaga.enemy_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 3

    def update(self):
        self.rect.move_ip(self.direction * self.speed, 0)
        if self.rect.left < 0 or self.rect.right > galaga.screen_width:
            self.direction *= -1
            self.rect.move_ip(0, galaga.enemy_height)


