import pygame
from pygame.math import Vector2
import core
import pygame
from pygame.math import Vector2
import core
from planetes import planetes



def setup():

    print("Setup START---------")
    core.fps = 100
    core.WINDOW_SIZE = [1400, 800]

    core.memory("centredusoleil", Vector2(700,400))
    core.memory("rayondusoleil", 100)
    core.memory("couleurdusoleil", (228, 105, 46))

    core.memory("tableplanetes", [])

    # planetes
    for planetes in range(10):
        core.memory("tableplanetes").append(planetes)

    print("Setup END-----------")



def run():


    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurdusoleil"), core.memory("centredusoleil"), core.memory("rayondusoleil"))

    def run():
        # Variable Local
        core.cleanScreen()

        for c in core.memory("tableplanetes"):
            c.draw(core.screen)





core.main(setup, run)