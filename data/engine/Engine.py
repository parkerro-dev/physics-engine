
import numpy
import pygame

from data.engine.PhysicsEngine.PhysicsEngine import PhysicsEngine
from data.engine.collision.CollisionEngine import CollisionEngine
from data.ui.sidePanel.SidePanel import SidePanel

from ..console.Console import Console

from ..bodies.BodyManager import BodyManager

from ..input.EventManager import EventManager

from .scene.SceneManager import SceneManager

from ..ui.TextEngine import TextEngine

from .coordinate.CoordinateSystem import CoordSys

from ..ui.UiManager import UiManager

class Engine():
    def __init__(self, globalSurface, engineSurface, sidePanelSurface, consoleSurface, width, height, blockSize):
        self.globalSurface = globalSurface
        self.engineSurface = engineSurface
        self.sidePanelSurface = sidePanelSurface
        self.consoleSurface = consoleSurface
        
        self.console = Console(self.consoleSurface)
        self.coordSys = CoordSys(self.engineSurface, width, height, blockSize)
       
        self.width = width
        self.height = height
        self.blockSize = blockSize

        
        self.TextEngine = TextEngine(self.coordSys, self.engineSurface, self.width, self.height)
        
        self.SceneManager = SceneManager(self.sidePanelSurface, self.console, self.engineSurface)
        self.BodyManager = BodyManager(self.engineSurface, self.SceneManager, self.blockSize,  self.coordSys)
        self.EventManager = EventManager(self.console, self.coordSys, self.BodyManager, self.engineSurface)
        
        self.UIManager = UiManager(self.console, self.SceneManager, self.BodyManager)
        self.SidePanel = SidePanel(self.sidePanelSurface, self.engineSurface, self.UIManager, self.SceneManager)

        self.PhysicsEngine = PhysicsEngine(self.coordSys, self.console, self.BodyManager, self.SceneManager)
        self.CollisionEngine = CollisionEngine()

        self.UIManager.makeNewUIObject("EngineSurface" , self.engineSurface, ((0, 0), (self.engineSurface.get_width(), self.engineSurface.get_height())), 1, False)
        self.UIManager.makeNewUIObject("sidePanelSurface", self.sidePanelSurface, ((self.engineSurface.get_width(), 0), (self.globalSurface.get_width(), self.engineSurface.get_height())), 1, False)
        self.UIManager.makeNewUIObject("ConsoleSurface" ,self.consoleSurface, ((0, self.engineSurface.get_height()), (self.globalSurface.get_width(), self.globalSurface.get_height())), 1, False)
        print(self.UIManager.UiObjects)

        self.SceneManager.UIManager = self.UIManager
        self.BodyManager.UIManager = self.UIManager
        self.BodyManager.CollisionEngine = self.CollisionEngine
        self.SceneManager.PhysicsEngine = self.PhysicsEngine
        self.On_Init()


    def On_Init(self):
        #this is used to set the object in different classes
        self.SceneManager.On_Init()

    def EngineEvent(self, event):
        self.EventManager.OnEvent(event, event.type)
        self.UIManager.onEvent(event)
    
    def EngineLoop(self):

        #blitzing and intialising surface UI objects
        #Engine Surface
        self.globalSurface.blit(self.engineSurface, (0, 0))
        self.engineSurface.fill((0,0,0))
        #Scene Manager / sidePanel Surface
        self.globalSurface.blit(self.sidePanelSurface, (self.engineSurface.get_width(), 0))

        #Console Surface
        self.globalSurface.blit(self.consoleSurface, (0, self.engineSurface.get_height()))


        #Console
        self.console.OnLoop()

        #draw coord sys
        self.coordSys.Grid()

        #UI Manager
        self.UIManager.OnLoop()

        #text
        self.TextEngine.TextLoop()

        #side panel
        self.SidePanel.OnLoop()

        #physics
        self.PhysicsEngine.OnPhysicsLoop()

        
        
    def EngineRender(self):
       
        # text
        self.TextEngine.TextRender()

        self.SceneManager.SceneLoop()
