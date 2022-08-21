
import pygame

class ColliderBody:
    def __init__(self, startCoords, endCoords):
        self.startCoords = startCoords
        self.endCoords = endCoords

    def updateCollider(self, startCoords, endCoords):
        self.startCoords = startCoords
        self.endCoords = endCoords 

    def CheckColliding(self, colliderStartCoords, colliderEndCoords):
        if self.startCoords[0] > colliderEndCoords[0] or colliderStartCoords[0] > self.endCoords[0]:
            print("cunt1")
            return False
        
        if self.endCoords[1] > colliderStartCoords[1] or colliderEndCoords[1] > self.startCoords[1]:
            print("self coords: {selfCoords}, otherCoords: {otherCoords}".format(selfCoords = (self.startCoords, self.endCoords), otherCoords = (colliderStartCoords, colliderEndCoords)))
            print("cunt2")
            return False
        print("cunt3")
        return True