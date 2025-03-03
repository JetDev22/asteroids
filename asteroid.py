from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            offsetAngle = random.uniform(20, 50)
            newVel1 = self.velocity.rotate(offsetAngle)
            newVel2 = self.velocity.rotate(-offsetAngle)
            newRad = self.radius - ASTEROID_MIN_RADIUS
            newAst1 = Asteroid(self.position[0], self.position[1], newRad)
            newAst2 = Asteroid(self.position[0], self.position[1], newRad)
            newAst1.velocity = newVel1 * 1.2
            newAst2.velocity = newVel2 * 1.2
            self.kill()
