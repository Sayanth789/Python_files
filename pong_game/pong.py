import pygame
import sys
import random

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

# Paddles
player = pygame.Rect(50, 250, 10, 100)
opponent = pygame.Rect(740, 250, 10, 100)

# Ball
ball = pygame.Rect(390, 290, 20, 20)
ball_speed_x = random.choice((4, -4))
ball_speed_y = random.choice((4, -4))

# Scores
player_score = 0
opponent_score = 0

font = pygame.font.Font(None, 60)


def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x = random.choice((4, -4))
    ball_speed_y = random.choice((4, -4))


while True:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.top > 0:
        player.y -= 6
    if keys[pygame.K_s] and player.bottom < HEIGHT:
        player.y += 6

    # Opponent AI
    if opponent.centery < ball.centery:
        opponent.y += 5
    if opponent.centery > ball.centery:
        opponent.y -= 5

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Paddle collision
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        opponent_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        player_score += 1
        reset_ball()

    # Drawing
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), opponent)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    pygame.draw.aaline(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Score display
    player_text = font.render(str(player_score), True, (255, 255, 255))
    opponent_text = font.render(str(opponent_score), True, (255, 255, 255))

    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)
