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
                    if self.SceneManager.menuUiObject not in self.hoverOverObjects:
                        self.SceneManager.engineRMBMenuClose()   
            
    
    def OnLoop(self):
        # This for loop checks for all UI objects and whether the mouse is hovering on it
        for uiObject in self.UiObjects:
            
            if uiObject.isMouseHovering is not True:
                uiObject.isMouseHover()
                if uiObject.isMouseHovering == True:
                    self.hoverOverObjects.append(uiObject)
                    print(self.hoverOverObjects)
            
            uiObject.isMouseHover()
            if uiObject in self.hoverOverObjects and uiObject.isMouseHovering == False:
                self.hoverOverObjects.remove(uiObject)
                print(self.hoverOverObjects)

        
                