import pygame
import random

import player
import enemy
from enemy import Alien, FastAlien
import score

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 64
SHIP_HEIGHT = 64
ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32
FAST_ENEMY_WIDTH = 16
FAST_ENEMY_HEIGHT = 16

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
        self.fast_enemy_image_path = "images/fast_enemy.png"

        # Set up game objects
        self.player = player.Starship(self.ship_image_path, self.bullet_image_path)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()

        self.spawn_threshold = 10
        self.second_wave = 15

        for i in range(50):
            bug = Alien(self.enemy_image_path, random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                        random.randint(50, 200))
            self.enemies.add(bug)

        self.game_over = False
        self.user_quit = False

        self.score = score.Scoring()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.reset_game()

    def update_game_logic(self):
        # if self.game_over:
        #     return

        self.player.update()
        self.enemies.update()
        self.bullets.update()
        self.enemies = pygame.sprite.Group([enemy for enemy in self.enemies if enemy.rect.bottom < SCREEN_HEIGHT])
        self.bullets = pygame.sprite.Group([bullet for bullet in self.player.bullets if bullet.rect.bottom > 0])
        self.score.get_score()

        for bullet in self.bullets:
            bullet.check_bullet_collision(self.enemies, self.score)

        self.check_enemy_collisions()

        if len(self.enemies) < self.second_wave and len(self.enemies) + self.second_wave - len(self.enemies) <= 50:
            for i in range(self.second_wave - len(self.enemies)):
                bug = FastAlien(self.fast_enemy_image_path, random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                                random.randint(50, 200))
                self.enemies.add(bug)

    def check_enemy_collisions(self):
        game_over_text = None
        for bug_enemy in self.enemies:
            if pygame.sprite.collide_rect(bug_enemy, self.player):
                game_over_text = "Player hit by enemy. Press 0 to restart."
                self.game_over = True
            if bug_enemy.rect.bottom >= SCREEN_HEIGHT:
                game_over_text = "Enemy reached bottom of screen. Press 0 to restart."
                self.game_over = True
        if self.game_over:
            self.show_game_over_screen(game_over_text)

    def show_game_over_screen(self, text):
        while True:
            self.screen.fill(BLACK)
            font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
            game_over_text = font.render(text, True, WHITE)
            score_text = font.render("Score: {}".format(self.score.get_score()), True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.reset_game()
                        return

    def reset_game(self):
        self.game_over = False
        self.player.reset_player()
        for old_enemy in self.enemies:
            old_enemy.kill()
        for old_bullet in self.bullets:
            old_bullet.kill()
        self.score.reset()
        for i in range(50):
            bug = enemy.Alien(self.enemy_image_path, random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH),
                              random.randint(50, 200))
            self.enemies.add(bug)

    def draw_objects(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.player.image, self.player.rect)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.score.draw(self.screen)
        self.score_group.draw(self.screen)
        self.score.image = self.score.font.render(f"Score: {self.score.score}", True, "WHITE")
        self.screen.blit(self.score.image, self.score.rect)
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
