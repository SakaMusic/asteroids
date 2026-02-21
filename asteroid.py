import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            new_vector_one = self.velocity.rotate(rand_angle)
            new_vector_two = self.velocity.rotate(rand_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = new_vector_one * 1.2
            asteroid_two.velocity = new_vector_two * 1.2