import pygame


class Scoring:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.image = self.font.render(f"Score: {self.score}", True, "WHITE")
        self.rect = self.image.get_rect()

    def add_points(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.score = 0


