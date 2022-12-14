import pygame

from data.ui.uiMakers.TextMaker import TextMaker
from ...engine.scene.SceneUIComponents.Button import Button

class SidePanel:
    def __init__(self, sidePanelSurface, engineSurface, UIManager, sceneManager, Colors):
        self.sidePanelSurface = sidePanelSurface
        self.engineSurface = engineSurface
        self.sceneManager = sceneManager
        self.UIManager = UIManager
        self.Colors = Colors
        self.HierarchyUI = HierarchyUI(self.sidePanelSurface, self.sceneManager)
        self.PropertiesUI = PropertiesUI(self.sidePanelSurface, self.sceneManager)
        self.OutlineColor = (155, 155, 155)
        self.HierarchyButton = Button("Hierarchy", (5, 5), self.sidePanelSurface, ((self.engineSurface.get_width(), 0),(self.engineSurface.get_width()+75, 20)), ((0, 0), (75, 20)),self.UIManager, self.HierarchyUI, self.Colors,True)
        self.PropertiesButton = Button("Properties", (5, 5), self.sidePanelSurface, ((self.engineSurface.get_width()+80, 0), (self.engineSurface.get_width()+155, 20)), ((80, 0), (155, 20)), self.UIManager, self.PropertiesUI, self.Colors,False)
        self.On_Init()
   
    def On_Init(self):
        self.HierarchyUI.PropertiesUI = self.PropertiesUI
        self.PropertiesUI.HierarchyUI = self.HierarchyUI

    def SidePanelLayout(self):
        self.Outline = pygame.draw.rect(self.sidePanelSurface, self.OutlineColor, (0, 20, self.sidePanelSurface.get_width(), self.sidePanelSurface.get_height()-20), 1)
        self.HierarchyButton.buttonLoop()
        self.PropertiesButton.buttonLoop()

    def OnLoop(self):
        self.sidePanelSurface.fill(self.Colors.bg)
        self.SidePanelLayout()
        
        if self.HierarchyUI.active:
           
            self.HierarchyButton.inverted = True
            self.PropertiesButton.inverted = False
            self.HierarchyUI.OnLoop()
        else:
            self.HierarchyButton.inverted = False
            self.PropertiesButton.inverted = True
            self.PropertiesUI.OnLoop()



class HierarchyUI:
    def __init__(self, sidePanelSurface, sceneManager):
        self.sidePanelSurface = sidePanelSurface
        self.sceneManager = sceneManager
        self.PropertiesUI = None
        self.active = True
        self.textManager = TextMaker()

    def OnClick(self, object):
        if self.active:
            return
        else:
            self.active = True
            self.PropertiesUI.active = False
        
    def OnLoop(self):
        for body in self.sceneManager.SceneBodies:
            id = body.body.getID()
            self.textManager.makeText(self.sidePanelSurface, "- Body {id}".format(id = id), 10, 20+(12*(id)))



class PropertiesUI:
    def __init__(self, sidePanelSurface, sceneManager):
        self.sceneManager = sceneManager
        self.sidePanelSurface = sidePanelSurface
        self.active = False
        self.HierarchyUI = None
        self.textManager = TextMaker()

    def OnClick(self, object):
        if self.active:
            return
        else:
            self.active = True
            self.HierarchyUI.active = False
        
    def PropertiesDisplay(self):
        self.Body = self.sceneManager.selectedSceneBody
        if self.Body == None:
            self.NoSelectedBody()
            return
        
        self.SelectedBody(self.Body.body)
    
    def NoSelectedBody(self):
        self.textManager.makeText(self.sidePanelSurface, "Please Select Something!", 25, 100)
    
    def SelectedBody(self, body):
        # Name
        self.textManager.makeText(self.sidePanelSurface, "name:", 10, 32)
        self.textManager.makeText(self.sidePanelSurface, body.name, 15, 50)

        #Location
        self.textManager.makeText(self.sidePanelSurface, "location:", 10, 68)
        self.textManager.makeText(self.sidePanelSurface, str(body.startCoord), 15, 86)

    def OnLoop(self):
        self.PropertiesDisplay()
        
