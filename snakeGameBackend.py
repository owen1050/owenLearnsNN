import random

class SnakeGame:
    def __init__(self):
        self.snake = [[2,0]]
        self.snakeDirection = 1
        self.gameOver = False
        self.WIDTH = 20
        self.HEIGHT = 30
        self.fruitPos = [int(self.WIDTH/2), int(self.HEIGHT/2)]
        self.score = 0
        self.steps = 0

    def setSnake(self, snake):
        self.snake = snake

    def setSnakeDirection(self, snakeD):
        self.snakeDirection = snakeD

    def setGameOver(self, go):
        self.gameOver = go

    def setWidth(self, w):
        self.WIDTH = w

    def setWidth(self, h):
        self.HEIGHT = h


    def incSnake(self):
        self.steps = self.steps + 1
        curr = self.snake[0]
            
        if self.snakeDirection == 0:
            new = [curr[0] + 0, curr[1] - 1]

        if self.snakeDirection == 1:
            new = [curr[0] + 1, curr[1] + 0]

        if self.snakeDirection == 2:
            new = [curr[0] + 0, curr[1] + 1]

        if self.snakeDirection == 3:
            new = [curr[0] - 1, curr[1] + 0]

        if new[0] > self.WIDTH - 1 or new[0] < 0 or new[1] > self.HEIGHT - 1 or new[1] < 0 or new in self.snake:
            self.gameOver = True

        if new == self.fruitPos:
            nfx = random.randint(0, self.WIDTH-1)
            nfy = random.randint(0, self.HEIGHT-1)
            self.fruitPos = [nfx, nfy]
            newSnake = self.snake[:]
            self.score = self.score + 1
            self.steps = 0
        else:
            newSnake = self.snake[:-1]

        newSnake.insert(0,new)
        self.snake = newSnake

        if self.steps > 100 * (self.score + 1):
            self.gameOver = True

    def getData(self):
        d1 = self.distToFruit()
        d2 = self.distToObs()
        return d1 + d2

    def distToFruit(self):
        r = self.fruitPos[0] - self.snake[0][0]
        l = self.snake[0][0] - self.fruitPos[0]

        u = self.fruitPos[1] - self.snake[0][1]
        d = self.snake[0][1] - self.fruitPos[1]
        return r, l, u, d

    def distToObs(self):
        x = self.snake[0][0]
        y = self.snake[0][1]
        minR = 50
        minL = 50
        minU = 50
        minD = 50
        for s in self.snake:
            if s[1] == y:
                if s[0] - x < minR and s[0] - x > 0:
                    minR = s[0] - x

                if x -  s[0] < minL and x -  s[0] > 0:
                    minL = x - s[0]

            if s[0] == x:
                if s[1] - y < minD and s[1] - y > 0:
                    minD = s[1] - y

                if y -  s[1] < minU and y -  s[1] > 0:
                    minU = y - s[1]

        if minR > self.WIDTH - x:
            minR = self.WIDTH - x

        if minL > x:
            minL = x 

        if minD > self.HEIGHT - y:
            minD = self.HEIGHT - y

        if minU > y:
            minU = y

        return minR, minL, minU, minD
