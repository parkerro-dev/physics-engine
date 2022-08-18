
from re import L
import pygame
import numpy

from ...ui.uiMakers.TextMaker import TextMaker

from .SceneBody import SceneBody

class SceneManager():
    def __init__(self, hierarchySurface, console, engineSurface):
        self.SceneBodies = []
        self.console = console
        self.hierarchySurface = hierarchySurface
        self.engineSurface = engineSurface
        self.textManager = TextMaker()
        self.UIManager = None
        self.menuActive = False
        self.menuSurface = pygame.Surface((80, 100))
        self.mousePos = None
        self.menuUiObject = None

    
    def addSceneBody(self, body, active = True):
        self.SceneBodies.append(SceneBody(body, active))
        body.setID(id=len(self.SceneBodies))

    def removeSceneBody(self, id):
        pass

    def hierarchyUI(self):
        # Outline
        pygame.draw.rect(self.hierarchySurface, (200,200,200), (3, 0, self.hierarchySurface.get_width()-5, self.hierarchySurface.get_height()-5), 2)

        # title
        self.textManager.makeText(self.hierarchySurface, "Hierarchy", 5, 5)

        # list bodies

    def engineRMBMenu(self):
        self.console.Log("We are making u a nice lil menu", self)
        self.mousePos = pygame.mouse.get_pos()
        self.menuUiObject = self.UIManager.makeNewUIObject("engineMenu", self.menuSurface, ((self.mousePos[0]+10, self.mousePos[1]+10), (self.mousePos[0]+90, self.mousePos[1]+110)), 2,)
        self.UIManager.hoverOverObjects.append(self.menuUiObject) 
        print(self.UIManager.hoverOverObjects)
        self.menuActive = True
    
    def engineRMBMenuClose(self):
        self.menuActive = False
        self.UIManager.removeUiObject(self.menuUiObject)
        self.menuUiObject = None

    def SceneLoop(self):
        self.hierarchyUI()
        for bodies in self.SceneBodies:
            bodies.body.makeBody()
            id = bodies.body.getID()
            self.textManager.makeText(self.hierarchySurface, "- Body {id}".format(id = id), 10, 5+(12*(id)))

        if self.menuActive:
            self.engineSurface.blit(self.menuSurface, self.mousePos)
            self.menuSurface.fill((255, 0, 0))
            if self.menuUiObject not in self.UIManager.hoverOverObjects:
                 self.engineRMBMenuClose()


        
           