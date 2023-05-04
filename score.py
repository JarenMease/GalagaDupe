import pygame


class Scoring:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 36)
        self.image = self.font.render(f"Score: {self.score}", True, "WHITE")
        self.rect = self.image.get_rect()
        self.update_image()

    def update_image(self):
        self.image = self.font.render(f"Score: {self.score}", True, "WHITE")

    def add_points(self, points):
        self.score += points
        self.update_image()

    def get_score(self):
        return self.score

    def draw(self, screen):
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

    def reset(self):
        self.score = 0
        self.update_image()

