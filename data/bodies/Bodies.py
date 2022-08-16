import pygame

import numpy

class RigidSurface():
    def __init__(self, surface, startCoord, endCoord, CollisionEngine=None, collider = True):
        self.id = None
        self.surface = surface
        self.startCoord = startCoord
        self.endCoord = endCoord                                                                                            
        self.CollisionEngine = CollisionEngine                                                                                     
        self.collider = collider
    
    def makeBody(self):
        pygame.draw.rect(self.surface, (255, 255, 255), (self.startCoord, self.endCoord))
        #if self.collider:
        #   self.makeCollider()
    
    def makeCollider(self):
        self.CollisionEngine.newColliderBody()

    def setID(self, id):
        self.id = id
    
    def getID(self):
        return self.id
