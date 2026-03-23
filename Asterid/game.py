import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

x, y = 400, 300
angle = 0
velocity = [0, 0]

clock = pygame.time.Clock()
running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        angle -= 5

    if keys[pygame.K_RIGHT]:
        angle += 5

    if keys[pygame.K_UP]:
        velocity[0] += math.cos(math.radians(angle)) * 0.1
        velocity[1] += math.sin(math.radians(angle)) * 0.1

    # update position
    x += velocity[0]
    y += velocity[1]

    # screen wrap
    x %= 800
    y %= 600

    # ship triangle
    points = [
        (x + math.cos(math.radians(angle)) * 20,
         y + math.sin(math.radians(angle)) * 20),

        (x + math.cos(math.radians(angle + 140)) * 20,
         y + math.sin(math.radians(angle + 140)) * 20),

        (x + math.cos(math.radians(angle - 140)) * 20,
         y + math.sin(math.radians(angle - 140)) * 20),
    ]

    pygame.draw.polygon(screen, (255,255,255), points, 1)

    pygame.display.flip()
    clock.tick(60)
