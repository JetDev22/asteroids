import pygame
from constants import *

def main():
    # Define Screen with width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set FPS
    clock = pygame.time.Clock()
    dt = 0

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
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
