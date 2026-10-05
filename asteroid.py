import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first = self.velocity.rotate(angle)
            second = self.velocity.rotate(-angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, self.radius)
            ast1.velocity = first
            ast2 = Asteroid(self.position.x, self.position.y, self.radius)
            ast2.velocity = second
            ast1.velocity *= 1.2
            ast2.velocity *= 1.2
