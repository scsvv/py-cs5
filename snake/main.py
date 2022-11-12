import pygame
from pygame.locals import *
from sys import exit 
from random import randint 

# SYSTEM VAR
SIZE = (720, 480)
FPS = pygame.time.Clock()


# COLOR VAR
black = (0, 0, 0)
white = (255, 255, 255)

# GAME PROCESS VAR
SPEED = 30
DIRECTION = [SPEED, 0]
# GAME OBJECT VAR
head = Rect(400, 300, 30, 30)


pygame.init()
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode(SIZE)

def move(obj):
    global DIRECTION, SPEED, KEYS

    if KEYS[K_UP] or KEYS[K_w]: 
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] or KEYS[K_s]: 
        DIRECTION = [0, SPEED]
    elif KEYS[K_LEFT] or KEYS[K_a]: 
        DIRECTION = [-SPEED, 0]
    elif KEYS[K_RIGHT] or KEYS[K_d]: 
        DIRECTION = [SPEED, 0]

    if obj.bottom > 510:
        obj.top = -10
    elif obj.top < -30:
        obj.bottom = 490
    elif obj.left < -30:
        obj.right = 730
    elif obj.right > 750:
        obj.left = -10 
        
    
    obj.move_ip(DIRECTION)

while True: 
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    KEYS = pygame.key.get_pressed()
    pygame.draw.rect(screen, white, head)
    move(head)
    pygame.display.update()
    FPS.tick(10)




