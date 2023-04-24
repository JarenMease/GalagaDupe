import galaga
import pygame
from bullet import Bullet


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ship_image.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.ship_width, galaga.ship_height))
        self.rect = self.image.get_rect()
        self.rect.x = galaga.screen_width // 2 - galaga.ship_width // 2
        self.rect.y = galaga.screen_height - galaga.ship_height - 10
        self.bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        elif keys[pygame.K_UP]:
            self.fire_bullet()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > galaga.screen_width:
            self.rect.right = galaga.screen_width

    def fire_bullet(self):
        new_bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(new_bullet)
