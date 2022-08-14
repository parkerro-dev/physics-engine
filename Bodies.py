import pygame

import numpy

class RigidSurface():
    def __init__(self, id,surface, startCoord, endCoord, CollisionEngine, collider = True):
        self.id = id
        self.surface = surface
        self.startCoord = startCoord
        self.endCoord = endCoord                                                                                            
        self.CollisionEngine = CollisionEngine                                                                                     
        self.collider = collider
    
    def makeBody(self):
        pygame.draw.rect(self.surface, (255, 255, 255), (self.startCoord, self.endCoord))
        if self.collider:
            self.makeCollider()
    
    def makeCollider(self):
        self.CollisionEngine.newColliderBody()
