import pygame
from pygame.locals import *
from data.engine.Engine import Engine

from data.engine.collision.CollisionEngine import CollisionEngine
 
class App:
    def __init__(self):
        self._running = True
        self.title = "engine"
        self._display_surf = None
        self.width, self.height = 1080, 650
        self.size = self.width, self.height
        self.BlockSize = 20
        self.engineWidth = 820
        self.engineHeight = 520
        self.engineSurfaceSize = self.engineWidth, self.engineHeight
        
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.globalSurface = self._display_surf
        
        icon = pygame.image.load('images/logo.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Physics Engine")

        self.engineSurface = pygame.Surface(self.engineSurfaceSize, )
        self.HierarchySurface = pygame.Surface((self.width-self.engineWidth, self.engineHeight))
        self.consoleSurface = pygame.Surface((self.width, self.height-self.engineHeight))

        self.Engine = Engine(self.globalSurface, 
                            self.engineSurface, 
                            self.HierarchySurface, 
                            self.consoleSurface, 
                            self.engineWidth, 
                            self.engineHeight, 
                            self.BlockSize)
        
 
    def on_event(self, event):
        self.Engine.EngineEvent(event)
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
        self.Engine.EngineLoop()
        


    def on_render(self):
        self.Engine.EngineRender()
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