
import pygame

from ..ui.uiMakers.TextMaker import TextMaker


class Console():
    def __init__(self, consoleSurface):
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
            print(logs)
            counter += 1
            consoleText = "> {message} from {location}".format(message = logs[0], location = logs[1])
            if logs[1] == "":
                consoleText = "> {message}".format(message = logs[0])
            self.textManager.makeText(self.surface, consoleText, 15, 110 - (counter*12)) 

    def OnLoop(self):
        #blank console Canvas
        self.surface.fill((0,0,0))
        # Outline Console
        pygame.draw.rect(self.surface, (200,200,200), (3, 0, self.surface.get_width()-5, self.surface.get_height()-5), 2)
        # console UI
        self.textManager.makeText(self.surface, "Console Log:", 10, 10)

        # Logging Console (showing last 10 console logs)
        self.PrintConsole(8)
