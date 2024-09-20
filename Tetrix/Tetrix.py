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

# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

khoi = [S, Z, I, O, J, L, T]
mau = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption('Caro (3x3_3) - cuberlong')
pygame.init()


def inkq(a) :
    for i in range(3) :
        for j in range(3) :
            print(a[j][i], end = ' ')
        print()
    print('_____________________________')

def main() :
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit() 
                exit(0) 
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    print(khoi[1])
        
if __name__ == '__main__' :
    main()