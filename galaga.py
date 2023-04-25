import pygame
import random

from bullet import Bullet
import player
import enemy

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


class GalagaGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Galaga")
        self.clock = pygame.time.Clock()

        # Load images
        self.ship_image_path = "images/ship_image.png"
        self.enemy_image_path = "images/enemy_image.png"
        self.bullet_image_path = "images/bullet_image.png"

        # Set up game objects
        self.player = player.Starship(self.ship_image_path, self.bullet_image_path)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        for i in range(10):
            bugs = enemy.Alien(self.enemy_image_path, random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                               random.randint(50, 200))
            self.enemies.add(bugs)

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.reset_game()

    def update_game_logic(self):
        if self.game_over:
            return

        self.player.update()
        self.enemies.update()
        self.bullets.update()

        self.enemies = pygame.sprite.Group([enemy for enemy in self.enemies if enemy.rect.bottom < SCREEN_HEIGHT])
        self.bullets = pygame.sprite.Group([bullet for bullet in self.player.bullets if bullet.rect.bottom > 0])

        for bullet in self.bullets:
            bullet.check_bullet_collision(self.enemies)

        self.check_enemy_collisions()

    def check_enemy_collisions(self):
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(enemy, self.player):
                print("Player hit by enemy")
                self.game_over = True
            if enemy.rect.bottom >= SCREEN_HEIGHT:
                print("Enemy reached bottom of screen")
                self.game_over = True

        if self.game_over:
            self.show_game_over_screen()

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render("You lost! Press 0 to Restart", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(30000)
        # pygame.quit()
        # quit()

    def reset_game(self):
        self.game_over = False
        self.player.reset_player()
        self.enemies.empty()
        self.bullets.empty()
        for i in range(10):
            bugs = enemy.Alien(self.enemy_image_path, random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                               random.randint(50, 200))
            self.enemies.add(bugs)

    def draw_objects(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.player.image, self.player.rect)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update_game_logic()
            self.draw_objects()
            self.clock.tick(60)


if __name__ == "__main__":
    game = GalagaGame()
    game.run()
