import pygame
import sys


pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

red_rect = pygame.Rect((width // 2 - 25, 0), (50, 400))
blue_rect = pygame.Rect((0, height // 2 - 25), (50, 50))

blue_speed = 5
moving_right = True

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    if moving_right:
        blue_rect.x += blue_speed
        if blue_rect.right >= width:
            moving_right = False
    else:
        blue_rect.x -= blue_speed
        if blue_rect.left <= 0:
            moving_right = True

    if blue_rect.colliderect(red_rect):
        red_color = green
    else:
        red_color = red

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red_color, red_rect)
    pygame.draw.rect(screen, blue, blue_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
