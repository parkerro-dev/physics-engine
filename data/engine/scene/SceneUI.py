import pygame

from data.engine.scene.SceneUIComponents.EngineMenu import EngineMenu

class SceneUi():
    def __init__(self, engineSurface, console):
        self.engineSurface = engineSurface
        self.console = console
        self.UIManager = None
        self.EngineMenu = EngineMenu(self.engineSurface, self.console)
        
   
    def On_Init(self):
        self.EngineMenu.UIManager = self.UIManager
   
    def SceneUILoop(self):
        self.EngineMenu.menuLoop()

