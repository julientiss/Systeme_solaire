import random

import pygame
from pygame.math import Vector2


class planetes :
    def __init__(self,largeur=1400,longueur=800):

        self.rayon = 5
        self.couleur = (random.randint(0,255)), random.randint(0,255), random.randint(0,255)
        self.position = Vector2(random.randint(0,1400),random.randint(0,800))
        self.nom = "planetes"

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
    def dead(self):
        self.nom