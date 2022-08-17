import pygame 
from .UiObject import UiObject

class UiManager():
    def __init__(self, eventManager):
        self.UiObjects = []
        self.eventManager = eventManager

    def makeNewUIObject(self, object, location, selectable = True):
        newUiObject = UiObject(object, location, selectable = True)  
        self.UiObjects.append(newUiObject)

    def OnLoop(self):
        if self.UiObjects == []:
            pass
        else:
            for uiObject in self.UiObjects:
                if uiObject.onMouseHover():
                    if self.eventManager.leftMouseDown():
                        uiObject.onMouseClick()
                    else:
                        uiObject.onMouseHover()