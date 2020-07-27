import pygame, time, random, snakeGameBackend
from pygame.locals import *

game = snakeGameBackend.SnakeGame()

#pygame init
GAMESIZE = 25
WINDOW_WIDTH = game.WIDTH * GAMESIZE
WINDOW_HEIGHT = game.HEIGHT * GAMESIZE
BLACK = (0,0,0)
WHITE = (255, 255, 255)

score = 0

pygame.init()

gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

fruitPic = pygame.image.load('fruit.png')
snakePic = pygame.image.load("snake.png")

def checkKeys(event):
    global game
    #print(event)
    if event.find("KeyDown") > 0:
        if event.find("1073741906") > 0:
            game.setSnakeDirection(0)

        if event.find("1073741903") > 0:
            game.setSnakeDirection(1)

        if event.find("1073741905") > 0:
            game.setSnakeDirection(2)

        if event.find("1073741904") > 0:
            game.setSnakeDirection(3)

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

while not game.gameOver:
    tickCounter = tickCounter + 1
    gameDisplay.fill(BLACK)

    for s in game.snake:
        gameDisplay.blit(snakePic, (s[0] * GAMESIZE, s[1] * GAMESIZE))

    gameDisplay.blit(fruitPic, (game.fruitPos[0] * GAMESIZE, game.fruitPos[1] * GAMESIZE))
    dispScore()

    pygame.display.update()

    if tickCounter > 4:
        game.incSnake()
        tickCounter = 0

    if game.score > 3:
        tickRate = 60
    
    for event in pygame.event.get():
        checkKeys(str(event))
        if event.type == pygame.QUIT:
            game.gameOver = True

    clock.tick(tickRate)
    
exit()
