import pygame
from settings import *

class Simulation:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        # Sprite Groups
        self.static_objects = pygame.sprite.Group()
        self.moving_objects = pygame.sprite.Group()
        # 1 Dimensional Plane
        self.plane = StaticObject((100,600), (2000,5),self.static_objects)
        self.wall = StaticObject((100,100), (5,500),self.static_objects)
        # Colliding Cubes
        self.cube1 = MovingObject((600,self.plane.rect[1]), (255,0,0), 1, (50,50), 0, self.moving_objects)
        self.cube2 = MovingObject((800,self.plane.rect[1]), (0,255,0), 10, (100,100), -1, self.moving_objects)
        # Collision counter
        self.collision_count = 0
        self.text_surf = pygame.font.SysFont("Arial", 30).render("Collisions: {}".format(self.collision_count), True, (255,255,255))
        self.text_rect = self.text_surf.get_rect(topleft=(10,10))

    def check_collision(self):
        for sprite in self.static_objects:
            if self.cube1.rect.colliderect(sprite.rect) or self.cube2.rect.colliderect(sprite.rect) or self.cube1.rect.colliderect(self.cube2.rect):
                self.collision_count += 1
                self.text_surf = pygame.font.SysFont("Arial", 30).render("Collisions: {}".format(self.collision_count), True, (255,255,255))
                self.text_rect = self.text_surf.get_rect(topleft=(10,10))

    def run(self):
        self.display_surface.blit(self.plane.image, self.plane.rect)
        self.display_surface.blit(self.wall.image, self.wall.rect)
        self.display_surface.blit(self.cube1.image, self.cube1.rect)
        self.display_surface.blit(self.cube2.image, self.cube2.rect)
        self.display_surface.blit(self.text_surf, self.text_rect)
        self.moving_objects.update(self.static_objects, self.moving_objects)
        self.check_collision()


class StaticObject(pygame.sprite.Sprite):
    def __init__(self, pos, size, group):
        super().__init__(group)
        self.image = pygame.Surface(size)
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft=pos)


class MovingObject(pygame.sprite.Sprite):
    def __init__(self, pos, color, mass, size, velocity, group):
        super().__init__(group)
        self.image = pygame.Surface(size)
        self.image.fill((color))
        self.rect = self.image.get_rect(bottomleft=pos)
        self.mass = mass
        self.velocity = velocity
        self.momentum = self.mass * self.velocity

    def update(self, static_objects, moving_objects):
        self.rect.x += self.velocity
        for sprite in static_objects:
            if self.rect.colliderect(sprite.rect):
                self.velocity *= -1
        for sprite in moving_objects:
            if self.rect.colliderect(sprite.rect) and self != sprite:
                self.velocity += sprite.momentum / self.mass
                #sprite.velocity += self.momentum / sprite.mass
        self.momentum = self.mass * self.velocity


