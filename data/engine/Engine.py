
import numpy
import pygame

from ..bodies.BodyManager import BodyManager

from ..input.EventManager import EventManager

from .SceneManager import SceneManager

from .TextEngine import TextEngine

from .CoordinateSystem import CoordSys

class Engine():
    def __init__(self, surface, width, height, blockSize):
        self.coordSys = CoordSys(surface, width, height, blockSize)
        self.surface = surface
        self.width = width
        self.height = height
        self.blockSize = blockSize

        self.TextEngine = TextEngine(self.coordSys, self.surface, self.width, self.height)
        self.SceneManager = SceneManager()
        self.BodyManager = BodyManager(self.SceneManager)
        self.EventManager = EventManager(self.coordSys, self.BodyManager, surface)
    
    def EngineEvent(self, event):
        self.EventManager.OnEvent(event, event.type)
    
    def EngineLoop(self):
        #draw coord sys
        self.coordSys.Grid()

        #text
        self.TextEngine.TextLoop()
        
    def EngineRender(self):
        # text
        self.TextEngine.TextRender()
        self.SceneManager.SceneLoop()


