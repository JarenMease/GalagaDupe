import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 64
SHIP_HEIGHT = 64
ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()


class GalagaGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Galaga")
        self.clock = pygame.time.Clock()

        # Load images
        self.ship_image = pygame.image.load("images/ship_image.png").convert_alpha()
        self.enemy_image = pygame.image.load("images/enemy_image.png").convert_alpha()

        self.ship_image = pygame.transform.scale(self.ship_image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.enemy_image = pygame.transform.scale(self.enemy_image, (ENEMY_WIDTH, ENEMY_HEIGHT))

        # Set up game objects
        self.ship = pygame.Rect(SCREEN_WIDTH // 2 - SHIP_WIDTH // 2, SCREEN_HEIGHT - SHIP_HEIGHT - 10, SHIP_WIDTH, SHIP_HEIGHT)
        self.enemies = []
        for i in range(5):
            enemy = pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH), random.randint(50, 200), ENEMY_WIDTH, ENEMY_HEIGHT)
            self.enemies.append(enemy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_game_logic(self):
        # Move ship
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ship.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.ship.move_ip(5, 0)

        # Keep ship inside screen
        if self.ship.left < 0:
            self.ship.left = 0
        if self.ship.right > SCREEN_WIDTH:
            self.ship.right = SCREEN_WIDTH

        # Move enemies
        for enemy in self.enemies:
            enemy.move_ip(0, 1)

        # Remove enemies that go off screen
        self.enemies = [enemy for enemy in self.enemies if enemy.bottom < SCREEN_HEIGHT]

    def draw_objects(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.ship_image, self.ship)
        for enemy in self.enemies:
            self.screen.blit(self.enemy_image, enemy)

        pygame.display.flip()

    def run(self):
        # Main game loop
        while True:
            self.handle_events()
            self.update_game_logic()
            self.draw_objects()
            self.clock.tick(60)


if __name__ == "__main__":
    game = GalagaGame()
    game.run()
