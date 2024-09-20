import pygame, sys, math
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ve do thi ham so - cuberlong')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

TILE = 50   # 50 pixels = 1 don vi

def veluoiovuong() :
    for i in range(1, 12) :
        pygame.draw.line(DISPLAYSURF, BLACK, (i*50, 0), (i*50, 600), 1)
        pygame.draw.line(DISPLAYSURF, BLACK, (0, i*50), (600, i*50), 1)

def vexOy() :
    pygame.draw.line(DISPLAYSURF, BLACK, (300, 0), (300, 600), 3)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 300), (600, 300), 3)

def vedothi1(a) :
    a = -a
    pygame.draw.line(DISPLAYSURF, BLUE, (300, 300), (300+1, 300+a), 3)
    pygame.draw.line(DISPLAYSURF, BLUE, (300, 300), (300-1, 600-a), 3)

def vedothi2(a) :
    for y in range(1, 300) :
        x = math.sqrt(abs(y/a))
        if (a < 0) :
            pygame.draw.circle(DISPLAYSURF, RED, (x+300, y+300), 3)
            pygame.draw.circle(DISPLAYSURF, RED, (-x+300, y+300), 3)
        else :
            pygame.draw.circle(DISPLAYSURF, RED, (x+300, -y+300), 3)
            pygame.draw.circle(DISPLAYSURF, RED, (-x+300, -y+300), 3)

DISPLAYSURF.fill(WHITE)

veluoiovuong()
vexOy()
vedothi1(2) # y = ax
vedothi2(0.01) # y = axx

pygame.display.update()

stop = input()