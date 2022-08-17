
import numpy
import pygame

from ..console.Console import Console

from ..bodies.BodyManager import BodyManager

from ..input.EventManager import EventManager

from .scene.SceneManager import SceneManager

from ..ui.TextEngine import TextEngine

from .coordinate.CoordinateSystem import CoordSys

from ..ui.UiManager import UiManager

class Engine():
    def __init__(self, globalSurface, engineSurface, hierarchySurface, consoleSurface, width, height, blockSize):
        self.globalSurface = globalSurface
        self.engineSurface = engineSurface
        self.hierarchySurface = hierarchySurface
        self.consoleSurface = consoleSurface
        
        self.console = Console(self.consoleSurface)
        self.coordSys = CoordSys(self.engineSurface, width, height, blockSize)
       
        self.width = width
        self.height = height
        self.blockSize = blockSize

        
        self.TextEngine = TextEngine(self.coordSys, self.engineSurface, self.width, self.height)
        self.UIManager = UiManager(self.EventManager)
        self.SceneManager = SceneManager(self.hierarchySurface)
        self.BodyManager = BodyManager(self.SceneManager)
        self.EventManager = EventManager(self.console, self.coordSys, self.BodyManager, self.engineSurface)
        

    def EngineEvent(self, event):
        self.EventManager.OnEvent(event, event.type)
    
    def EngineLoop(self):

         #blitzing
        self.globalSurface.blit(self.engineSurface, (0, 0))
        self.globalSurface.blit(self.hierarchySurface, (self.engineSurface.get_width(), 0))
        self.globalSurface.blit(self.consoleSurface, (0, self.engineSurface.get_height()))
        
        #Console
        self.console.OnLoop()

        #draw coord sys
        self.coordSys.Grid()

        

        #text
        self.TextEngine.TextLoop()

        
        
    def EngineRender(self):
       
        # text
        self.TextEngine.TextRender()

        self.SceneManager.SceneLoop()


