import pygame
import sys
input = pygame.key
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 23
HEIGHT = 23
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array.
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0) 
 
# Set the HEIGHT and WIDTH
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Soduko Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Game Loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_0:
                    print("test")
			
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(9):
        for column in range(9):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)

    pygame.display.flip()
	
pygame.quit()
