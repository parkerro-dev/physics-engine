from math import sqrt
import pygame
import matplotlib.pyplot as plt
import numpy

class PhysicsEngine():
    def __init__(self, coordSys, console, bodyManager, sceneManager):
        self.coordSys = coordSys
        self.console = console
        self.bodyManager = bodyManager
        self.sceneManager = sceneManager
        self.time = None
        self._isPlaying = False
        self.gravity = 9.81
        self.physicsBodies = []
        self.bodies = self.sceneManager.SceneBodies
        

    def OnPlay(self):
        self.console.Log("Running", self)
        for bodies in self.bodies:
            if bodies.body.physics:
                self.physicsBodies.append(bodies)
        
        self.time = pygame.time.Clock()
        self._isPlaying = True

        for body in self.physicsBodies:
            self.calcMotion(body)

    def calcMotion(self, body):
        #check if colliding (simple atm it wont work with more than two bodies though.)
        t_list = []
        h_list = []
        t = 0
        h0 = body.body.endCoord[1]
        vY = 0
        g = self.gravity
        freefall = True
        dt = 0.001
        rho = 0.85 # coefficient of restitution
        tau = 0.1 # contact time
        hmax = h0
        t_last = -sqrt(2*h0/g)
        h = h0
        hstop = 0.01
        vmax = sqrt(2 * hmax * g)
        while(hmax > hstop):
            if freefall:
                hnew = h + vY*dt - 0.5*g*dt*dt
                if(hnew<0):
                    t = t_last + 2*sqrt(2*hmax/g)
                    h = 0
                    freefall = False
                    t_last = t + tau
                else:
                    t = t+dt
                    vY = vY - g*dt
                    h = hnew
            else:
                t = t+tau
                vmax = vmax * rho
                vY = vmax
                freefall = True
                h=0
            hmax = 0.5*vmax*vmax/g
            body.body.height.append(-h)
            h_list.append(h)
            t_list.append(t)
        plt.plot(t_list, h_list)
        plt.show()






    def OnPhysicsLoop(self):
        if self._isPlaying == False:
            return
        

        
 
        