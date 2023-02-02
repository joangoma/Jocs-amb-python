import pygame
from .board import Board
from .constants import BLUE, midaQ

class Game:

    turn1 = (255, 255, 255)

    def __init__(self, win):
        self._init()
        self.win = win
        self.turn1 = (255, 255, 255)
        self.turn = self.turn1
        self.board = Board()
        self.valid_moves()
        self.blanc = 0
        self.negre = 0
        self.t = True
        self.l, self.pos = self.valid_moves()
        

    def update(self):
        self.board.drawBoard(self.win)
        self.draw_valid_moves2(self.pos)
        self.draw_valid_moves(self.l)
        self.board.peces()
        pygame.display.update()

    def _init(self):
        if self.turn1 == (255, 255, 255):
            self.turn = (0,0,0)
            self.turn1 = (0,0,0)
        else:
            self.turn = (255, 255, 255)
            self.turn1 = (255, 255, 255)
        self.board = Board()
        self.valid_moves()
        self.blanc = 0
        self.negre = 0
        self.t = True
        self.l, self.pos = self.valid_moves()

    def reset(self):
        self._init()

    def end_game(self):
        self.blanc, self.negre = self.board.blan, self.board.negr

        if self.blanc + self.negre == 64:
            return True
        else:
            return False
        
        if self.blanc == 0 or self.negre == 0:
            return True

    def valid_moves(self):
        self.pos = []
        self.l , self.pos = self.board.validMoves(self.turn)
        if self.l == []:
            self.changeTurn()
        return self.l, self.pos
    
    def draw_valid_moves(self, moves):
        for move in moves:
            for e in move.keys():
                col = e[0]
                row = e[1]
                pygame.draw.circle(self.win, BLUE, (col * midaQ + midaQ//2, row * midaQ + midaQ//2), 10)
        
    def draw_valid_moves2(self, moves):
        '''
        for move in moves:
            col = move[0]
            row = move[1]
            pygame.draw.circle(self.win, (255, 0, 0), (col * midaQ + midaQ//2, row * midaQ + midaQ//2), 5)
        '''

    def changeTurn(self):
        if self.turn == (255, 255, 255):
            self.turn = (0,0,0)
        else:
            self.turn = (255, 255, 255)
    
    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.changeTurn()

    def move(self, x1, y1):
        for d in self.l: 
            for k in d.keys(): 
                if k == (y1, x1):
                    if self.turn == (255, 255, 255):
                        self.board.addPeca(x1, y1, (255, 255, 255)) 
                    elif self.turn == (0, 0, 0):
                        self.board.addPeca(x1, y1, (0, 0, 0))


                    for e in d[k]:
                        x = e[1]
                        y = e[0]
                        self.board.turnPeca(y, x)
                    self.t = False

        if self.t == False:
            self.changeTurn()

        self.valid_moves()
                    
        self.t = True
                
        
        
    
    

        
