import pygame
import numpy

class TextMaker():
    def __init__(self):
        self.Font = pygame.font.Font("myFont.ttf", 20)

    def makeText(self, surface, text, posX, posY, color=(255,255,255), bgColor = (0, 0, 0), fillSurfaceWidth = False):
        if fillSurfaceWidth:
            TextSurface = pygame.Surface((surface.get_width()-1, 20))
            TextSurface.fill(bgColor)
            textToMake = pygame.font.Font.render(self.Font, text, True, color, bgColor)
            
            TextSurface.blit(textToMake, (0, 0))
            surface.blit(TextSurface, (posX, posY))
        else:
            textToMake = pygame.font.Font.render(self.Font, text, True, color, bgColor)
            surface.blit(textToMake, (posX, posY))
        return