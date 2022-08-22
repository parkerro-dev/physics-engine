
from re import S
import pygame
import numpy

from data.engine.scene.SceneUI import SceneUi

from ...ui.uiMakers.TextMaker import TextMaker

from .SceneBody import SceneBody

class SceneManager():
    def __init__(self, hierarchySurface, console, engineSurface):
        self.SceneBodies = []
        self.console = console
        self.hierarchySurface = hierarchySurface
        self.engineSurface = engineSurface
        self.textManager = TextMaker()
        self.UIManager = None
        self.PhysicsEngine = None

        
        
        
        
    def On_Init(self):
        self.SceneUI = SceneUi(self.engineSurface, self.UIManager, self.console, self.PhysicsEngine)

    
    def addSceneBody(self, body, active = True):
        self.SceneBodies.append(SceneBody(body, active))
        body.setID(id=len(self.SceneBodies))

    def removeSceneBody(self, id):
        pass

    def hierarchyUI(self):
        # Outline
        pygame.draw.rect(self.hierarchySurface, (200,200,200), (3, 0, self.hierarchySurface.get_width()-5, self.hierarchySurface.get_height()-5), 1)

        # title
        self.textManager.makeText(self.hierarchySurface, "Hierarchy", 5, 5)

    def SceneLoop(self):
        self.hierarchyUI()
        for bodies in self.SceneBodies:
            bodies.body.makeBody()
            
            
            if bodies.body.isColliding():
                self.console.Log("Collider alert!!", bodies)
            id = bodies.body.getID()
            self.textManager.makeText(self.hierarchySurface, "- Body {id}".format(id = id), 10, 5+(12*(id)))

        self.SceneUI.SceneUILoop()

        
           