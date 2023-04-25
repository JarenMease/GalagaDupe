import galaga
import pygame
# from bullet import Bullet
import bullet


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ship_image.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (galaga.ship_width, galaga.ship_height))
        self.rect = self.image.get_rect()
        self.rect.x = galaga.screen_width // 2 - galaga.ship_width // 2
        self.rect.y = galaga.screen_height - galaga.ship_height - 10
        self.bullets = pygame.sprite.Group()
        self.speed = 5
        # self.is_firing = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        elif keys[pygame.K_RIGHT] and self.rect.right < galaga.screen_width:
            self.rect.move_ip(self.speed, 0)
        elif keys[pygame.K_SPACE]:
            self.fire_bullet()
        # elif keys[pygame.K_UP]:
        #     # self.fire_bullet()
        #     self.is_firing = True
        # else:
        #     self.is_firing = False

        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > galaga.screen_width:
        #     self.rect.right = galaga.screen_width
        #
        # # if self.is_firing:
        # #     self.fire_bullet()
        #
        # if keys[pygame.K_UP]:
        #     self.fire_bullet()

        self.bullets.update()

    def fire_bullet(self):
        print("Firing bullet")
        new_bullet = bullet.Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(new_bullet)
