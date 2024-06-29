import pygame
import sys


pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

red_rect = pygame.Rect((175, 0), (50, 400))
blue_rect = pygame.Rect((0, 175), (50, 50))
blue_rect2 = pygame.Rect((0, 0), (50, 50))
blue_rect3 = pygame.Rect((0, 340), (50, 50))
blue_speed = 5
blue2_speed = 10
blue3_speed = 20
moving_right = True
moving_right2 = True
moving_right3 = True
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
    
    if moving_right2:
        blue_rect2.x += blue2_speed
        if blue_rect2.right >= width:
            moving_right2 = False
    else: 
        blue_rect2.x -= blue2_speed
        if blue_rect2.left <= 0:
            moving_right2 = True
    
    if moving_right3:
        blue_rect3.x += blue3_speed
        if blue_rect3.right >= width:
            moving_right3 = False
    else:
        blue_rect3.x -= blue3_speed
        if blue_rect3.left <= 0:
            moving_right3 = True


    if blue_rect.colliderect(red_rect) or blue_rect2.colliderect(red_rect) or blue_rect3.colliderect(red_rect):
        red_color = green
    else:
        red_color = red

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red_color, red_rect)
    pygame.draw.rect(screen, blue, blue_rect)
    pygame.draw.rect(screen, blue, blue_rect2)
    pygame.draw.rect(screen, blue, blue_rect3)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()