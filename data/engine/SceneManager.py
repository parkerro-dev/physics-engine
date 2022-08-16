import pygame
import numpy

from .SceneBody import SceneBody

class SceneManager():
    def __init__(self):
        self.SceneBodies = []
    
    def addSceneBody(self, body, active = True):
        self.SceneBodies.append(SceneBody(body, active))
        body.setID(id=len(self.SceneBodies))

    def removeSceneBody(self, id):
        pass

    def SceneLoop(self):
        for bodies in self.SceneBodies:
            bodies.body.makeBody()