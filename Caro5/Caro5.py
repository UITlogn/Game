LINK = 'D:'

import pygame, sys, random
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

XXX = pygame.image.load(LINK+'\\VScode\\PYTHON\Game\\Caro5\\X.png')
OOO = pygame.image.load(LINK+'\\VScode\\PYTHON\Game\\Caro5\\O.png')
DISPLAYSURF = pygame.display.set_mode((600, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Caro (30x30_5) - cuberlong')
pygame.init()
for i in range(1, 30) :
    pygame.draw.line(DISPLAYSURF, BLACK, (0, i*20), (600, i*20), 1)
    pygame.draw.line(DISPLAYSURF, BLACK, (i*20, 0), (i*20, 600), 1)

a = [[' ' for i in range(40)] for i in range(40)]
luot = bool(random.randint(1, 100)%2)

def inkq(a) :
    for i in range(30) :
        for j in range(30) :
            print(a[j][i], end = ' ')
        print("|")
    print('_____________________________')

def click(x, y) :
    global a, luot, DISPLAYSURF
    autoexit = True
    print('Click pos:', x, y, end = ' : ')
    if a[x][y] != ' ' :
        print('false!')
        return
    if luot == 1 :
        print('X -> ')
        a[x][y] = 'X'
        DISPLAYSURF.blit(XXX, (x*20+1, y*20+1))
        pygame.display.update()
    else :
        print('O -> ')
        a[x][y] = 'O'
        DISPLAYSURF.blit(OOO, (x*20+1, y*20+1))
        pygame.display.update()

    if Check(x, y) == True :
        if luot == 1 :
            print('X WIN!!!')
            font = pygame.font.SysFont('consolas', 20, 2)
            commentSuface = font.render('X WIN !!!', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            DISPLAYSURF.blit(commentSuface, (0, 0))
            pygame.display.update()
            pygame.time.delay(10000)
            exit(0)
        else :
            print('O WIN!!!')
            font = pygame.font.SysFont('consolas', 20, 2)
            commentSuface = font.render('O WIN !!!', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            DISPLAYSURF.blit(commentSuface, (0, 0))
            pygame.display.update()
            pygame.time.delay(10000)
            exit(0)
    if Full() == True :
        print('Full without winer')
        font = pygame.font.SysFont('consolas', 20, 2)
        commentSuface = font.render('DRAW !!!', True, (0, 0, 0))
        commentSize = commentSuface.get_size()
        DISPLAYSURF.blit(commentSuface, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        exit(0)

    luot = (luot+1)%2
    inkq(a)

def check2(a1, a2, b1, b2, c1, c2, d1, d2, e1, e2) :
    if a[a1][a2] != ' ' :
        if a[a1][a2] == a[b1][b2] :
            if a[a1][a2] == a[c1][c2] :
                if a[a1][a2] == a[d1][d2] :
                    if a[a1][a2] == a[e1][e2] :
                        pygame.draw.line(DISPLAYSURF, BLACK, (a1*20+10, a2*20+10), (e1*20+10, e2*20+10), 5)
                        return True
    return False

def Check(x, y) :
    # 5 Hang ngang
    if check2(x, y, x+1, y, x+2, y, x+3, y, x+4, y) == True:
        return True
    if check2(x-1, y, x, y, x+1, y, x+2, y, x+3, y) == True:
        return True
    if check2(x-2, y, x-1, y, x, y, x+1, y, x+2, y) == True:
        return True
    if check2(x-3, y, x-2, y, x-1, y, x, y, x+1, y) == True:
        return True
    if check2(x-4, y, x-3, y, x-2, y, x-1, y, x, y) == True:
        return True
    # 5 Hang doc
    if check2(x, y, x, y+1, x, y+2, x, y+3, x, y+4) == True:
        return True
    if check2(x, y-1, x, y, x, y+1, x, y+2, x, y+3) == True:
        return True
    if check2(x, y-2, x, y-1, x, y, x, y+1, x, y+2) == True:
        return True
    if check2(x, y-3, x, y-2, x, y-1, x, y, x, y+1) == True:
        return True
    if check2(x, y-4, x, y-3, x, y-2, x, y-1, x, y) == True:
        return True
    # 5 Duong cheo \
    if check2(x, y, x+1, y+1, x+2, y+2, x+3, y+3, x+4, y+4) == True:
        return True
    if check2(x-1, y-1, x, y, x+1, y+1, x+2, y+2, x+3, y+3) == True:
        return True
    if check2(x-2, y-2, x-1, y-1, x, y, x+1, y+1, x+2, y+2) == True:
        return True
    if check2(x-3, y-3, x-2, y-2, x-1, y-1, x, y, x+1, y+1) == True:
        return True
    if check2(x-4, y-4, x-3, y-3, x-2, y-2, x-1, y-1, x, y) == True:
        return True
    # 5 Duong cheo /
    if check2(x, y, x+1, y-1, x+2, y-2, x+3, y-3, x+4, y-4) == True:
        return True
    if check2(x-1, y+1, x, y, x+1, y-1, x+2, y-2, x+3, y-3) == True:
        return True
    if check2(x-2, y+2, x-1, y+1, x, y, x+1, y-1, x+2, y-2) == True:
        return True
    if check2(x-3, y+3, x-2, y+2, x-1, y+1, x, y, x+1, y-1) == True:
        return True
    if check2(x-4, y+4, x-3, y+3, x-2, y+2, x-1, y+1, x, y) == True:
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
                    click(vt[0] // 20, vt[1] // 20)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    pygame.quit() 
                    exit(0)    
        
if __name__ == '__main__' :
    main()