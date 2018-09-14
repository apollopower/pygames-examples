# Import Pygame modele:
import pygame, sys

#import some useful constants
from pygame.locals import *

#init the pygame module:
pygame.init()

# Constants representing different resources:

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

# A list representing a tilemap:
tilemap = [
    [GRASS, COAL, ROCK, LAVA,  DIRT],
    [WATER, WATER, GRASS, ROCK, ROCK],
    [COAL, GRASS, WATER, GRASS, DIRT],
    [DIRT, GRASS, COAL, LAVA, LAVA],
    [GRASS, WATER, DIRT, ROCK, COAL]
]


# A dictionary linking resources to textures:
textures = {
    DIRT: pygame.image.load("resources/dirt.png"),
    GRASS: pygame.image.load("resources/grass.png"),
    WATER: pygame.image.load("resources/water.png"),
    COAL: pygame.image.load("resources/coal.png"),
    ROCK: pygame.image.load("resources/rock.png"),
    LAVA: pygame.image.load("resources/lava.png")
}


# Game Dimensions:
TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

# Create a new drawing surface, width=300 height=300
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE), )

# Give the window a caption:
pygame.display.set_caption("Python Game")

# Loop for game:
while True:
    # Get all the user events;
    for event in pygame.event.get():
        # If user presses close window button:
        if event.type == QUIT:
            # End game
            pygame.quit()
            sys.exit()
    
    # End of event checker:

    # Draw out tilemap:
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Draw the resource at that position in the tilemap
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    # update the display:
    pygame.display.update()