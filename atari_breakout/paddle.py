import pygame
from settings import *

class Paddle:
    def __init__(self):
        self.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = HEIGHT - 40

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += PADDLE_SPEED

        self.x = max(0, min(WIDTH - PADDLE_WIDTH, self.x))

    def rect(self):
        return pygame.Rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))