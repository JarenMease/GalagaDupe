
from galaga import *


class Player:
    def __init__(self, x, y, width, height, ship_image):
        super().__init__()
        self.image = pygame.image.load("images/ship_image.png").convert_alpha()
        self.image = pygame.transform.scale(ship_image, (ship_width, ship_height))
        self.rect = pygame.Rect(screen_width // 2 - ship_width // 2, screen_height - ship_height - 10, ship_width, ship_height)

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep player inside screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

    def draw_player(self, surface):
        surface.bilt(self.image, self.rect)


class Enemy:
    def __init__(self, x, y, width, height, enemy_image):
        super().__init__()
        self.image = pygame.image.load("images/enemy_image.png").convert_alpha()
        self.image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))
        self.rect = pygame.Rect(random.randint(0, screen_width - enemy_width), random.randint(50, 200), enemy_width, enemy_height)

