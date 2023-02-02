import pygame
from .constants import verd, negre, al, am, row, col, midaQ, blanc
from .peca import Peca

class Board:

    def __init__(self):
        self.board = []
        self.negr = 0
        self.blan = 0
        self.iniciTaulell()
        self.posM = []
        self.dir = []
    
    def iniciTaulell(self):  
        i1 = 0
        i2 = 0
        while i1 <= 7:
            self.board.append([])
            while i2 <= 7:
                self.board[i1].append(0)
                i2 += 1
            i1 += 1
            i2 = 0

        self.board[3][3] = Peca(blanc, 3, 3)
        self.board[3][4] = Peca(negre, 3, 4)
        self.board[4][3] = Peca(negre, 4, 3)
        self.board[4][4] = Peca(blanc, 4, 4)

        '''
        self.board[3][3] = Peca(negre, 3, 3)
        self.board[3][4] = Peca(negre, 3, 4)
        self.board[4][3] = Peca(negre, 4, 3)
        self.board[4][4] = Peca(blanc, 4, 4)
        self.board[3][2] = Peca(negre, 2, 3)
        '''

    def drawBoard(self, win):
        
        x = 0
        y = 0
        win.fill(verd)#
        
        for i in range(row): #
            x += midaQ #
            y += midaQ #

            pygame.draw.line(win, (0,0,0), (x, 0), (x, am)) #
            pygame.draw.line(win, (0,0,0), (0, y), (am, y)) #
        
        for i1 in range(row):
            for j in range(col):
                if self.board[i1][j] != 0:
                    piece = self.board[i1][j]
                    piece.drawPiece(win)

        #print(self.board)
        
    def addPeca(self, row, col, cl):
        self.board[col][row] = Peca(cl, col, row)
    
    def evaluate(self):
        return (self.negr - self.blan) + (self.punta1() - self.punta2())
    
    


    def punta1(self):
        i = 0
        if self.board[0][0] != 0 and self.board[0][0].color == (0, 0, 0):
            i += 5
        elif self.board[7][7] != 0 and self.board[7][7].color == (0, 0, 0):
            i += 5
        elif self.board[0][7] != 0 and self.board[0][7].color == (0, 0, 0):
            i += 5
        elif self.board[7][0] != 0 and self.board[7][0].color == (0, 0, 0):
            i += 5
        return i

    def punta2(self):
        i = 0
        if self.board[0][0] != 0 and self.board[0][0].color == (255, 255, 255):
            i += 5
        elif self.board[7][7] != 0 and self.board[7][7].color == (255, 255, 255):
            i += 5
        elif self.board[0][7] != 0 and self.board[0][7].color == (255, 255, 255):
            i += 5
        elif self.board[7][0] != 0 and self.board[7][0].color == (255, 255, 255):
            i += 5
        return i

    def turnPeca(self, x, y):
        if self.board[x][y].color == (0, 0, 0):
            self.board[x][y] = 0
            self.board[x][y] = Peca(blanc, x, y)
        else:
            self.board[x][y] = 0
            self.board[x][y] = Peca(negre, x, y)
            

    def peces(self):
        self.blan = 0
        self.negr = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != 0:
                    if self.board[i][j].color == (255, 255, 255):
                        self.blan += 1
                    elif self.board[i][j].color == (0,0,0):
                        self.negr += 1

        return self.blan, self.negr

    def winner(self):
        if self.blan + self.negr == 64:
            return True
        else:
            return False
        
        if self.blan == 0 or self.negr == 0:
            return True

    def espai(self, i, j):
        return True
        if i == 7 or i == 0 or j == 7 or j == 0:
            return False
        else:
            return True

    #def move(self):

    def validMoves(self, turn):
        self.posM = []
        self.dir = []
        self.dicL = []
        self.minl = []
        self.posF = []
        self.t = True
        x = 0
        y = 0
        self.dic = {}
        for row in range(8):
            for c in range(8):
                if self.board[row][c] != 0:
                    if self.board[row][c].color != turn:  
                        self.posF.append((row, c))#
                        if self.espai(row, c) == True:
                            if row + 1 <= 7:
                                if self.board[row + 1][c] == 0:
                                    self.posM.append((row + 1, c))
                                    self.dir.append("dreta")
                            if c + 1 <= 7:
                                if self.board[row][c + 1] == 0:
                                    self.posM.append((row, c + 1))
                                    self.dir.append("avall")
                            if row - 1 >= 0:
                                if self.board[row - 1][c] == 0:
                                    self.posM.append((row -1, c))
                                    self.dir.append("esquerra")
                            if c - 1 >= 0:
                                if self.board[row][c - 1] == 0:
                                    self.posM.append((row, c - 1))
                                    self.dir.append("amunt")
                            if row + 1 <= 7 and c + 1 <= 7:
                                if self.board[row + 1][c + 1] == 0:
                                    self.posM.append((row + 1, c + 1))
                                    self.dir.append("punta avall dreta")
                            if row - 1 >= 0 and c + 1 <= 7:
                                if self.board[row - 1][c + 1] == 0:
                                    self.posM.append((row - 1, c + 1))
                                    self.dir.append("punta avall esquerra")
                            if row - 1 >= 0 and c - 1 >= 0:
                                if self.board[row- 1][c - 1] == 0:
                                    self.posM.append((row - 1, c - 1))
                                    self.dir.append("punta amunt esquerra")
                            if row + 1 <= 7 and c - 1 >= 0:
                                if self.board[row + 1][c - 1] == 0:
                                    self.posM.append((row + 1, c - 1))
                                    self.dir.append("punta amunt dreta")
        
        '''
        for e in range(len(self.posM)):
            t = ()
            e1, e2 = self.posM[e][0], self.posM[e][1]
            t = (e2, e1)
            self.posM[e] = t
            t = ()
        '''

        for i in range(len(self.posM)):
            self.x = 0
            self.y = 0

            
            if(self.t == True):
                if self.dir[i] == "amunt":
                    self.minl = []
                    x = self.posM[i][0]
                    y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        y += 1
                        if y <= 7:
                            if self.board[x][y] != 0:
                                if self.board[x][y].color != turn:
                                    self.minl.append((x, y))
                                elif self.board[x][y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1


            if(self.t == True):    
                if self.dir[i] == "avall":
                    self.minl = []
                    x = self.posM[i][0]
                    y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        y -= 1
                        if y >= 0:
                            if self.board[x][y] != 0:
                                if self.board[x][y].color != turn:
                                    self.minl.append((x, y))
                                elif self.board[x][y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1
            
            if(self.t == True):
                if self.dir[i] == "dreta":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        self.x -= 1
                        if self.x >= 0:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1

            if(self.t == True):
                if self.dir[i] == "esquerra":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:    
                        self.x += 1
                        if self.x <= 7:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1

            if(self.t == True):
                if self.dir[i] == "punta avall dreta":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:

                        self.y -= 1
                        self.x -= 1
                        if self.x >= 0 and self.y >= 0:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1

            if(self.t == True):
                if self.dir[i] == "punta avall esquerra":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        self.y -= 1
                        self.x += 1
                        if self.x <= 7 and self.y >= 0:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1

            if(self.t == True):

                if self.dir[i] == "punta amunt esquerra":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        self.x += 1
                        self.y += 1
                        if self.x <= 7 and self.y <= 7:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1


            if(self.t == True):
                if self.dir[i] == "punta amunt dreta":
                    self.minl = []
                    self.x = self.posM[i][0]
                    self.y = self.posM[i][1]
                    i1 = 0
                    while self.t:
                        self.x -= 1
                        self.y += 1
                        if self.x >= 0 and self.y <= 7:
                            if self.board[self.x][self.y] != 0:
                                if self.board[self.x][self.y].color != turn:
                                    self.minl.append((self.x, self.y))
                                elif self.board[self.x][self.y].color == turn:
                                    self.dic[self.posM[i]] = self.minl
                                    self.dicL.append(self.dic)
                                    self.dic = {}
                                    self.minl = []
                                    self.t = False
                                else:
                                    self.dic = {}
                                    self.minL = []
                                    self.t = False
                            else:
                                self.dic = {}
                                self.minL = []
                                self.t = False
                        if i1 > 7:
                            self.t = False
                            break
                        i1 += 1
            
            self.t = True
        print(self.dicL)
        return self.dicL, self.posM


    
        

    
    

        
