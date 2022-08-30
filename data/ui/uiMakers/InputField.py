import pygame
from .TextMaker import TextMaker

class InputField:
    def __init__(self, type, text, object, posX, posY, surface, UIManager):
        self.type = type
        self.text = text 
        self.object = object
        self.posX = posX
        self.posY = posY
        self.surface = surface
        self.textMaker = TextMaker()
        self.UIManager = UIManager
        self.selected = False
        if type == "Numerical":
            self.NumericalInputField()


    def OnClick(self, object):
        if object == self:
            self.selected = True
        else:
            print("error: the input field isnt equal to itself, idk how you did that")

    def NumericalInputField(self):
        pass
