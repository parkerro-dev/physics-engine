
from .Bodies import RigidSurface


class BodyManager():
    def __init__(self, sceneManager, blockSize, coordSys):
     self.sceneManager = sceneManager
     self.blockSize = blockSize
     self.coordSys = coordSys
    

    def makeRigidSurface(self, surface, startCoord, endCoord, CollisionEngine=None, collider = True):
        rigidSurface = RigidSurface(surface, startCoord, endCoord, self.blockSize, self.coordSys, CollisionEngine, collider = True)
        self.sceneManager.addSceneBody(rigidSurface)