
import pygame

from ..ui.uiMakers.TextMaker import TextMaker

'''
Console object is a one instance class used to display a custom console log inside of the application
by using a in-app console, loggin is easier to see within the UI
'''
class Console():
    def __init__(self, consoleSurface, Colors):
        self.Colors = Colors
        self.surface = consoleSurface
        self.textManager = TextMaker()
        self.consoleLog = [("blank", "me"), ("-------------------", ""), ("Physics Engine v0.0.1", ""), ("Author: Robert Parker", ""), ("-------------------", "")]
        

    def Log(self, message, location):
        self.consoleLog.append((message, location))

    def PrintConsole(self, logsToShow):
        startPoint = len(self.consoleLog)- (logsToShow+1)
        if startPoint < 0 :
            startPoint = 0
        counter = 0
        for logs in self.consoleLog[:startPoint:-1]:
            counter += 1
            consoleText = "> {message} from {location}".format(message = logs[0], location = logs[1])
            if logs[1] == "":
                consoleText = "> {message}".format(message = logs[0])
            self.textManager.makeText(self.surface, consoleText, 15, 110 - (counter*12), self.Colors.primary, self.Colors.bg) 

    def OnLoop(self):
        #blank console Canvas
        self.surface.fill(self.Colors.bg)
        # Outline Console
        pygame.draw.rect(self.surface, self.Colors.secondary, (0, 0, self.surface.get_width(), self.surface.get_height()), 1)
        # console UI
        self.textManager.makeText(self.surface, "Console Log:", 10, 10)

        # Logging Console (showing last 10 console logs)
        self.PrintConsole(7)
