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
        self.UiObjects.remove(UiObject)

    def onEvent(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            self.console.Log("mouse button {button} was pressed".format(button = event.button), self)
            
            if event.button == 3: # right mouse button
                for uiObject in self.hoverOverObjects:
                    if uiObject.name == "EngineSurface":
                        self.SceneManager.engineRMBMenu()
            
            if event.button == 1:
                if self.SceneManager.menuActive:
                    for uiObjects in self.hoverOverObjects:
                        if uiObjects.name == "makeSurfaceOption":
                            self.bodyManager.makeRigidSurface((0, 0), (5, 1))
                            self.SceneManager.engineRMBMenuClose()  
            
    
    def OnLoop(self):
        # This for loop checks for all UI objects and whether the mouse is hovering on it
        for uiObject in self.UiObjects:
            
            if uiObject.isMouseHovering is not True:
                uiObject.isMouseHover()
                if uiObject.isMouseHovering == True:
                    self.hoverOverObjects.append(uiObject)
                    for uiObject in self.hoverOverObjects:
                        print(uiObject.name)
                    
            
            uiObject.isMouseHover()
            if uiObject in self.hoverOverObjects and uiObject.isMouseHovering == False:
                self.hoverOverObjects.remove(uiObject)
                

        for uiObjects in self.hoverOverObjects:
            print(uiObjects.name)
                