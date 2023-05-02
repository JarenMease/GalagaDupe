import pygame
import galaga


class Alien(pygame.sprite.Sprite):
    def __init__(self, enemy_image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(enemy_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.ENEMY_WIDTH, galaga.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 5
        self.alien_points = 5

    def update(self):
        self.rect.move_ip(self.direction * self.speed, 0)
        if self.rect.left < 0 or self.rect.right > galaga.SCREEN_WIDTH:
            self.direction *= -1
            self.rect.move_ip(0, galaga.ENEMY_HEIGHT)


class FastAlien(Alien):
    def __init__(self, fast_enemy_image_path, x, y):
        super().__init__(fast_enemy_image_path, x, y)
        self.image = pygame.image.load(fast_enemy_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.FAST_ENEMY_WIDTH, galaga.FAST_ENEMY_HEIGHT))
        self.direction = 1
        self.speed = 15
        self.alien_points = 15

    def update(self):
        self.rect.move_ip(self.direction * self.speed, 0)
        if self.rect.left < 0 or self.rect.right > galaga.SCREEN_WIDTH:
            self.direction *= -1
            self.rect.move_ip(0, galaga.FAST_ENEMY_HEIGHT)

