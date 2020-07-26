import pygame, time, random, snakeGameBackend
from pygame.locals import *



#snake init
WIDTH = 20
HEIGHT = 30

gameOver = False
snake = [(1,1),(1,0),(0,0)]
snakeDirection = 1 #0 is up, 1 is right, 2 is down, 3 is left
fruitPos = (int(WIDTH/2), int(HEIGHT/2))
score = 0

#pygame init
GAMESIZE = 25
WINDOW_WIDTH = WIDTH * GAMESIZE
WINDOW_HEIGHT = HEIGHT * GAMESIZE
BLACK = (0,0,0)
WHITE = (255, 255, 255)

pygame.init()

gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

fruitPic = pygame.image.load('fruit.png')
snakePic = pygame.image.load("snake.png")

def checkKeys(event):
    global snakeDirection
    print(event)
    if event.find("KeyDown") > 0:
        if event.find("1073741906") > 0:
            snakeDirection = 0

        if event.find("1073741903") > 0:
            snakeDirection = 1

        if event.find("1073741905") > 0:
            snakeDirection = 2

        if event.find("1073741904") > 0:
            snakeDirection = 3

def text_objects(text, font):
    global WHITE
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def dispScore():
    global gameDisplay, score
    largeText = pygame.font.Font('font.ttf',25)
    TextSurf, TextRect = text_objects(str(score), largeText)
    TextRect.center = (13,13)
    gameDisplay.blit(TextSurf, TextRect)

tickCounter = 0
tickRate = 40

while not gameOver:
    tickCounter = tickCounter + 1
    gameDisplay.fill(BLACK)

    for s in snake:
        gameDisplay.blit(snakePic, (s[0] * GAMESIZE, s[1] * GAMESIZE))

    gameDisplay.blit(fruitPic, (fruitPos[0] * GAMESIZE, fruitPos[1] * GAMESIZE))
    dispScore()

    pygame.display.update()

    if tickCounter > 5:
        snakeGameBackend.incSnake()
        tickCounter = 0
    if score > 3:
        tickRate = 60
    
    for event in pygame.event.get():
        checkKeys(str(event))
        if event.type == pygame.QUIT:
            gameOver = True

    clock.tick(tickRate)
    

pygame.quit()
quit()