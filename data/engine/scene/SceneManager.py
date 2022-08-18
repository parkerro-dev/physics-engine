
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
        self.menuSurface = pygame.Surface((90, 100))
        self.menuSurfaceOutline = pygame.Surface((91, 101))
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

        self.menuUiObject = self.UIManager.makeNewUIObject("engineMenu", self.menuSurface, ((self.mousePos[0]-10, self.mousePos[1]-10), (self.mousePos[0]+100, self.mousePos[1]+110)), 2,)
        
        self.menuUiObject.isMouseHovering = True
        # adds itself to the hover items so it doesnt close immediately
        self.UIManager.hoverOverObjects.append(self.menuUiObject) 
        
        self.menuActive = True

        self.UIManager.makeNewUIObject("makeSurfaceOption", self.menuUiObject, ((self.mousePos), (self.mousePos[0] + self.menuSurface.get_width(), self.mousePos[1]+20)), 3)


    def engineMenuOptions(self):
        self.makeSurfaceOption = self.textManager.makeText(self.menuSurface, "Make Surface", 1, 1)


    
    def engineRMBMenuClose(self):
        self.menuActive = False
        self.UIManager.removeUiObject(self.menuUiObject)
        if self.menuUiObject in self.UIManager.hoverOverObjects:
            self.UIManager.hoverOverObjects.remove(self.menuUiObject)
        self.menuUiObject = None

    def SceneLoop(self):
        self.hierarchyUI()
        for bodies in self.SceneBodies:
            bodies.body.makeBody()
            id = bodies.body.getID()
            self.textManager.makeText(self.hierarchySurface, "- Body {id}".format(id = id), 10, 5+(12*(id)))

        if self.menuActive:
            self.engineSurface.blit(self.menuSurface, self.mousePos)
            self.menuSurface.fill((0, 0, 0))
            pygame.draw.rect(self.menuSurface, (200, 200, 200), (0, 0, self.menuSurface.get_width(), self.menuSurface.get_height()), 1)

            self.engineMenuOptions()
            if self.menuUiObject.isMouseHovering == False:
                self.engineRMBMenuClose()


        
           