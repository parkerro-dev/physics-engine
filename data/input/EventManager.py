import pygame

class EventManager():
    def __init__(self, coordSys, BodyManager, surface):
        self.eventCounter = 0
        self.coordSys = coordSys
        self.BodyManager = BodyManager
        self.surface = surface

    def OnEvent(self, event, type):
        if type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                startPos = self.coordSys.GetPos(0, 0)
                endPos = (20,50)

                print(startPos, endPos)
                self.BodyManager.makeRigidSurface(self.surface, startPos, endPos)
