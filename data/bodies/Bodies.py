import pygame

import numpy

class RigidSurface():
    def __init__(self, surface, startCoord, endCoord, blockSize, coordSys, CollisionEngine=None, collider = True):
        self.id = None
        self.surface = surface
        self.startCoord = startCoord
        self.endCoord = endCoord                                                                                            
        self.CollisionEngine = CollisionEngine                                                                                     
        self.collider = collider
        self.blockSize = blockSize
        self.coordSys = coordSys

    def rectInput(self):
        rectWidth = (self.endCoord[0] - self.startCoord[0])*self.blockSize
        rectHeight = (self.endCoord[1] - self.startCoord[1] )*self.blockSize

        rectValues = (self.coordSys.GetPos(self.startCoord[0], self.startCoord[1]), (rectWidth, rectHeight))
        return rectValues
    
    def makeBody(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.rectInput())
        #if self.collider:
        #   self.makeCollider()
    
    def makeCollider(self):
        self.CollisionEngine.newColliderBody()

    def setID(self, id):
        self.id = id
    
    def getID(self):
        return self.id

class RigidBody:
    def __init__(self, ):
        pass
