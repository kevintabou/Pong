from pygame.math import Vector2
import core
import pygame
import random
import math

class Ball:

    def __init__(self):

        self.centredecercle = pygame.Vector2(200, 200)
        self.centredecercle = pygame.Vector2(self.centredecercle.x, self.centredecercle.y)
        self.rayonducercle = 10
        self.couleurducercle = (255, 255, 255)
        self.vitesse = pygame.Vector2(0, 0)
        self.gravity_x = 0
        self.gravity_y = 0

    def draw (self):
        pygame.draw.circle(core.screen, self.couleurducercle, self.centredecercle,  self.rayonducercle)

    def move(self):

        print("fct move")

        # Hors limite X
        if self.centredecercle.x > core.WINDOW_SIZE[0] - self.rayonducercle:
            self.gravity_x = -5
            self.vitesse = self.vitesse - self.vitesse
            self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.centredecercle.x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_x = 5
            self.vitesse = self.vitesse - self.vitesse
            self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Hors limite Y
        if self.centredecercle.y > core.WINDOW_SIZE[1] - self.rayonducercle:
            self.gravity_y = -5
            self.vitesse = self.vitesse - self.vitesse
            self.couleurducercle, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.centredecercle.y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_y = 5
            self.vitesse = self.vitesse - self.vitesse
            self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Reset
        if core.getKeyPressList("r"):
            self.centredecercle = pygame.Vector2(200, 200)
            self.gravity_x = 0
            self.gravity_y = 0
            self.vitesse = Vector2(0, 0)
            print("reset")
