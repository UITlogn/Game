LINK = 'D:'

import pygame
import sys
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
    
best = 0
score = 0 
speed = 10

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), rr)

class Snake(object):
    def __init__(self):
        self.length = 3
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 255, 0)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            global score, speed, best
            speed = 10
            if (score > best) :
                sys.stdout = open(LINK+'\\VScode\\PYTHON_3\\Game\\Snake\\best.txt', 'w')
                print(score)
                sys.stdout.close()
                best = score
            score = 0
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()            
            
    def reset(self):
        self.length = 3
        self.positions =  [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 255, 0), r, 1)
            
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 0), r, 2)

def main():
    sys.stdin = open(LINK+'\\VScode\\PYTHON_3\\Game\\Snake\\best.txt', 'r')
    global best
    best = int(input())
    sys.stdin.close()

    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()
    
    myfont = pygame.font.SysFont("consolas", 30)
    global speed
    while True:
        clock.tick(speed)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            speed += 0.5
            global score
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface) 
        screen.blit(surface, (0,0))

        text = myfont.render("Score {0}".format(score), 1, (255,255,255))
        screen.blit(text, (5, 10))

        text = myfont.render("Best {0}".format(best), 1, (255,255,255))
        screen.blit(text, (SCREEN_WIDTH-150, 10))

        pygame.display.update()

main()
