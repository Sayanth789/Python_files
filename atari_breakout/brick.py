import pygame 
from settings import * 

class BrickManager:
    def __init__(self):
        self.bricks = [] 

        for row in range(ROWS):
            for col in range(COLS):
                x = col * (BRICK_WIDTH + GAP) + OFFSET_X
                y = row * (BRICK_HEIGHT + GAP)  + OFFSET_Y

                color = COLORS[row % len(COLORS)]
                self.bricks.append([x, y, color])

    def draw(self, screen):
        for brick in self.bricks:
            pygame.draw.rect(screen, brick[2],
                             (brick[0], brick[1], BRICK_WIDTH, BRICK_HEIGHT))
            
    def collide(self, ball_rect, ball):
        for brick in self.bricks[:]:
            brick_rect = pygame.Rect(brick[0], brick[1], BRICK_WIDTH, BRICK_HEIGHT)
            
            if ball_rect.colliderect(brick_rect):
                self.bricks.remove(brick)

                if abs(ball_rect.bottom - brick_rect.top) < 10:
                    ball.dy = -abs(ball.dy)
                elif abs(ball_rect.top - brick_rect.bottom) < 10:
                    ball.dy = abs(ball.dy)    
                else:
                    ball.dx = -ball.dx 
                return True 
        return False         