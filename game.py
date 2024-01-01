import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 600, 600
FPS = 30
CELL_SIZE = 30
MAZE = [
    "#######",
    "#S....#",
    "#.###.#",
    "#.#...#",
    "#.#.###",
    "#.....E",
    "#######"
]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Puzzler")

# Load images
player_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
player_image.fill(RED)

wall_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
wall_image.fill(BLACK)

empty_image = pygame.Surface((CELL_SIZE, CELL_SIZE))
empty_image.fill(WHITE)

# Find the starting position (S)
start_pos = None
for i in range(len(MAZE)):
    for j in range(len(MAZE[i])):
        if MAZE[i][j] == 'S':
            start_pos = (j * CELL_SIZE, i * CELL_SIZE)
            break

player_pos = start_pos

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] > 0 and MAZE[player_pos[1] // CELL_SIZE - 1][player_pos[0] // CELL_SIZE] != '#':
        player_pos = (player_pos[0], player_pos[1] - CELL_SIZE)
    elif keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - CELL_SIZE and MAZE[player_pos[1] // CELL_SIZE + 1][player_pos[0] // CELL_SIZE] != '#':
        player_pos = (player_pos[0], player_pos[1] + CELL_SIZE)
    elif keys[pygame.K_LEFT] and player_pos[0] > 0 and MAZE[player_pos[1] // CELL_SIZE][player_pos[0] // CELL_SIZE - 1] != '#':
        player_pos = (player_pos[0] - CELL_SIZE, player_pos[1])
    elif keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - CELL_SIZE and MAZE[player_pos[1] // CELL_SIZE][player_pos[0] // CELL_SIZE + 1] != '#':
        player_pos = (player_pos[0] + CELL_SIZE, player_pos[1])

    # Draw the maze
    for i in range(len(MAZE)):
        for j in range(len(MAZE[i])):
            if MAZE[i][j] == '#':
                screen.blit(wall_image, (j * CELL_SIZE, i * CELL_SIZE))
            else:
                screen.blit(empty_image, (j * CELL_SIZE, i * CELL_SIZE))

    # Draw the player
    screen.blit(player_image, player_pos)

    pygame.display.flip()
    clock.tick(FPS)

