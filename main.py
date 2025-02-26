import pygame
from constants import *

def main():
    # Define Screen with width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main Loop
    while True:
        # Checks if user closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen solid black
        screen.fill((0,0,0))
        # Update Screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
