LINK = 'D:'

import pygame, sys, random
from pygame.locals import *
import time

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

BACKGROUND = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\back.png')
XXX = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\X.png')
OOO = pygame.image.load(LINK+'\\VScode\\PYTHON_3\\Game\\Caro\\O.png')

DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.blit(BACKGROUND, (0, 0))
pygame.display.set_caption('Caro (3x3_3) - cuberlong')
pygame.init()

a = [[' ' for i in range(3)] for i in range(3)]

def inkq(a) :
    for i in range(3) :
        for j in range(3) :
            print(a[j][i], end = ' ')
        print()
    print('_____________________________')

def ktra(x, y) :
    if a[x][y] == ' ' :
        return True
    return False

def click(x, y) :
    global a, DISPLAYSURF
    print('Click pos:', x, y, end = ' : ')
    if a[x][y] != ' ' :
        print('!!!')
        return False
    print('X -> ')
    a[x][y] = 'X'
    DISPLAYSURF.blit(XXX, (x*100+5, y*100+5))
    pygame.display.update()

    if Check() == True :
        print('YOU WIN!!!')
        font = pygame.font.SysFont('consolas', 20, 2)
        commentSuface = font.render('YOU WIN !!!', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        DISPLAYSURF.blit(commentSuface, (0, 0))
        pygame.display.update()
        pygame.time.delay(2000)
        exit(0)

    if Full() == True :
        print('Full without winer')
        font = pygame.font.SysFont('consolas', 20, 2)
        commentSuface = font.render('DRAW !!!', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        DISPLAYSURF.blit(commentSuface, (0, 0))
        pygame.display.update()
        pygame.time.delay(2000)
        exit(0)

    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while ktra(x, y) == False :
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    print('O -> ')
    a[x][y] = 'O'
    DISPLAYSURF.blit(OOO, (x*100+5, y*100+5))
    pygame.display.update()

    if Check() == True :
        print('YOU LOSE!!!')
        font = pygame.font.SysFont('consolas', 20, 2)
        commentSuface = font.render('YOU LOSE !!!', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        DISPLAYSURF.blit(commentSuface, (0, 0))
        pygame.display.update()
        pygame.time.delay(2000)
        exit(0)
        
    inkq(a)

def Check() :
    # 3 Hang ngang
    if a[0][0] != ' ' and a[0][0] == a[0][1] and a[0][0] == a[0][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (50, 50), (50, 250), 10)
        return True
    if a[1][0] != ' ' and a[1][0] == a[1][1] and a[1][0] == a[1][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (150, 50), (150, 250), 10)
        return True
    if a[2][0] != ' ' and a[2][0] == a[2][1] and a[2][0] == a[2][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (250, 50), (250, 250), 10)
        return True
    # 3 Hang doc
    if a[0][0] != ' ' and a[0][0] == a[1][0] and a[0][0] == a[2][0] :
        pygame.draw.line(DISPLAYSURF, BLACK, (50, 50), (250, 50), 10)
        return True
    if a[0][1] != ' ' and a[0][1] == a[1][1] and a[0][1] == a[2][1] :
        pygame.draw.line(DISPLAYSURF, BLACK, (50, 150), (250, 150), 10)
        return True
    if a[0][2] != ' ' and a[0][2] == a[1][2] and a[0][2] == a[2][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (50, 250), (250, 250), 10)
        return True
    # 2 Duong cheo
    if a[0][0] != ' ' and a[0][0] == a[1][1] and a[0][0] == a[2][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (50, 50), (250, 250), 10)
        return True
    if a[2][0] != ' ' and a[2][0] == a[1][1] and a[2][0] == a[0][2] :
        pygame.draw.line(DISPLAYSURF, BLACK, (250, 50), (50, 250), 10)
        return True
    return False

def Full() :
    for i in a :
        for j in i :
            if j == ' ' :
                return False
    return True

def main() :
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit() 
                exit(0) 
            if event.type == pygame.MOUSEBUTTONDOWN :
                if pygame.mouse.get_pressed()[0] :
                    vt = pygame.mouse.get_pos()
                    click(vt[0] // 100, vt[1] // 100)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    pygame.quit() 
                    exit(0)
        
if __name__ == '__main__' :
    main()