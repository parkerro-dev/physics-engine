
from re import S
import pygame
import numpy

from data.engine.scene.SceneUI import SceneUi

from ...ui.uiMakers.TextMaker import TextMaker

from .SceneBody import SceneBody
'''
This class should only have one instance and it is used to manage the bodies in the engine scene
It has its own object type called SceneBody, scenebodies are used as a way to reference bodies objects which
are in the scene while not directly affecting them, its like a middle man that makes the code
safer on a UI level
'''
class SceneManager():
    def __init__(self, sidePanelSurface, console, engineSurface, Colors):
        self.SceneBodies = []
        self.Colors = Colors
        self.console = console
        self.sidePanelSurface = sidePanelSurface
        self.engineSurface = engineSurface
        self.textManager = TextMaker()
        self.UIManager = None
        self.PhysicsEngine = None
        self.selectedSceneBody = None

    def On_Init(self):
        self.SceneUI = SceneUi(self.engineSurface, self.UIManager, self.console, self.PhysicsEngine, self.Colors)

    
    def addSceneBody(self, body, active = True):
        self.SceneBodies.append(SceneBody(body, active))
        body.setID(id=len(self.SceneBodies))

    def removeSceneBody(self, id):
        pass

    def SceneLoop(self):
        for bodies in self.SceneBodies:
            bodies.body.makeBody()
            #checks if body has become selected
            if bodies.body.selected:
                #checks if theres already a selected body if there is it sets its selected property to false
                if self.selectedSceneBody is not bodies:
                    if self.selectedSceneBody is not None:
                        self.selectedSceneBody.body.selected = False
                    self.selectedSceneBody = bodies  
                    self.console.Log("You've selected this {bodies}".format(bodies = self.selectedSceneBody), self)
            
            if bodies.body.isColliding():
                self.console.Log("Collider alert!!", bodies)
            
        self.SceneUI.SceneUILoop()

        
           