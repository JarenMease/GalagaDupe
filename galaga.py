import pygame
import sys
import random

from bullet import Bullet
# from player import Starship
# from enemy import Alien
# import bullet
import player
import enemy

screen_width = 800
screen_height = 600
ship_width = 64
ship_height = 64
enemy_width = 32
enemy_height = 32

# colors
black = (0, 0, 0)
white = (255, 255, 255)


# Initialize Pygame
# pygame.init()

class GalagaGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Galaga")
        self.clock = pygame.time.Clock()

        # Load images
        self.ship_image_path = "images/ship_image.png"
        self.enemy_image_path = "images/enemy_image.png"
        self.bullet_image_path = "images/bullet_image.png"

        # Set up game objects
        self.player = player.Starship()
        # self.player = Starship()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        for i in range(10):
            # bugs = Alien(self.enemy_image_path, random.randint(0, screen_width - enemy_width), random.randint(50, 200))
            bugs = enemy.Alien(random.randint(0, screen_width - enemy_width), random.randint(50, 200))
            self.enemies.add(bugs)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.fire_bullet()

    def update_game_logic(self):
        self.player.update()
        self.enemies.update()
        self.bullets.update()

        self.enemies = pygame.sprite.Group([enemy for enemy in self.enemies if enemy.rect.bottom < screen_height])
        self.bullets = pygame.sprite.Group([bullet for bullet in self.bullets if bullet.rect.bottom > 0])

    def draw_objects(self):
        self.screen.fill(black)
        self.screen.blit(self.player.image, self.player.rect)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)

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
