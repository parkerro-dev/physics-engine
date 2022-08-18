
from .Bodies import RigidSurface


class BodyManager():
    def __init__(self, engineSurface, sceneManager, blockSize, coordSys):
     self.engineSurface = engineSurface
     self.sceneManager = sceneManager
     self.blockSize = blockSize
     self.coordSys = coordSys
     self.UIManager = None
     self.RigidSurfaceCounter = 0
    

    def makeRigidSurface(self, startCoord, endCoord, CollisionEngine=None, collider = True):
        rigidSurface = RigidSurface(self.engineSurface, startCoord, endCoord, self.blockSize, self.coordSys, CollisionEngine, collider = True)
        self.RigidSurfaceCounter += 1
        self.UIManager.makeNewUIObject("Surface{counter}".format(counter = self.RigidSurfaceCounter), rigidSurface, rigidSurface.locationValues(), 3, True)
        self.sceneManager.addSceneBody(rigidSurface)