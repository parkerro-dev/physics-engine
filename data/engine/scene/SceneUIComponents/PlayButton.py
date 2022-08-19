import pygame

from data.ui.uiMakers.TextMaker import TextMaker

class Button:
    def __init__(self, text, textLocation, surface, location, UIManager, parent):
        self.surface = surface
        self.location = location
        self.UIManager = UIManager
        self.textMaker = TextMaker()
        self.text = text
        self.textLocation = textLocation
        self.parent = parent
        self.makeButton()

    def makeButton(self):
        buttonSurfaceSize = (self.location[1][0]-self.location[0][0], self.location[1][1]-self.location[0][1] )
        self.buttonSurface = pygame.Surface(buttonSurfaceSize)
        self.ButtonUIObject = self.UIManager.makeNewUIObject("{text}Button".format(text = self.text), self, self.location, 3)
    
    def OnClick(self):
        self.parent.OnClick(self)

    def buttonLoop(self):
        self.surface.blit(self.buttonSurface, self.location)
        pygame.draw.rect(self.buttonSurface, (150, 150, 150), (0, 0, self.buttonSurface.get_width(), self.buttonSurface.get_height()), 1, 1)
        self.textMaker.makeText(self.buttonSurface, self.text, self.textLocation[0], self.textLocation[1])