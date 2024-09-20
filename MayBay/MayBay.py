LINK = 'D:'

import pygame, sys, random
from pygame.locals import *

BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)

PINK   = (255,   0, 255)
YELLOW = (255, 255,   0)
ORANGE = (255, 128,   0)
AQUA   = (  0, 255, 255)
SILVER = (192, 192, 192)
GRAY   = (128, 128, 128)
MAROON = (128,   0,   0)
OLIVE  = (128, 128,   0)
GREEND = (  0, 128,   0)
PURPLE = (128,   0, 128)
TEAL   = (  0, 128, 128)
NAVY   = (  0,   0, 128)

DISPLAYSURF = pygame.display.set_mode((600, 600))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption('Caro (3x3_3) - cuberlong')
BAY1 = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\MayBay\\maybaydo.png')
BAY2 = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\MayBay\\maybayxanh.png')
pygame.init()

X1 = 0
Y1 = 500
X2 = 500
Y2 = 500
def capnhat() :
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(BAY1, (X1, Y1))
    DISPLAYSURF.blit(BAY2, (X2, Y2))
    pygame.display.update()

def main() :
    running = True
    capnhat()
    move1x = 0
    move1y = 0
    move2x = 0
    move2y = 0
    while running:
        pygame.time.delay(1)
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit() 
                exit(0)
                
            global X1, Y1, X2, Y2
            if event.type == KEYDOWN:
                if event.key == K_UP: move1y = -1
                if event.key == K_DOWN: move1y = 1
                if event.key == K_LEFT: move1x = -1
                if event.key == K_RIGHT: move1x = 1
                if event.key == K_w: move2y = -1
                if event.key == K_s: move2y = 1
                if event.key == K_a: move2x = -1
                if event.key == K_d: move2x = 1
            if event.type == KEYUP:
                if event.key == K_UP: move1y = 0
                if event.key == K_DOWN: move1y = 0
                if event.key == K_LEFT: move1x = 0
                if event.key == K_RIGHT: move1x = 0
                if event.key == K_w: move2y = 0
                if event.key == K_s: move2y = 0
                if event.key == K_a: move2x = 0
                if event.key == K_d: move2x = 0
        X1 = (X1+move1x+600)%600
        Y1 = (Y1+move1y+600)%600
        X2 = (X2+move2x+600)%600
        Y2 = (Y2+move2y+600)%600
        capnhat()
        pygame.time.delay(1)

                    
                

        
if __name__ == '__main__' :
    main()