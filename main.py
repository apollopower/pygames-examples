# Import Pygame modele:
import pygame, sys, random

#import some useful constants
from pygame.locals import *

#init the pygame module:
pygame.init()

# clock to manage frames
fpsClock = pygame.time.Clock()

# __________________________________________________

# PLAYER DATA
PLAYER = pygame.image.load("resources/player.png")
# The position of the player, X & Y
playerPos = [0,0]

# Constants representing colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# __________________________________________________

# RESOURCES


# Constants representing different resources:

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
LAVA = 5
CLOUD = 6


# Inventory:
inventory = {
    DIRT: 0,
    GRASS: 0,
    WATER: 0,
    COAL: 0,
    ROCK: 0,
    LAVA: 0
}

# Font for inventory:
INVFONT = pygame.font.SysFont('HelveticaBold.ttf', 24)

# A dictionary linking resources to textures:
textures = {
    DIRT: pygame.image.load("resources/dirt.png"),
    GRASS: pygame.image.load("resources/grass.png"),
    WATER: pygame.image.load("resources/water.png"),
    COAL: pygame.image.load("resources/coal.png"),
    ROCK: pygame.image.load("resources/rock.png"),
    LAVA: pygame.image.load("resources/lava.png"),
    CLOUD: pygame.image.load("resources/cloud.png")
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
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 80))

# Give the window a caption, and icon:
pygame.display.set_caption("SquareCraft")
pygame.display.set_icon(textures[GRASS])


# Generating Game World:
# Loop through each row
for rw in range(MAPHEIGHT):
    # Loop through each column of row
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,60)
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


# _________________________________________________________

# Cloud starting X Position on screen:
cloud1X = -200
cloud1Y = 0

cloud2X = -250
cloud2Y = random.randint(0, MAPHEIGHT*TILESIZE)

cloud3X = -350
cloud3Y = random.randint(0, MAPHEIGHT*TILESIZE)


# __________________________________________________________
# GAME

# Loop for game:
while True:
    # Resetting screen to black to avoid visual issues
    DISPLAYSURF.fill(BLACK)
    # Get all the user events;
    for event in pygame.event.get():
        # If user presses close window button:
        if event.type == QUIT:
            # End game
            pygame.quit()
            sys.exit()
        # If a key is pressed:
        elif event.type == KEYDOWN:
            # ____________________________________________________________
            # MOVEMENT
            if event.key == K_d:
                if playerPos[0] < (MAPWIDTH - 1): playerPos[0] += 1
            elif event.key == K_a:
                playerPos[0] -= 1 if playerPos[0] > 0 else 0
            elif event.key == K_w:
                playerPos[1] -= 1 if playerPos[1] > 0 else 0
            elif event.key == K_s:
                if playerPos[1] < (MAPHEIGHT - 1): playerPos[1] += 1
            # _____________________________________________________________
            # Mining/adding to inventory
            if event.key == K_SPACE:
                # What resource is the player standing on?
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                # If for inventory, Player now has one more of the resource:
                if currentTile in inventory:
                    inventory[currentTile] += 1
                    # After mining, the player is standing on dirt:
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    print(inventory[currentTile])
            # ______________________________________________________________
            # Placing Down Blocks
            if event.key == K_1 and inventory[DIRT] > 0:
                inventory[DIRT] -= 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
            elif event.key == K_2 and inventory[GRASS] > 0:
                inventory[GRASS] -= 1
                tilemap[playerPos[1]][playerPos[0]] = GRASS
            elif event.key == K_3 and inventory[WATER] > 0:
                inventory[WATER] -= 1
                tilemap[playerPos[1]][playerPos[0]] = WATER
            elif event.key == K_4 and inventory[COAL] > 0:
                inventory[COAL] -= 1
                tilemap[playerPos[1]][playerPos[0]] = COAL
            elif event.key == K_5 and inventory[ROCK] > 0:
                inventory[ROCK] -= 1
                tilemap[playerPos[1]][playerPos[0]] = ROCK
            elif event.key == K_6 and inventory[LAVA] > 0:
                inventory[LAVA] -= 1
                tilemap[playerPos[1]][playerPos[0]] = LAVA

    
    # End of event checker:

    # Draw out tilemap:
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Draw the resource at that position in the tilemap
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
    
    # Display Cloud, moving it slightly each frame:
 
    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloud1X, cloud1Y))
    cloud1X += 1
    if cloud1X > MAPWIDTH*TILESIZE:
        cloud1X = -200
        cloud1Y = random.randint(0,MAPHEIGHT*TILESIZE)
    
    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloud2X, cloud2Y))
    cloud2X += 1
    if cloud2X > MAPWIDTH*TILESIZE:
        cloud2X = -200
        cloud2Y = random.randint(0,MAPHEIGHT*TILESIZE)

    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(), (cloud3X, cloud3Y))
    cloud3X += 1
    if cloud3X > MAPWIDTH*TILESIZE:
        cloud3X = -200
        cloud3Y = random.randint(0,MAPHEIGHT*TILESIZE)

    
    # Display Inventory (starting 10 pixels in):
    placePosition = 10
    for item in resources:
        # Add the image
        DISPLAYSURF.blit(textures[item],(placePosition, MAPHEIGHT*TILESIZE + 20))
        placePosition += 50
        # Add the text showing amount in inventory:
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE + 20))
        placePosition += 80

    # Display player in correct position:
    DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
    # update the display:
    pygame.display.update()
    fpsClock.tick(24)