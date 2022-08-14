import pygame
import numpy

class CollisionEngine():
    def __init__(self, bodies):
        self.bodies = bodies

    def newColliderBody(self):
        self.bodies.append(2)