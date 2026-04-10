import random
import pygame
from settings import *

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-3, 3])
        self.dy = -3

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def rect(self):
        return pygame.Rect(
            self.x - BALL_RADIUS,
            self.y - BALL_RADIUS,
            BALL_RADIUS * 2,
            BALL_RADIUS * 2
        )

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (int(self.x), int(self.y)), BALL_RADIUS)

    def normalize_speed(self):
        length = (self.dx**2 + self.dy**2) ** 0.5
        self.dx = self.dx / length * BALL_SPEED
        self.dy = self.dy / length * BALL_SPEED