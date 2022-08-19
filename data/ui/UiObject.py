import pygame

class UiObject():
    def __init__(self, name ,object, location, layer, selectable=True):
        self.name = name
        self.object = object
        self.location = location # location format is ((x, y), (x1, y1)
        self.layer = layer
        self.selectable = selectable
        self.isMouseHovering = False
        print("name: {name}, loccation: {x}, {y}, {xx}, {yy}".format(name = self.name, x= self.location[0][0], y = self.location[0][1], xx = self.location[1][0], yy = self.location[1][1]))

    def isMouseHover(self):
        mousePos = pygame.mouse.get_pos()
        mouseX = mousePos[0]
        mouseY = mousePos[1] 
        if mousePos[1]> self.location[0][1] and mousePos[1] < self.location[1][1]:
            if mousePos[0] > self.location[0][0] and mousePos[0] < self.location[1][0]:
                self.isMouseHovering = True
                return
        
        self.isMouseHovering = False
        return
    

    def onMouseClick(self):
        if self.selectable:
            self.object.OnClick()
           
    
