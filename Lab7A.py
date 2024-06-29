import pygame, sys
from pygame.locals import *
# Initializes Pygame
pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
# Main gameplay loop

FPS = 60
change_every_x_seconds = 15
color_change_speed = 255 / (FPS * change_every_x_seconds)
color_value = 0
increasing = True


while True:
    # Check which keys have been pressed
    keys = pygame.key.get_pressed()
    # Checks what events happened, and act on them.
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    # Paint the whole screen back
    if increasing:
        color_value += color_change_speed
        if color_value >= 255:
            color_value = 255
            increasing = False
    else:
        color_value -= color_change_speed
        if color_value <= 0:
            color_value = 0
            increasing = True

    color = (color_value, color_value, color_value)
    screen.fill(color)

    # Update the Display with the contents of the Display's surface
    pygame.display.flip()
    # Slow the game to update 60 times per second
    clock.tick(FPS)
