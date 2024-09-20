LINK = 'D:'

import pygame, sys, random
from pygame.locals import *

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
pygame.display.update()

a = [[' ' for i in range(3)] for i in range(3)]

# co so du lieu :
th = [[[' ' for i in range(3)] for i in range(3)] for i in range(26)]
xuli = [(0, 0) for i in range(26)]
# Buoc 1
th[0] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']]; xuli[0] = (1, 1)
th[1] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', 'X', ' ']]; xuli[1] = (1, 1)
th[2] = [[' ', ' ', ' '], [' ', ' ', ' '], ['X', ' ', ' ']]; xuli[2] = (1, 1)
th[3] = [[' ', ' ', ' '], [' ', ' ', 'X'], [' ', ' ', ' ']]; xuli[3] = (1, 1)
th[4] = [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]; xuli[4] = (0, 0)
th[5] = [[' ', ' ', ' '], ['X', ' ', ' '], [' ', ' ', ' ']]; xuli[5] = (1, 1)
th[6] = [[' ', ' ', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]; xuli[6] = (1, 1)
th[7] = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]; xuli[7] = (1, 1)
th[8] = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]; xuli[8] = (1, 1)
# Buoc 2
th[9] = [['O', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]; xuli[9] = (0, 2)
th[10] = [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'X']]; xuli[10] = (0, 1)
th[11] = [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'X', ' ']]; xuli[11] = (2, 0)
th[12] = [['X', ' ', ' '], [' ', 'O', 'X'], [' ', ' ', ' ']]; xuli[12] = (0, 2)
th[13] = [[' ', 'X', ' '], [' ', 'O', ' '], [' ', ' ', 'X']]; xuli[13] = (0, 2)
th[14] = [[' ', 'X', ' '], [' ', 'O', ' '], [' ', 'X', ' ']]; xuli[14] = (0, 0)
th[15] = [[' ', 'X', ' '], [' ', 'O', ' '], ['X', ' ', ' ']]; xuli[15] = (0, 0)
th[16] = [[' ', 'X', ' '], [' ', 'O', 'X'], [' ', ' ', ' ']]; xuli[16] = (0, 2)
th[17] = [[' ', 'X', ' '], ['X', 'O', ' '], [' ', ' ', ' ']]; xuli[17] = (0, 0)
th[18] = [[' ', ' ', 'X'], [' ', 'O', ' '], [' ', 'X', ' ']]; xuli[18] = (2, 2)
th[19] = [[' ', ' ', 'X'], [' ', 'O', ' '], ['X', ' ', ' ']]; xuli[19] = (0, 1)
th[20] = [[' ', ' ', 'X'], ['X', 'O', ' '], [' ', ' ', ' ']]; xuli[20] = (0, 0)
th[21] = [[' ', ' ', ' '], ['X', 'O', ' '], [' ', ' ', 'X']]; xuli[21] = (2, 0)
th[22] = [[' ', ' ', ' '], ['X', 'O', ' '], [' ', 'X', ' ']]; xuli[22] = (2, 0)
th[23] = [[' ', ' ', ' '], ['X', 'O', 'X'], [' ', ' ', ' ']]; xuli[23] = (0, 0)
th[24] = [[' ', ' ', ' '], [' ', 'O', 'X'], [' ', 'X', ' ']]; xuli[24] = (2, 2)
th[25] = [[' ', ' ', ' '], [' ', 'O', 'X'], ['X', ' ', ' ']]; xuli[25] = (2, 2)
#####################################################################################
def inkq(a) :
    print(a)
    for i in range(3) :
        for j in range(3) :
            print(a[j][i], end = ' ')
        print()
    print('_____________________________')

def ktra(x, y) :
    if a[x][y] == ' ' :
        return True
    return False

def ngaunhien() :
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while a[x][y] != ' ' :
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    return (x, y)

def chan() :
    if a[0] == ['X', 'X', ' '] :
        return (0, 2)
    if a[1] == ['X', 'X', ' '] :
        return (1, 2)
    if a[2] == ['X', 'X', ' '] :
        return (2, 2)
    if a[0] == ['X', ' ', 'X'] :
        return (0, 1)
    if a[1] == ['X', ' ', 'X'] :
        return (1, 1)
    if a[2] == ['X', ' ', 'X'] :
        return (2, 1)
    if a[0] == [' ', 'X', 'X'] :
        return (0, 0)
    if a[1] == [' ', 'X', 'X'] :
        return (1, 0)
    if a[2] == [' ', 'X', 'X'] :
        return (2, 0)
    if a[0][0] == 'X' and a[1][0] == 'X' and a[2][0] == ' ' :
        return (2, 0)
    if a[0][0] == 'X' and a[2][0] == 'X' and a[1][0] == ' ' :
        return (1, 0)
    if a[2][0] == 'X' and a[1][0] == 'X' and a[0][0] == ' ' :
        return (0, 0)
    if a[0][1] == 'X' and a[1][1] == 'X' and a[2][1] == ' ' :
        return (2, 1)
    if a[0][1] == 'X' and a[2][1] == 'X' and a[1][1] == ' ' :
        return (1, 1)
    if a[2][1] == 'X' and a[1][1] == 'X' and a[0][1] == ' ' :
        return (0, 1)
    if a[0][2] == 'X' and a[1][2] == 'X' and a[2][2] == ' ' :
        return (2, 2)
    if a[0][2] == 'X' and a[2][2] == 'X' and a[1][2] == ' ' :
        return (1, 2)
    if a[2][2] == 'X' and a[1][2] == 'X' and a[0][2] == ' ' :
        return (0, 2)
    if a[0][0] == 'X' and a[2][2] == 'X' and a[1][1] == ' ' :
        return (1, 1)
    if a[1][1] == 'X' and a[2][2] == 'X'  and a[0][0] == ' ':
        return (0, 0)
    if a[0][0] == 'X' and a[1][1] == 'X'  and a[2][2] == ' ':
        return (2, 2)
    if a[0][2] == 'X' and a[1][1] == 'X'  and a[2][0] == ' ':
        return (2, 0)
    if a[0][2] == 'X' and a[2][0] == 'X'  and a[1][1] == ' ':
        return (1, 1)
    if a[2][0] == 'X' and a[1][1] == 'X'  and a[0][2] == ' ':
        return (0, 2)
    return (3, 3)

def cwin() :
    if a[0] == ['O', 'O', ' '] :
        return (0, 2)
    if a[1] == ['O', 'O', ' '] :
        return (1, 2)
    if a[2] == ['O', 'O', ' '] :
        return (2, 2)
    if a[0] == ['O', ' ', 'O'] :
        return (0, 1)
    if a[1] == ['O', ' ', 'O'] :
        return (1, 1)
    if a[2] == ['O', ' ', 'O'] :
        return (2, 1)
    if a[0] == [' ', 'O', 'O'] :
        return (0, 0)
    if a[1] == [' ', 'O', 'O'] :
        return (1, 0)
    if a[2] == [' ', 'O', 'O'] :
        return (2, 0)
    if a[0][0] == 'O' and a[1][0] == 'O' and a[2][0] == ' ' :
        return (2, 0)
    if a[0][0] == 'O' and a[2][0] == 'O' and a[1][0] == ' ' :
        return (1, 0)
    if a[2][0] == 'O' and a[1][0] == 'O' and a[0][0] == ' ' :
        return (0, 0)
    if a[0][1] == 'O' and a[1][1] == 'O' and a[2][1] == ' ' :
        return (2, 1)
    if a[0][1] == 'O' and a[2][1] == 'O' and a[1][1] == ' ' :
        return (1, 1)
    if a[2][1] == 'O' and a[1][1] == 'O' and a[0][1] == ' ' :
        return (0, 1)
    if a[0][2] == 'O' and a[1][2] == 'O' and a[2][2] == ' ' :
        return (2, 2)
    if a[0][2] == 'O' and a[2][2] == 'O' and a[1][2] == ' ' :
        return (1, 2)
    if a[2][2] == 'O' and a[1][2] == 'O' and a[0][2] == ' ' :
        return (0, 2)
    if a[0][0] == 'O' and a[2][2] == 'O' and a[1][1] == ' ' :
        return (1, 1)
    if a[1][1] == 'O' and a[2][2] == 'O'  and a[0][0] == ' ':
        return (0, 0)
    if a[0][0] == 'O' and a[1][1] == 'O'  and a[2][2] == ' ':
        return (2, 2)
    if a[0][2] == 'O' and a[1][1] == 'O'  and a[2][0] == ' ':
        return (2, 0)
    if a[0][2] == 'O' and a[2][0] == 'O'  and a[1][1] == ' ':
        return (1, 1)
    if a[2][0] == 'O' and a[1][1] == 'O'  and a[0][2] == ' ':
        return (0, 2)
    return (3, 3)

def buoc1() :
    for i in range(9) :
        if a == th[i] :
            return xuli[i]
    return (3, 3)

def buoc2() :
    for i in range(9, 26) :
        if a == th[i] :
            return xuli[i]
    return (3, 3)

def AI() :
    t = buoc1()
    print(t)
    if t != (3, 3) :
        return t
    t = buoc2()
    print(t)
    if t != (3, 3) :
        return t
    t = cwin()
    print(t)
    if t != (3, 3) :
        return t
    t = chan()
    print(t)
    if t != (3, 3) :
        return t
    return ngaunhien()

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

    xy = AI()
    print('O -> ')
    a[xy[0]][xy[1]] = 'O'
    DISPLAYSURF.blit(OOO, (xy[0]*100+5, xy[1]*100+5))
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