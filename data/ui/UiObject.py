import pygame

class UiObject():
    def __init__(self, object, location, selectable=True):
        self.object = object
        self.location = location # location format is ((top, left), (bottom, right)
        self.selectable = selectable

    def isMouseHover(self):
        mousePos = pygame.mouse.get_pos() 
        if mousePos.y> self.location[0][0] and mousePos.y < self.location[1][0]:
            if mousePos.x > self.location[0][1] and mousePos.x < self.location[1][1]:
                return True
        
        return False

    def onMouseHover(self):
        if self.selectable:
            self.object.onMouseHover()
    
    def onMouseClick(self):
        if self.selectable:
            self.object.onMouseClick()
    
