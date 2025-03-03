import pygame
import sys
from asteroidfield import *
from constants import *
from player import *
from circleshape import *
from asteroid import *
from shot import *

def main():
    # Define Screen with width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Shot.containers = (shot, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Create player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create Asteroid Field
    asteroidfield = AsteroidField()

    # Main Loop
    while True:
        # Checks if user closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen solid black
        screen.fill((0,0,0))
        # update sprites
        for item in updatable:
            item.update(dt)
        # Check for collision
        for item in asteroids:
            if player.collision(item):
                print("Game over!")
                sys.exit()
            for bullet in shot:
                if bullet.collision(item):
                    item.split()
                    bullet.kill()
        # Draw sprites
        for item in drawable:
            item.draw(screen)
        # Update Screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
