from pygame.math import Vector2
import core
import pygame
import random
from Ball_C import Ball
from Ennemi_C import Ennemi
from Joueur_C import Joueur


class Ball_C(Ball):
    pass
class Ennemi_C(Ennemi):
    pass
class Joueur_C(Joueur):
    pass

def setup():
    print("Setup START---------")

    core.memory("L", 1000)
    core.memory("H", 600)

    core.fps = 30
    core.WINDOW_SIZE = [core.memory("L"), core.memory("H")]

    core.memory("Ball")
    core.memory("Joueur")
    core.memory("Ennemi")

    for i in range(1):
        core.memory("Ball").append(Ball_C())

    for i in range(1):
        core.memory("Ennemi").append(Ennemi_C())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    for Ball in core.memory("Ball"):
        Ball.draw(core.WINDOW_SIZE)

    for Ennemi in core.memory("Ennemi"):
        Ennemi.draw(core.screen)
        Ennemi.move()

    core.memory("Joueur").draw()
    core.memory("Joueur").move()



    print("RUN")

core.main(setup, run)
