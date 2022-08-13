from numpy import empty
import pygame
from pygame.locals import *
import EngineInit as start
 
class App:
    def __init__(self):
        self._running = True
        self.title = "engine"
        self._display_surf = None
        self.width, self.height = 640, 400
        self.size = self.width, self.height
        self.BlockSize = 20
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.globalSurface = self._display_surf
 
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.globalSurface.fill((0, 0, 0))
            if event.key == pygame.K_LEFT:
                self.BlockSize -= 5
            if event.key == pygame.K_RIGHT:
                self.BlockSize +=5
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        start.BeforeLoad(self.globalSurface, self.width, self.height, self.BlockSize)
        pygame.draw.rect(self._display_surf, (0, 128, 255), pygame.Rect(30, 30, 60, 60))        
    def on_render(self):
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