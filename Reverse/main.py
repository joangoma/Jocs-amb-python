import pygame
from reverse.constants import al, am, midaQ
#from reverse.board import Board
from reverse.game import Game
from algoritme.minimax import minimax

import tkinter as tk
from tkinter import messagebox


win = pygame.display.set_mode((al, am))
pygame.display.set_caption('Reversi')

fps = 60

def columna_filera(x, y):
    row = x // midaQ
    col = y // midaQ
    return row, col

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
    run = True
    clock = pygame.time.Clock()
    #board = Board()
    game = Game(win)
    game.valid_moves()

    while run:
        clock.tick(fps)
        #pygame.display.update()
        '''
        if game.turn == (0, 0, 0):
            value, new_board = minimax(game.get_board(), 4, (0, 0, 0), game, float("-inf"), float("inf"))
            game.ai_move(new_board)
        '''

        if game.end_game():
            if game.blanc > game.negre:
                message_box('Tornar a jugar...', 'Han guanyat les blanques '  + str(game.blanc) + ' a ' + str(game.negre))
                game.reset()
            elif game.blanc < game.negre:
                message_box('Tornar a jugar...', 'Han guanyat les negres '  + str(game.negre) + ' a ' + str(game.blanc))
                game.reset()
            else:
                message_box('Tornar a jugar...', 'Empat!!!')
                game.reset()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = columna_filera(pos[1], pos[0])
                game.move(row, col)

        game.update()
    pygame.quit()

main()