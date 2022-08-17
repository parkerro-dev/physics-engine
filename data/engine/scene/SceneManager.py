
import pygame
import numpy

from ...ui.uiMakers.TextMaker import TextMaker

from .SceneBody import SceneBody

class SceneManager():
    def __init__(self, surface):
        self.SceneBodies = []
        self.surface = surface
        self.textManager = TextMaker()

    
    def addSceneBody(self, body, active = True):
        self.SceneBodies.append(SceneBody(body, active))
        body.setID(id=len(self.SceneBodies))

    def removeSceneBody(self, id):
        pass

    def hierarchyUI(self):
        # Outline
        pygame.draw.rect(self.surface, (200,200,200), (3, 0, self.surface.get_width()-5, self.surface.get_height()-5), 2)

        # title
        self.textManager.makeText(self.surface, "Hierarchy", 5, 5)

        # list bodies

        

    def SceneLoop(self):
        self.hierarchyUI()
        for bodies in self.SceneBodies:
            bodies.body.makeBody()
            id = bodies.body.getID()
            self.textManager.makeText(self.surface, "- Body {id}".format(id = id), 10, 5+(12*(id)))