
from .Bodies import Particle, RigidSurface


class BodyManager():
    def __init__(self, engineSurface, sceneManager, blockSize, coordSys):
     self.engineSurface = engineSurface
     self.sceneManager = sceneManager
     self.blockSize = blockSize
     self.coordSys = coordSys
     self.UIManager = None
     self.RigidSurfaceCounter = 0
     self.ParticleCounter = 0
     self.CollisionEngine = None
    

    def makeRigidSurface(self, startCoord, endCoord, collider = True):
        rigidSurface = RigidSurface(self.engineSurface, startCoord, endCoord, self.blockSize, self.coordSys, self.CollisionEngine, collider = True)
        rigidSurface.makeCollider()
        self.RigidSurfaceCounter += 1
        self.UIManager.makeNewUIObject("Surface{counter}".format(counter = self.RigidSurfaceCounter), rigidSurface, rigidSurface.locationValues(), 3, True)
        self.sceneManager.addSceneBody(rigidSurface)

    def makeParticle(self, position):
        particle = Particle(self.engineSurface, 10, 1, (255,0, 0), position, 0.2, self.coordSys, self.CollisionEngine)
        particle.makeCollider()
        self.ParticleCounter += 1
        self.UIManager.makeNewUIObject("Particle{counter}".format(counter = self.ParticleCounter), particle, particle.locationValues(), 3, True)
        particle.name = "Particle{counter}".format(counter = self.ParticleCounter)
        self.sceneManager.addSceneBody(particle)