import pygame
import sys

# The sound isn't playing at the correct speed but every file i try does the same so I left it as is

pygame.init()
screen = pygame.display.set_mode((800, 600))


black = (0, 0, 0)
white = (255, 255, 255)


maze_width, maze_height = 16, 12 
cell_size = 800 // maze_width


font = pygame.font.Font(None, 36)
initial_timer = 30
timer = initial_timer
timer_started = False

pygame.mixer.init()
treasure_sound = pygame.mixer.Sound("QL7TEGT-applause-cheering.mp3")
start_text = font.render("Start", True, black)
treasure = pygame.image.load("treasure.png").convert_alpha()
treasure_scaled = pygame.transform.scale(treasure, (cell_size, cell_size))

player_image = pygame.image.load("player.png").convert_alpha()
player_scaled = pygame.transform.scale(player_image, (cell_size, cell_size))

player_pos = [cell_size, cell_size]
player_speed = cell_size // 2


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]

def draw_maze():
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, black, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif maze[y][x] == 3:
                screen.blit(treasure_scaled, (x * cell_size, y * cell_size))
            elif maze[y][x] == 2:
                screen.blit(start_text, (x * cell_size, y * cell_size))
def draw_timer():
    timer_text = font.render(f"Time: {round(timer, 0)}", True, white)
    screen.blit(timer_text, (10, 10))

def can_move(new_pos):
    new_rect = pygame.Rect(new_pos[0], new_pos[1], cell_size, cell_size)
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                wall_rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if new_rect.colliderect(wall_rect):
                    return False
    return True

def modify_maze():
    maze[10][13] = 1
    maze[6][14] = 0
    maze[7][14] = 0
    maze[11][14] = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_pos = player_pos.copy()
            if event.key == pygame.K_w and new_pos[1] > 0:
                new_pos[1] -= player_speed
            if event.key == pygame.K_s and new_pos[1] < screen.get_height() - cell_size:
                new_pos[1] += player_speed
            if event.key == pygame.K_d and new_pos[0] < screen.get_width() - cell_size:
                new_pos[0] += player_speed
            if event.key == pygame.K_a and new_pos[0] > 0:
                new_pos[0] -= player_speed

            if can_move(new_pos):
                player_pos = new_pos

            if event.key == pygame.K_r:
                player_pos = [cell_size + 1, cell_size + 1]

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    treasure_rect = pygame.Rect(14 * cell_size, 11 * cell_size, cell_size, cell_size)
    player_rect = pygame.Rect(player_pos[0], player_pos[1], cell_size, cell_size)
    if player_rect.colliderect(treasure_rect):
        modify_maze()
        timer_started = True
        timer = initial_timer
        treasure_sound.play()

    if timer_started:
        timer -= clock.get_time() / 1000  
        if timer <= 0:
            print("Game over.")
            running = False

    start_rect = pygame.Rect(cell_size, cell_size, cell_size, cell_size)
    if player_rect.colliderect(start_rect) and timer_started:
        print("You win!")
        running = False

    screen.fill(white)
    draw_maze()
    draw_timer()
    screen.blit(player_scaled, player_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


