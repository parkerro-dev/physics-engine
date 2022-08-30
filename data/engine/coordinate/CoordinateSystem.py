import pygame

class CoordSys():
    def __init__(self, surface, width, height, blockSize, Colors):
        self.surface = surface
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.Colors = Colors

    def Grid(self):
        self.origin = (self.width//2, self.height//2)
        self.originX = self.width//2
        self.originY = self.height//2
        #Drawing the origin lines
        pygame.draw.line(self.surface, (self.Colors.primary), (self.originX, 0), (self.originX, self.height))
        pygame.draw.line(self.surface, (self.Colors.primary), (0, self.originY), (self.width, self.originY))
        for i in range(-self.width//self.blockSize ,self.width//self.blockSize):
            if(i==0): 
                continue
            pygame.draw.line(self.surface, (self.Colors.darkSecondary), self.GetPos(i, -self.height//self.blockSize), self.GetPos(i, self.height//self.blockSize))

        for j in range(-self.height//self.blockSize, self.height//self.blockSize):
            if (j==0):
                continue
            pygame.draw.line(self.surface, (self.Colors.darkSecondary), self.GetPos(-self.width//self.blockSize,j), self.GetPos(self.width//self.blockSize, j))

    def GetCoord(self, posX, posY):
        relPosX = posX - self.originX
        relPosY = self.originY - posY
        coordX = round(relPosX/self.blockSize, 3)
        coordY = round(relPosY/self.blockSize, 3)
        return((coordX, coordY))

    def GetPos(self, coordX, coordY):
        relPosX = coordX * self.blockSize
        relPosY = coordY * self.blockSize
        posX = self.originX + relPosX
        posY = -relPosY + self.originY
        return((posX, posY))

    