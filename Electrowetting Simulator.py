
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50
 
# This sets the margin between each cell
MARGIN = 10
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1
 
# Initialize pygame
pygame.init()

font = pygame.font.SysFont("comicsansms", 12)



 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800,800]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Electrowetting Simulator")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
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
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN


            curX = (MARGIN + WIDTH) * column + MARGIN
            curY = (MARGIN + HEIGHT) * row + MARGIN

            X = curX + int(WIDTH/2)
            Y = curY + int(HEIGHT/2)
            pygame.draw.rect(screen,
                             color,[curX,curY,           
                              WIDTH,
                              HEIGHT])

            pos = str(row) + "-" + str(column);

            #Grid location text labels

            text = font.render(pos, True, BLACK)
            
            screen.blit(text,(curX+2,curY))
    
 
    #Draw the Droplets
    pygame.draw.circle(screen,RED,(curX + int(WIDTH/2) ,curY + int(HEIGHT/2)),
                                   25)



################

#TODO
   # def MoveDrop(drop,start,end):
     #   drop = 
        
################
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
