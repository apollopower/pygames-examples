# Import Pygame modele:
import pygame, sys, random

#import some useful constants
from pygame.locals import *

#init the pygame module:
pygame.init()


# PLAYER DATA
PLAYER = pygame.image.load("resources/player.png")
# The position of the player, X & Y
playerPos = [0,0]


# Constants representing different resources:

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5

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
MAPWIDTH = 25
MAPHEIGHT = 15


# List of our game resources:
resources = [DIRT, GRASS, WATER, COAL, ROCK, LAVA]

# Use list comprehension to generate tilemap (initializing first to only dirt)
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

# Create a new drawing surface
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

# Give the window a caption:
pygame.display.set_caption("Chinese Minecraft")


# Generating Game World:
# Loop through each row
for rw in range(MAPHEIGHT):
    # Loop through each column of row
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,50)
        # if 0, make it lava
        if randomNumber == 0:
            tile = LAVA
        elif randomNumber >=1 and randomNumber <= 3:
            tile = COAL
        elif randomNumber >= 4 and randomNumber <= 10:
            tile = WATER
        elif randomNumber >= 11 and randomNumber <= 16:
            tile = ROCK
        elif randomNumber >= 17 and randomNumber <= 25:
            tile = GRASS
        elif randomNumber >= 26:
            tile = DIRT
        # Set the position on tilemap to this tile:
        tilemap[rw][cl] = tile


# Loop for game:
while True:
    # Get all the user events;
    for event in pygame.event.get():
        # If user presses close window button:
        if event.type == QUIT:
            # End game
            pygame.quit()
            sys.exit()
        # If a key is pressed:
        elif event.type == KEYDOWN:
            if event.key == K_d:
                playerPos[0] += 1
            elif event.key == K_a:
                playerPos[0] -= 1
            elif event.key == K_w:
                playerPos[1] -= 1
            elif event.key == K_s:
                playerPos[1] += 1
    
    # End of event checker:

    # Draw out tilemap:
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Draw the resource at that position in the tilemap
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    # Display player in correct position:
    DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
    # update the display:
    pygame.display.update()