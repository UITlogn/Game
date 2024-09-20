import pygame, sys
from pygame.locals import *
import random

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Draw')

# https://teamvietdev.com/bang-ma-mau-rbg-hex-thong-dung/
# Tạo sẵn các màu sắc
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

COLOR = [BLACK, WHITE, RED, GREEN, BLUE, PINK, YELLOW, ORANGE, AQUA, SILVER, GRAY, MAROON, OLIVE, GREEND, PURPLE, TEAL, NAVY]
def Randcolor(BWRGB) :
    if BWRGB == 1 :
        return COLOR[random.randint(0, 4)]
    return COLOR[random.randint(0, 16)]

DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, RED, (10, 10, 100, 50))# Hình chữ nhật
pygame.draw.rect(DISPLAYSURF, GREEN, (150, 10, 100, 50), 2)# Hình chữ nhật rỗng
pygame.draw.circle(DISPLAYSURF, RED, (50, 100), 20) # Hình tròn
pygame.draw.circle(DISPLAYSURF, BLUE, (200, 100), 20, 1)# Hình tròn rỗng
pygame.draw.ellipse(DISPLAYSURF, RED, (10, 150, 100, 50))# Hình elip
pygame.draw.ellipse(DISPLAYSURF, GREEN, (150, 150, 100, 50), 3)# Hình elip rỗng
pygame.draw.polygon(DISPLAYSURF, RED, ((10, 220), (150, 230), (100 ,290), (30, 270)))# Đa giác
pygame.draw.polygon(DISPLAYSURF, BLUE, ((160, 220), (300, 230), (250 ,290), (180, 270)), 2)# Đa giác rỗng
pygame.draw.line(DISPLAYSURF, BLACK, (300, 50), (350, 150), 4)# Đoạn thẳng
pygame.display.update()

while True:
    '''for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()'''
    
    pygame.draw.circle(DISPLAYSURF, Randcolor(0), (50, 100), 20)
    pygame.display.update()
    pygame.time.delay(1000)