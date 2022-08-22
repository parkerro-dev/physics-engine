from operator import index
import pygame 
from .UiObject import UiObject

class UiManager():
    
    def __init__(self, console, sceneManager, bodyManager):
        self.UiObjects = []
        self.console = console
        self.SceneManager = sceneManager
        self.bodyManager = bodyManager
        self.hoverOverObjects = []

    def makeNewUIObject(self,name ,object, location, layer, selectable = True):
        newUiObject = UiObject(name ,object, location, layer, selectable)  
        self.UiObjects.append(newUiObject)
        return newUiObject

    def removeUiObject(self, UiObject):
        if UiObject in self.UiObjects:
            self.UiObjects.remove(UiObject)

    def onEvent(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            self.console.Log("mouse button {button} was pressed".format(button = event.button), self)
            
            if event.button == 3: # right mouse button
                for uiObject in self.hoverOverObjects:
                    if uiObject.name == "EngineSurface":
                        self.SceneManager.SceneUI.EngineMenu.createMenu()
            
            if event.button == 1:
                for uiObjects in self.hoverOverObjects:
                    if self.SceneManager.SceneUI.EngineMenu.menuActive:
                        if uiObjects.name == "makeSurfaceOption":
                            self.bodyManager.makeRigidSurface((-10, 0), (10, -1))
                            self.SceneManager.SceneUI.EngineMenu.closeMenu()
                        if uiObjects.name == "makeParticleOption":
                            self.bodyManager.makeParticle((pygame.mouse.get_pos()))
                            self.SceneManager.SceneUI.EngineMenu.closeMenu()

                    elif uiObjects.name == "playButton":
                        uiObjects.onMouseClick() 
                    elif uiObjects.name == "HierarchyButton" or uiObjects.name == "PropertiesButton":
                        print("click click")
                        uiObjects.onMouseClick()
            
    
    def OnLoop(self):
        # This for loop checks for all UI objects and whether the mouse is hovering on it
        for uiObject in self.UiObjects:
            
            if uiObject.isMouseHovering is not True:
                uiObject.isMouseHover()
                if uiObject.isMouseHovering == True:
                    self.hoverOverObjects.append(uiObject)
                    for uiObject in self.hoverOverObjects:
                        pass
                        #print(uiObject.name)
                    
            
            uiObject.isMouseHover()
            if uiObject in self.hoverOverObjects and uiObject.isMouseHovering == False:
                self.hoverOverObjects.remove(uiObject)
                

        for uiObjects in self.hoverOverObjects:
            pass
            #print(uiObjects.name)
                