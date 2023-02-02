import pygame
import os
import random
import tkinter as tk
from tkinter import messagebox

midaq = 20
fil, col = 20, 20
al, am = fil*midaq, col*midaq
mines = 75


nums = [(pygame.image.load(os.path.join("sprites", "one.png"))), 
        (pygame.image.load(os.path.join("sprites", "two.png"))),
        (pygame.image.load(os.path.join("sprites", "three.png"))), 
        (pygame.image.load(os.path.join("sprites", "four.png"))),
        (pygame.image.load(os.path.join("sprites", "five.png"))), 
        (pygame.image.load(os.path.join("sprites", "six.png"))),
        (pygame.image.load(os.path.join("sprites", "seven.png"))), 
        (pygame.image.load(os.path.join("sprites", "eight.png")))]

base = pygame.image.load(os.path.join("sprites", "block.png"))
mina = pygame.image.load(os.path.join("sprites", "mine.png"))
empty = pygame.image.load(os.path.join("sprites", "empty.png"))
band = pygame.image.load(os.path.join("sprites", "flagged.png"))

#fem rescale de les imatges
for i, e in enumerate(nums):
    nums[i] = pygame.transform.scale(e, (midaq, midaq))
base = pygame.transform.scale(base, (midaq, midaq))
mina = pygame.transform.scale(mina, (midaq, midaq))
empty = pygame.transform.scale(empty, (midaq, midaq))
band = pygame.transform.scale(band, (midaq, midaq))

class Partida:
    def __init__(self, pI, mines):
        self.part = []
        self.pI = pI
        self.mines = mines
        self.viu = True
        self.mapaGen = False
        self.generarMap()

    def update(self, fines):
        if self.viu == True:
            self.dibuixPart(fines)
            pygame.display.update()

    def dibuixPart(self, fines):
        for i in range(fil):
            for j in range(col):
                #fines.blit(base, (i*midaq, j*midaq))
                if self.part[i][j][1] == False: 
                    fines.blit(base, (i*midaq, j*midaq))
                    if self.part[i][j][2] == True: fines.blit(band, (i*midaq, j*midaq))
                elif self.part[i][j][1] == True:
                    if self.part[i][j][0] == 'M': fines.blit(mina, (i*midaq, j*midaq)) 
                    else: 
                        num = int(self.part[i][j][0])
                        if num == 0: fines.blit(empty, (i*midaq, j*midaq))
                        else: fines.blit(nums[num-1], (i*midaq, j*midaq))

    def generarMap(self):
        for i in range(fil):
            self.part.append([])
            for j in range(col):
                self.part[i].append(['0', False, False])
        self.mapaGen = True
    
    def contMin(self, x, y): 
        num = 0
        l = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        x1, y1 = x, y
        for e in l:
            x1, y1 = x + e[0], y + e[1]
            if x1 >= 0 and x1 < len(self.part) and y1 >= 0 and y1 < len(self.part[0]):
                #print(x1, y1)
                if self.part[x1][y1][0] == 'M': num += 1
        return num

    def minaProp(self, x, y, x1, y1):
        num = 0
        l = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 0)]
        x2, y2 = x, y
        for e in l:
            x2, y2 = x + e[0], y + e[1]
            if x2 == x1 and y2 == y1: return True
            
        return False

    def generarMin(self, x1, y1):
        mines = 0
        minl = []
        while mines < self.mines:
            x = random.randrange(0, fil)
            y = random.randrange(0, col)
            if (((x, y)) not in minl) and (self.minaProp(x, y, x1, y1) == False): 
                minl.append((x, y))
                mines += 1

        for i in range(fil):
            for j in range(col):
                if ((i, j)) in minl: self.part[i][j] = (['M', False, False])
                else: self.part[i][j] = (['.' , False, False])
        
        for i in range(fil):
            for j in range(col):
                if ((i, j)) not in minl: self.part[i][j] = ([str(self.contMin(i, j)), False, False])
        #print(self.part)

    def bfs(self, x, y):
        if (x >= 0 and x < len(self.part) and y >= 0 and y < len(self.part[0])) == False: return False
        if self.part[x][y][0] != '0': 
            if self.part[x][y][0] != 'M': 
                self.part[x][y][1] = True
                return False
        if self.part[x][y][1] == True: return False
        self.part[x][y][1] = True

        l = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for e in l:
            self.bfs(x+e[0], y+e[1])

        #falta programar aquesta funció

    def tirar(self, x, y):
        tup = self.part[x][y]
        if tup[1] == False and tup[2] == False:
            if tup[0] == '0': 
                self.bfs(x, y)
                tup[1] = True
                self.part[x][y] = tup
            else:
                tup[1] = True
                self.part[x][y] = tup

    def bandera(self, x, y):
        if self.part[x][y][2] == False: 
            self.part[x][y][2] = True
            if self.part[x][y][0] == 'M': self.mines -= 1
        elif self.part[x][y][2] == True:
            self.part[x][y][2] = False

    def guany(self):
        if self.mines == 0:
            self.viu = False
            return True
        
        return False
    
    def lose(self):
        for i in range(fil):
            for j in range(col):
                if self.part[i][j][0] == 'M' and self.part[i][j][1] == True: 
                    self.viu = False
                    return True
        return False

def columna_filera(x, y): 
    fil = x // midaq
    col = y // midaq 
    return fil, col

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    fps = 60
    bucle = True
    rellotge = pygame.time.Clock()

    finest = pygame.display.set_mode((al, am))
    pygame.display.set_caption('Minesweeper')

    part = Partida((0,0), mines)

    t = False
    while bucle:
        if part.viu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bucle = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if t == False:
                            pos = pygame.mouse.get_pos()
                            x, y = columna_filera(pos[0], pos[1])
                            part.generarMin(x, y)
                            part.tirar(x, y)
                            t = True
                        else:
                            pos = pygame.mouse.get_pos()
                            x, y = columna_filera(pos[0], pos[1])
                            part.tirar(x, y)
                    elif event.button == 3:
                        pos = pygame.mouse.get_pos()
                        x, y = columna_filera(pos[0], pos[1])
                        part.bandera(x, y)
                    
        if part.guany():
            message_box("Has guanyat !!!", "Menú principal")
            bucle = False
            pygame.quit()
        elif part.lose():
            message_box("Has perdut :(", "Menú principal")
            bucle = False
            pygame.quit()
        
        part.update(finest)
    pygame.quit()
main()