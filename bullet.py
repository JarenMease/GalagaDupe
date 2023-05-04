import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 2

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom <= 0:
            self.reset()

    def check_bullet_collision(self, enemy_group, score):
        collisions = pygame.sprite.spritecollide(self, enemy_group, True)
        if collisions:
            self.reset()
            for enemy in collisions:
                score.add_points(enemy.alien_points)

    def reset(self):
        self.kill()
