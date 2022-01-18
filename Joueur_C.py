from pygame.math import Vector2
import core
import pygame
import random
from pygame import draw
import math

class Joueur:

    def __init__(self):

        self.vitesse = pygame.Vector2(0, 0)
        self.gravity_x = 0
        self.gravity_y = 0

        pygame.init()

        surface = pygame.display.set_mode((400, 300))
        color = (255, 255, 255)
        core.draw.rect(255, 255,2555 , 30, 30, 3, 60)
        pygame.draw.rect(surface, color, pygame.Rect(30, 30, 3, 60))
        pygame.display.flip()

    def move (self):

        # Hors limite Y
        if self.rectangle.y > core.WINDOW_SIZE[1] - self.rayonducercle:
            self.gravity_y = -5
            self.vitesse = self.vitesse - self.vitesse
            self.color, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.rectangle.y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_y = 5
            self.vitesse = self.vitesse - self.vitesse
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Hors limite X
        if self.rectangle.x > core.WINDOW_SIZE[0] - self.rayonducercle:
            self.gravity_x = -5
            self.vitesse = self.vitesse - self.vitesse
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.rectangle.x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_x = 5
            self.vitesse = self.vitesse - self.vitesse
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Reset
        if core.getKeyPressList("r"):
            self.rectangle = pygame.Vector2(200, 200)
            self.gravity_x = 0
            self.gravity_y = 0
            self.vitesse = Vector2(0, 0)
            print("reset")

         # Up
        #if core.getKeyPressList("z"):
          #  self.gravity_y = -5
           # print("up")
        # Down
       # if core.getKeyPressList("s"):
         #   self.gravity_y = 5
          #  print("down")

        # Right
        #if core.getKeyPressList("d"):
         #   self.gravity_x = 5
          #  print("right")

        # Left
        #if core.getKeyPressList("q"):
         #   self.gravity_x = -5
         #   print("left")

        # Souris
        if core.getMouseLeftClick() is not None:
            self.PS = pygame.Vector2(0, 0)
            self.k = 0.003
            self.l0 = 1
            self.u = 10
            self.pos_souris = pygame.Vector2(0, 0)

            # Pos souris
            self.pos_souris = pygame.Vector2(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1])

            # Vecteur pos_souris - pos_cercle
            self.PS = pygame.Vector2(self.pos_souris.x - self.rectangle.x,
                                     self.pos_souris.y - self.rectangle.y)

            # Norme vecteur PS
            self.l = self.PS.length()

            # Longueur vecteur PS
            self.u = self.PS.normalize()

            # Calcul Force finale
            self.Fr = self.k * abs(self.l - self.l0) * self.u
            print(self.Fr)

            # Vitesse = vitesse + force
            self.vitesse = self.vitesse + self.Fr

            # pos_cercle = pos_cercle + vitesse
        self.rectangle = self.rectangle + self.vitesse

        self.rectangle = pygame.Vector2(self.rectangle.x + self.gravity_x,
                                             self.rectangle.y + self.gravity_y)

        print("rectangle")