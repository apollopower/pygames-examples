# Constants representing different resources:

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# A list representing a tilemap:
tilemap = [
    [GRASS, COAL, DIRT],
    [WATER, WATER, GRASS],
    [COAL, GRASS, WATER],
    [DIRT, GRASS, COAL],
    [GRASS, WATER, DIRT]
]

# Constants representing colors:
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# A dictionary linking resources to colors:
colors = {
    DIRT: BROWN,
    GRASS: GREEN,
    WATER: BLUE,
    COAL: BLACK
}