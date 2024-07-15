import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500))

rect1 = pygame.Rect(0, 0, 100, 100)
rect2 = pygame.Rect(0, 400, 100, 100)

rect = pygame.Rect(50, 100, 25, 30)
print(rect.bottomright)
surf1 = pygame.Surface((rect1.w, rect1.h))
surf1.fill((0, 255, 0))  

surf2 = pygame.Surface((rect2.w, rect2.h))
surf2.fill((0, 0, 255))  

speed1 = 5
speed2 = 5

running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    
    rect1.move_ip(speed1, 0)
    rect2.move_ip(speed2, 0)

    if rect1.right >= screen.get_width() or rect1.left <= 0:
        speed1 = -speed1
    if rect2.right >= screen.get_width() or rect2.left <= 0:
        speed2 = -speed2
        
    
    screen.fill((0, 0, 0))


    screen.blit(surf1, rect1.topleft)
    screen.blit(surf2, rect2.topleft)

    pygame.display.update()
    clock.tick(60)

