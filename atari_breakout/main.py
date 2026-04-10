import pygame 
import sys 

from settings import * 
from ball import Ball 
from paddle import Paddle 
from brick import BrickManager

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock() 
font = pygame.font.SysFont(None, 36)

ball = Ball() 
paddle = Paddle() 
bricks = BrickManager() 


score = 0 
lives = 3 

while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit() 
            sys.exit() 

    keys = pygame.key.get_pressed()
    paddle.move(keys)        

    ball.move() 
    ball_rect = ball.rect()

    # walls 
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball.dx = -ball.dx

    if ball_rect.top  <= 0:
        ball.dy = -ball.dy 

    # bottom 
    if ball_rect.bottom >= HEIGHT:
        lives -= 1

        if lives == 0:
            print("Game Over..")
            pygame.quit()
            sys.exit()
        
        ball = Ball()

    # paddle_collision 
    if ball_rect.colliderect(paddle.rect()) and ball.dy > 0:
        hit_pos = (ball.x - paddle.x) / PADDLE_WIDTH 
        ball.dx = (hit_pos - 0.5) * 8
        ball.dy = -abs(ball.dy)
        ball.y = paddle.y - BALL_RADIUS 
        ball.normalize_speed()
    
    # bricks 
    if bricks.collide(ball_rect, ball):
        score += 1
    if len(bricks.bricks) == 0:
        screen.fill((0, 0, 0))
        win_text = font.render("YOU WIN!", True, (0, 255, 0))
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    

    # draw       
    screen.fill((0, 0, 0))

    paddle.draw(screen)
    ball.draw(screen)
    bricks.draw(screen)


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)


