import pygame

from data.ui.uiMakers.TextMaker import TextMaker

class Button:
    def __init__(self, text, textLocation, surface, locationOnScreen, location,UIManager, parent, inverted = False):
        self.surface = surface
        self.location = locationOnScreen
        self.blitLocation = location
        self.UIManager = UIManager
        self.textMaker = TextMaker()
        self.text = text
        self.textLocation = textLocation
        self.parent = parent
        self.inverted = inverted
        self.backgroundColor = (0, 0, 0)
        self.invertedBackgroundColor = (255, 255, 255)
        self.textColor = (255, 255, 255)
        self.invertedTextColor = (0, 0, 0)
        self.makeButton()

    def makeButton(self):
        buttonSurfaceSize = (self.location[1][0]-self.location[0][0], self.location[1][1]-self.location[0][1] )
        self.buttonSurface = pygame.Surface(buttonSurfaceSize)
        self.ButtonUIObject = self.UIManager.makeNewUIObject("{text}Button".format(text = self.text), self, self.location, 3)
    
    def OnClick(self):
        self.parent.OnClick(self)

    def buttonLoop(self):
        self.surface.blit(self.buttonSurface, self.blitLocation)
        if self.inverted:
            self.buttonSurface.fill(self.invertedBackgroundColor)
            pygame.draw.rect(self.buttonSurface, (150, 150, 150), (0, 0, self.buttonSurface.get_width(), self.buttonSurface.get_height()), 1, 1)
            self.textMaker.makeText(self.buttonSurface, self.text, self.textLocation[0], self.textLocation[1], self.invertedTextColor, self.invertedBackgroundColor)

        else:
            self.buttonSurface.fill(self.backgroundColor)
            pygame.draw.rect(self.buttonSurface, (150, 150, 150), (0, 0, self.buttonSurface.get_width(), self.buttonSurface.get_height()), 1, 1)
            self.textMaker.makeText(self.buttonSurface, self.text, self.textLocation[0], self.textLocation[1], self.textColor, self.backgroundColor)

        
