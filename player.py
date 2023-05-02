import time

import galaga
import pygame
import bullet


class Starship(pygame.sprite.Sprite):
    def __init__(self, ship_image_path, bullet_image_path):
        super().__init__()
        self.image = pygame.image.load(ship_image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.SHIP_WIDTH, galaga.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = galaga.SCREEN_WIDTH // 2 - galaga.SHIP_WIDTH // 2
        self.rect.y = galaga.SCREEN_HEIGHT - galaga.SHIP_HEIGHT - 10
        self.bullets = pygame.sprite.Group()
        self.speed = 5
        self.bullet_image_path = bullet_image_path
        self.last_shot_time = 0.0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        elif keys[pygame.K_RIGHT] and self.rect.right < galaga.SCREEN_WIDTH:
            self.rect.move_ip(self.speed, 0)
        elif keys[pygame.K_SPACE]:
            current_time = time.time()
            time_since_last_shot = current_time - self.last_shot_time
            if time_since_last_shot >= 0.25:
                self.fire_bullet()
                self.last_shot_time = current_time
            # self.fire_bullet()

        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)

    def fire_bullet(self):
        new_bullet = bullet.Bullet(self.bullet_image_path, self.rect.centerx, self.rect.top)
        self.bullets.add(new_bullet)

    def reset_player(self):
        self.rect.x = galaga.SCREEN_WIDTH // 2 - galaga.SHIP_WIDTH // 2
        self.rect.y = galaga.SCREEN_HEIGHT - galaga.SHIP_HEIGHT - 10
        self.bullets.empty()

