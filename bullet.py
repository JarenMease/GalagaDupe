import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # self.image = pygame.Surface((2, 10))
        # self.image = pygame.Surface((10, 20))
        self.image = pygame.image.load("images/bullet_image.png").convert_alpha()
        # self.image.fill((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        self.rect.centerx = x
        self.rect.bottom = y
        # self.speed = 5
        self.speed = 3

    def update(self):
        # self.rect.y += self.speed
        self.rect.move_ip(10, self.speed)

    # def update(self):
    #     self.rect.move_ip(0, self.speed)
    #     if self.rect.bottom < 0:
    #         self.kill()

    # def update(self):
    #     self.rect.y -= self.speed
    #     if self.rect.bottom <= 0:
    #         self.kill()

    # def add(self, sprite_group):
    #     sprite_group.add(self)
        # sprite_group
