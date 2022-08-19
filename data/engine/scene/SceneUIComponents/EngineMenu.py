import pygame

from data.ui.UiManager import UiManager
from ....ui.uiMakers.TextMaker import TextMaker

class EngineMenu():
    def __init__(self, engineSurface: pygame.Surface, console, UIManager):
        self.engineSurface = engineSurface
        self.UIManager = UIManager
        self.console = console
        self.textMaker = TextMaker()
        self.menuActive = False
        self.menuWidth = 90
        self.menuHeight = 100
        self.menuSurface = pygame.Surface((self.menuWidth, self.menuHeight))
        self.mousePos = None
        self.menuUiObject = None


    def createMenu(self):
        self.console.Log("We are making u a nice lil menu", self)

        self.mousePos = pygame.mouse.get_pos()

        self.menuUiObject = self.UIManager.makeNewUIObject("engineMenu", self.menuSurface, ((self.mousePos[0]-10, self.mousePos[1]-10), (self.mousePos[0]+100, self.mousePos[1]+110)), 2,)
        
        self.menuUiObject.isMouseHovering = True
        # adds itself to the hover items so it doesnt close immediately
        self.UIManager.hoverOverObjects.append(self.menuUiObject) 
        
        self.menuActive = True

        self.UIManager.makeNewUIObject("makeSurfaceOption", self.menuUiObject, ((self.mousePos), (self.mousePos[0] + self.menuSurface.get_width(), self.mousePos[1]+20)), 3)

    def createMenuOptions(self):
            self.makeSurfaceOption = self.textMaker.makeText(self.menuSurface, "Make Surface", 1, 1)
    
    def closeMenu(self):
        self.menuActive = False
        self.UIManager.removeUiObject(self.menuUiObject)
        if self.menuUiObject in self.UIManager.hoverOverObjects:
            self.UIManager.hoverOverObjects.remove(self.menuUiObject)
        self.menuUiObject = None

    def menuLoop(self):
        if self.menuActive:
            self.engineSurface.blit(self.menuSurface, self.mousePos)
            self.menuSurface.fill((0, 0, 0))
            pygame.draw.rect(self.menuSurface, (200, 200, 200), (0, 0, self.menuSurface.get_width(), self.menuSurface.get_height()), 1)

            self.createMenuOptions()
            if self.menuUiObject.isMouseHovering == False:
                self.closeMenu()
