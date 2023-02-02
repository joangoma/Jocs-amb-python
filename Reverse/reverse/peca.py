import pygame
from .constants import verd, negre, al, row, am, col, midaQ

class Peca:
    padding = 15
    OUTLINE = 2 
    def __init__(self, color, row, col): #
        self.color = color
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.espai = 15
        self.cal_pos()
        
    def cal_pos(self):
        self.x = midaQ * self.row + midaQ//2
        self.y = midaQ * self.col + midaQ//2

    def drawPiece(self, win):
        radi = midaQ//2 - self.espai
        pygame.draw.circle(win, (31, 31, 31), (self.x, self.y), radi + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radi)

    