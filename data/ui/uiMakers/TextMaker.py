import pygame
import numpy

class TextMaker():
    def __init__(self):
        self.Font = pygame.font.Font("myFont.ttf", 20)

    def makeText(self, surface, text, posX, posY, color=(255,255,255), bgColor = (0, 0, 0)):
        textToMake = pygame.font.Font.render(self.Font, text, True, color, bgColor)
        surface.blit(textToMake, (posX, posY))
        return