import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,600))
surf = pygame.Surface((60,60))
surf.fill((255,0,0))
surf1 = pygame.Surface((60,60))
surf1.fill((255,0,0))
surf2 = pygame.Surface((60,60))
surf2.fill((255,0,0))
surf3 = pygame.Surface((60,60))
surf3.fill((255,0,0))
surf4 = pygame.Surface((60,60))
surf4.fill((255,0,0))
surf5 = pygame.Surface((60,60))
surf5.fill((255,0,0))



screen.blit(surf, (0,0))
screen.blit(surf1, (0, 540))
screen.blit(surf2, (540,0))
screen.blit(surf3, (540, 540))
# now we put one in the middle
screen.blit(surf4, (270,270))
pygame.display.flip()

running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
            




