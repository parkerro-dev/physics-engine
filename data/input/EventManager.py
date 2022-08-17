
import pygame

class EventManager():
    def __init__(self, console, coordSys, BodyManager, surface):
        self.name = "Event Manager"
        self.console = console
        self.eventCounter = 0
        self.coordSys = coordSys
        self.BodyManager = BodyManager
        self.surface = surface

    def OnEvent(self, event, type):
        if type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                startPos = (0, 0)
                endPos = (15,5)

                print(startPos, endPos)
                self.console.Log("Rigid Surface made at {startPos}, {endPos}".format(startPos=startPos, endPos=endPos), self.name)
                self.BodyManager.makeRigidSurface(self.surface, startPos, endPos)
