LINK = 'E:'

import pygame
from pygame.locals import *

a = [[' ', ' ', ' '], [' ', 'O', 'X'], ['X', ' ', ' ']]

BACKGROUND = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\back.png')
XXX = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\X.png')
OOO = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\O.png')

DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.blit(BACKGROUND, (0, 0))
pygame.display.set_caption('Caro (3x3_3) - cuberlong')
pygame.init()

def solve() :
    global DISPLAYSURF
    DISPLAYSURF.blit(BACKGROUND, (0, 0))
    for i in range(3) :
        for j in range(3) :
            danh(i, j)

def danh(x, y) :
    global DISPLAYSURF, a
    if (a[x][y] == ' ') :
        return
    if (a[x][y] == 'X') :
        DISPLAYSURF.blit(XXX, (x*100+5, y*100+5))
        pygame.display.update()
    else :
        DISPLAYSURF.blit(OOO, (x*100+5, y*100+5))
        pygame.display.update()

solve()
pygame.time.delay(10000)
