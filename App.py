from numpy import empty
import pygame
from pygame.locals import *
from Engine import Engine
from TextMaker import TextMaker
from CollisionEngine import CollisionEngine
 
class App:
    def __init__(self):
        self._running = True
        self.title = "engine"
        self._display_surf = None
        self.width, self.height = 1080, 600
        self.size = self.width, self.height
        self.BlockSize = 20
        
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.globalSurface = self._display_surf
        self.Engine = Engine(self.globalSurface, self.width, self.height, self.BlockSize)
        self.CollisionEngine = CollisionEngine
        pygame.font.init()
        if pygame.font.get_init():
            self.TextMaker = TextMaker()
 
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.globalSurface.fill((0, 0, 0))
            if event.key == pygame.K_LEFT:
                # stops block size becoming 0 as it breaks it.
                if self.Engine.blockSize > 5:
                    self.Engine.blockSize -= 5
                
            if event.key == pygame.K_RIGHT:
                self.Engine.blockSize +=5
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        self.Engine.Grid()
        self.mousePos = pygame.mouse.get_pos()
        self.mouseCoords = self.Engine.GetCoord(self.mousePos[0], self.mousePos[1])
        print(self.mouseCoords)
        self.mouseCoordsString = ''.join(str(self.mouseCoords))


    def on_render(self):
        self.TextMaker.makeText(self.globalSurface, "My Physics Engine v0.0.1", 0, 0)
        self.TextMaker.makeText(self.globalSurface, self.mouseCoordsString, self.width-75, self.height-10)
        
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()