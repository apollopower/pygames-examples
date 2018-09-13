import pygame

def main():
    
    # Initialize pygame module:
    pygame.init()
    # load window:
    pygame.display.set_caption("Test")

    # Creating a surface on screen with size 800x600
    screen = pygame.display.set_mode((800,600))

    running = True

    # Main loop:
    while running:
        # Even handling eventqueue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Change value to false, exit main loop
                running = False
    
# Run the main function if module is executed as main script:

if __name__ == "__main__":
    # Call main function:
    main()