import pygame
from pygame.locals import *
from sys import exit 
from random import randint 

# SYSTEM VAR
SIZE = (1080, 720)
FPS = pygame.time.Clock()

# COLOR VAR
black = (0, 0, 0)
white = (255, 255, 255)

# GAME PROCESS VAR
SPEED = 20
DIRECTION = [0, SPEED]
POINTS = 0
# GAME OBJECT VAR

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Game")

game_music = pygame.mixer.Sound('./sound/gamesound.wav')
coin_sound = pygame.mixer.Sound('./sound/point.wav')
screen = pygame.display.set_mode(SIZE)
font = pygame.font.SysFont(None, 32)


game_music.set_volume(0.2)
coin_sound.set_volume(0.5)
def score():
    global POINTS
    text = font.render(f'Очки: {POINTS}', True, white)
    text_rect = text.get_rect(center=(SIZE[0]/2, SIZE[1]-SIZE[1]*0.05))
    screen.blit(text, text_rect)

def pickup():
    global apple_rect, head_rect, POINTS, snake

    if head_rect.colliderect(apple_rect): 
        apple_rect.x = randint(40, 700)
        apple_rect.y = randint(40, 440)
        snake.append(snake[1].copy())
        POINTS += 10
        coin_sound.play()

def game_over_event(): 
    global snake, head_rect

    for el in snake[1:]:
        if head_rect.colliderect(el):
            return True 
    return False 

def load_image(src, x, y): 
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (20, 20))
    rect = image.get_rect(center=(x, y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect

def move(obj, body):
    global DIRECTION, SPEED, KEYS

    if (KEYS[K_UP] or KEYS[K_w]) and DIRECTION[1] == 0: 
        DIRECTION = [0, -SPEED]
    elif (KEYS[K_DOWN] or KEYS[K_s]) and DIRECTION[1] == 0: 
        DIRECTION = [0, SPEED]
    elif (KEYS[K_LEFT] or KEYS[K_a]) and DIRECTION[0] == 0: 
        DIRECTION = [-SPEED, 0]
    elif (KEYS[K_RIGHT] or KEYS[K_d]) and DIRECTION[0] == 0: 
        DIRECTION = [SPEED, 0]

    if obj.bottom > SIZE[1] + 30:
        obj.top = -10
    elif obj.top < -30:
        obj.bottom = SIZE[1] - 10
    elif obj.left < -30:
        obj.right = SIZE[0] + 10
    elif obj.right > SIZE[0] + 30:
        obj.left = -10 
        
    for i in range(len(body) - 1, 0, -1):
        body[i].x = body[i-1].x
        body[i].y = body[i-1].y 

    
    obj.move_ip(DIRECTION)

# objects
head_image, head_rect = load_image('./img/head.png', 400, 300)
body_image, body_rect = load_image('./img/body.png', 400, 280)
apple_image, apple_rect = load_image('./img/apple.png', 200, 100) 

snake = [head_rect, body_rect]
game_music.play()
while True: 
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    if game_over_event():
        text = font.render(f'U LOSER', True, white)
        text_rect = text.get_rect(center=(SIZE[0]/2, SIZE[1]/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        FPS.tick(20)
        continue

    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)
    for el in snake[1:]: 
        screen.blit(body_image, el)
    move(head_rect, snake)
    pickup()
    score()


    pygame.display.update()
    FPS.tick(20)