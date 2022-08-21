
from cmath import rect
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
        rectWidth = numpy.abs(self.endCoord[0] - self.startCoord[0])*self.blockSize
        rectHeight = numpy.abs(self.endCoord[1] - self.startCoord[1] )*self.blockSize
        rectHeightOffset = rectHeight/self.blockSize
        print(rectHeight, rectWidth)
        rectValues = (self.coordSys.GetPos(self.startCoord[0], self.startCoord[1]), (rectWidth, rectHeight))
        return rectValues

    def locationValues(self):
        location = (self.coordSys.GetPos(self.startCoord[0], self.startCoord[1]), self.coordSys.GetPos(self.endCoord[0], self.endCoord[1]))
        return location
    
    def makeBody(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.rectInput())
        #if self.collider:
        #   self.makeCollider()
    
    def makeCollider(self):

        self.colliderBody = self.CollisionEngine.newColliderBody((self.startCoord[0]-0.01,self.startCoord[1]-0.01), (self.endCoord[0]+0.01, self.endCoord[1]+0.01))

    def isColliding(self):
        print(self.CollisionEngine.checkCollision(self.colliderBody))
        if self.CollisionEngine.checkCollision(self.colliderBody) == []:
            return False

        return True
    
    def setID(self, id):
        self.id = id
    
    def getID(self):
        return self.id

class Particle:
    def __init__(self, surface, size, mass, color, position, friction, coordSys, CollisionEngine):
        self.surface = surface
        self.size = size
        self.mass = mass
        self.color = color
        self.position = position
        self.friction = friction
        self.coordSys = coordSys
        self.velocityX = 0
        self.velocityY = 0
        self.id = None
        self.CollisionEngine = CollisionEngine
        self.startCoord = self.coordSys.GetCoord(self.position[0], self.position[1])
        self.endCoord = self.coordSys.GetCoord(self.position[0]+self.size, self.position[1]+self.size)


    def locationValues(self):
        location = (self.position, (self.position[0]+self.size, self.position[1]+self.size))
        return location

    def setID(self, id):
        self.id = id
    
    def getID(self):
        return self.id

    def getPositionPos(self):
       #get position on screen instead of coordsys
       positionPos = (self.coordSys.GetPos(self.position[0], self.position[1]))
       return positionPos
    
    def makeBody(self):
        pygame.draw.rect(self.surface, self.color, ((self.position), (self.size, self.size)))
        self.collider.updateCollider((self.startCoord[0]-0.01,self.startCoord[1]-0.01), (self.endCoord[0]+0.01,self.endCoord[1]+0.01))

    def makeCollider(self):
    
        self.collider = self.CollisionEngine.newColliderBody((self.startCoord[0]-0.01,self.startCoord[1]-0.01), (self.endCoord[0]+0.01,self.endCoord[1]+0.01))

    def isColliding(self):
        print(self.CollisionEngine.checkCollision(self.collider))
        if self.CollisionEngine.checkCollision(self.collider) == []:
            return False

        return True