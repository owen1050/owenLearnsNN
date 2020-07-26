import random

def incSnake():
    global snake, snakeDirection, gameOver, WIDTH, HEIGHT, fruitPos, score
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
        score = score + 1
    else:
        newSnake = snake[:-1]

    newSnake.insert(0,new)
    snake = newSnake
