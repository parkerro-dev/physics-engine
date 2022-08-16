
from .Bodies import RigidSurface


class BodyManager():
    def __init__(self, sceneManager):
     self.sceneManager = sceneManager
    

    def makeRigidSurface(self, surface, startCoord, endCoord, CollisionEngine=None, collider = True):
        rigidSurface = RigidSurface(surface, startCoord, endCoord, CollisionEngine, collider = True)
        self.sceneManager.addSceneBody(rigidSurface)