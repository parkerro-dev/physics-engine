import pygame
import numpy

from data.engine.collision.ColliderBody import ColliderBody

class CollisionEngine():
    def __init__(self):
        self.Colliders = []

    def newColliderBody(self, startCoords, endCoords):
        colliderBody = ColliderBody(startCoords, endCoords)
        self.Colliders.append(colliderBody)
        return colliderBody

    def checkCollision(self, colliderBody):
        collisions = []
        for colliders in self.Colliders:
            if colliders == colliderBody:
                continue
            else:
                if(colliders.CheckColliding(colliderBody.startCoords, colliderBody.endCoords)):
                    collisions.append(colliders)

            
        return collisions
