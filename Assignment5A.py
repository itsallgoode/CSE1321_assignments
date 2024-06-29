import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define maze parameters
CELL_SIZE = 20
MAZE_WIDTH = WINDOW_WIDTH // CELL_SIZE
MAZE_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Define player and treasure positions
player_x = 1
player_y = 1
treasure_x = MAZE_WIDTH - 2
treasure_y = MAZE_HEIGHT - 2

# Define maze layout
maze = [[1] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
maze[player_y][player_x] = 0
maze[treasure_y][treasure_x] = 0

# Generate maze
def generate_maze():
    visited = [[False] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    stack = [(player_y, player_x)]
    visited[player_y][player_x] = True

    while stack:
        current_y, current_x = stack[-1]
        neighbors = []

        # Check neighbors
        if current_y > 1 and not visited[current_y - 2][current_x]:
            neighbors.append((current_y - 2, current_x))
        if current_y < MAZE_HEIGHT - 2 and not visited[current_y + 2][current_x]:
            neighbors.append((current_y + 2, current_x))
        if current_x > 1 and not visited[current_y][current_x - 2]:
            neighbors.append((current_y, current_x - 2))
        if current_x < MAZE_WIDTH - 2 and not visited[current_y][current_x + 2]:
            neighbors.append((current_y, current_x + 2))

        if neighbors:
            next_y, next_x = random.choice(neighbors)
            stack.append((next_y, next_x))
            visited[next_y][next_x] = True
            maze[current_y + (next_y - current_y) // 2][current_x + (next_x - current_x) // 2] = 0
        else:
            stack.pop()

generate_maze()

# Load sound effect
treasure_sound = pygame.mixer.Sound("treasure.wav")

# Game loop
running = True
treasure_found = False
start_time = None
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 0:
        player_y += 1
    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 0:
        player_x += 1

    # Check for treasure collision
    if player_x == treasure_x and player_y == treasure_y:
        treasure_found = True
        treasure_sound.play()
        generate_maze()
        start_time = time.time()

    # Draw maze
    window.fill(BLACK)
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(window, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif treasure_found and (x, y) != (player_x, player_y):
                pygame.draw.rect(window, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(window, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # Draw player and treasure
    if not treasure_found:
        pygame.draw.rect(window, RED, (treasure_x * CELL_SIZE, treasure_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(window, RED, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw timer
    if treasure_found:
        elapsed_time = int(time.time() - start_time)
        remaining_time = 30 - elapsed_time
        if remaining_time <= 0:
            running = False
        font = pygame.font.Font(None, 36)
        text = font.render(f"Time: {remaining_time}", True, WHITE)
        window.blit(text, (10, 10))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

