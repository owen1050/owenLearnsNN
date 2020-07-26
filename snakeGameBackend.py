import random

WIDTH = 20
HEIGHT = 30

gameOver = False
snake = [(1,1),(1,0),(0,0)]
snakeDirection = 1 #0 is up, 1 is right, 2 is down, 3 is left
fruitPos = (8,1) #(int(WIDTH/2), int(HEIGHT/2))


def incSnake():
    global snake, snakeDirection, gameOver, WIDTH, HEIGHT, fruitPos
    curr = snake[0]
        
    if snakeDirection == 0:
        new = (curr[0] + 0, curr[1] - 1)

    if snakeDirection == 1:
        new = (curr[0] + 1, curr[1] + 0)

    if snakeDirection == 2:
        new = (curr[0] + 0, curr[1] + 1)

    if snakeDirection == 3:
        new = (curr[0] - 1, curr[1] + 0)

    if new[0] > WIDTH - 1 or new[0] < 0 or new[1] > HEIGHT - 1 or new[1] < 0 or new in snake:
        gameOver = True

    if new == fruitPos:
        nfx = random.randint(0, WIDTH-1)
        nfy = random.randint(0, HEIGHT-1)
        fruitPos = (nfx, nfy)
        newSnake = snake[:]
    else:
        newSnake = snake[:-1]

    newSnake.insert(0,new)
    snake = newSnake



while gameOver == False:
    print(snake)
    incSnake()
