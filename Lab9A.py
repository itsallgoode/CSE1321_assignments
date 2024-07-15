import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

lazer = pygame.image.load("laser-98735_640.png").convert_alpha()
power_up = pygame.image.load("button-7086658_640_on.png").convert_alpha()
power_down = pygame.image.load("button-7086658_640_off.png").convert_alpha()
power_up_sound = pygame.mixer.Sound("power-up-7103.mp3")
power_down_sound = pygame.mixer.Sound("power-down-7103.mp3")
shoot_sound = pygame.mixer.Sound("blaster-2-81267.mp3")

new_width = 100
new_height = 100

scaled_lazer = pygame.transform.scale(lazer, (new_width, new_height))
scaled_power_up = pygame.transform.scale(power_up, (new_width, new_height))
scaled_power_down = pygame.transform.scale(power_down, (new_width, new_height))

screen_center = (screen.get_width() // 2, screen.get_height() // 2)
lazer_pos = (screen_center[0] - new_width // 2, screen_center[1] - new_height // 2)
power_up_pos = (lazer_pos[0] - new_width - 20, lazer_pos[1])
power_down_pos = (lazer_pos[0] + new_width + 20, lazer_pos[1])

black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font(None, 32)
status_font = pygame.font.Font(None, 64)

laser_status = "Off"
laser_busy = False

running = True

def play_sound(sound, status):
    global laser_busy, laser_status
    laser_busy = True
    laser_status = status
    sound.play()
    pygame.time.set_timer(pygame.USEREVENT, int(sound.get_length() * 1000))

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and not laser_busy:
            mouse_pos = event.pos
            if scaled_power_up.get_rect(topleft=power_up_pos).collidepoint(mouse_pos) and laser_status == "Off":
                play_sound(power_up_sound, "Charging")
            elif scaled_lazer.get_rect(topleft=lazer_pos).collidepoint(mouse_pos) and laser_status == "Ready":
                play_sound(shoot_sound, "Shooting")
            elif scaled_power_down.get_rect(topleft=power_down_pos).collidepoint(mouse_pos) and laser_status == "Ready":
                play_sound(power_down_sound, "Discharging")
        if event.type == pygame.USEREVENT:
            if laser_status == "Charging":
                laser_status = "Ready"
            elif laser_status == "Shooting":
                laser_status = "Ready"
            elif laser_status == "Discharging":
                laser_status = "Off"
            laser_busy = False
            pygame.time.set_timer(pygame.USEREVENT, 0)

    screen.fill(white)

    lazer_text = font.render("Shoot", True, black)
    power_up_text = font.render("Power Up", True, black)
    power_down_text = font.render("Power Down", True, black)
    status_text = status_font.render(laser_status, True, black)

    status_text_pos = (screen.get_width() // 2 - status_text.get_width() // 2, screen.get_height() // 2 - status_text.get_height() // 2 - 80)
    lazer_text_pos = (lazer_pos[0] + (new_width - lazer_text.get_width()) // 2, lazer_pos[1] + new_height + 20)
    power_up_text_pos = (power_up_pos[0] + (new_width - power_up_text.get_width()) // 2, power_up_pos[1] + new_height + 20)
    power_down_text_pos = (power_down_pos[0] + (new_width - power_down_text.get_width()) // 2, power_down_pos[1] + new_height + 20)
    screen.blit(scaled_lazer, lazer_pos)
    screen.blit(scaled_power_up, power_up_pos)
    screen.blit(scaled_power_down, power_down_pos)
    screen.blit(lazer_text, lazer_text_pos)
    screen.blit(power_up_text, power_up_text_pos)
    screen.blit(power_down_text, power_down_text_pos)
    screen.blit(status_text, status_text_pos)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
