import pygame
from data.ui.uiMakers.TextMaker import TextMaker

class TextEngine():
    def __init__(self, coordSys, surface, width, height):
        pygame.font.init()
        if pygame.font.get_init():
            self.TextMaker = TextMaker()

        self.coordSys = coordSys
        self.globalSurface = surface
        self.width = width
        self.height = height
    
    def TextLoop(self):
        self.mousePos = pygame.mouse.get_pos()
        self.mouseCoords = self.coordSys.GetCoord(self.mousePos[0], self.mousePos[1])
        self.mouseCoordsString = ''.join(str(self.mouseCoords))

    def TextRender(self):
        self.TextMaker.makeText(self.globalSurface, "My Physics Engine v0.0.1", 0, 0)
        self.TextMaker.makeText(self.globalSurface, self.mouseCoordsString, self.width-75, self.height-10)
        