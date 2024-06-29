import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

blue = (0, 0, 255)
black = (0, 0, 0)

rect = pygame.Rect((225, 225), (50, 50))
rect_speed = 5

running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    if keys[pygame.K_w] and rect.top > 0:
        rect.y -= rect_speed
    if keys[pygame.K_s] and rect.bottom < screen.get_height():
        rect.y += rect_speed
    if keys[pygame.K_d] and rect.right < screen.get_width():
        rect.x += rect_speed
    if keys[pygame.K_a] and rect.left > 0:
        rect.x -= rect_speed
    if keys[pygame.K_r]:
        rect.x, rect.y = 225, 225
    
    screen.fill(black)
    pygame.draw.rect(screen, blue, rect)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
