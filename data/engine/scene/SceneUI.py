import pygame

from data.engine.scene.SceneUIComponents.EngineMenu import EngineMenu
from data.engine.scene.SceneUIComponents.Button import Button

class SceneUi():
    def __init__(self, engineSurface, UIManager ,console, PhysicsEngine):
        self.engineSurface = engineSurface
        self.console = console
        self.UIManager = UIManager
        self.PhysicsEngine = PhysicsEngine
        
        self.On_Init()
        
   
    def On_Init(self):
        self.EngineMenu = EngineMenu(self.engineSurface, self.console, self.UIManager)
        self.PlayButton = Button("play", (5, 5), self.engineSurface, ((25, self.engineSurface.get_height()-25), (60, self.engineSurface.get_height()-5)), ((25, self.engineSurface.get_height()-25), (60, self.engineSurface.get_height()-5)), self.UIManager, self)
        
        
    def OnClick(self, objectClick):
        if objectClick == self.PlayButton:
            self.console.Log("you pressed play", self)
            self.PhysicsEngine.OnPlay()
   
    def SceneUILoop(self):
        self.EngineMenu.menuLoop()
        self.PlayButton.buttonLoop()

