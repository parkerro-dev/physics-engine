from tarfile import BLOCKSIZE
import pygame

class BeforeLoad():
    def __init__(self, surface, width, height, BlockSize):
        self.surface = surface
        self.width = width
        self.height = height
        self.BlockSize = BlockSize
        self.Grid()

    def Grid(self):
        for i in range(self.BlockSize, self.width, self.BlockSize):
            pygame.draw.line(self.surface, (255,255,255, 0), (i, 0), (i,self.height))
        for j in range(self.BlockSize, self.height, self.BlockSize):
            pygame.draw.line(self.surface, (255,255, 255), (0, j), (self.width, j))

