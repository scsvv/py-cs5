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
SPEED = 20
DIRECTION = [SPEED, 0]
POINTS = 0
# GAME OBJECT VAR

pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode(SIZE)
font = pygame.font.SysFont(None, 32)

def score():
    global POINTS
    text = font.render(f'Очки: {POINTS}', True, white)
    text_rect = text.get_rect(center=(360, 460))
    screen.blit(text, text_rect)

def pickup():
    global apple_rect, head_rect, POINTS

    if head_rect.colliderect(apple_rect): 
        apple_rect.x = randint(40, 700)
        apple_rect.y = randint(40, 440)
        POINTS += 10

def load_image(src, x, y): 
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (20, 20))
    rect = image.get_rect(center=(x, y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect

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

# objects
head_image, head_rect = load_image('./img/head.png', 400, 300)
apple_image, apple_rect = load_image('./img/apple.png', 200, 100) 

while True: 
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)
    move(head_rect)
    pickup()
    score()
    pygame.display.update()
    FPS.tick(20)