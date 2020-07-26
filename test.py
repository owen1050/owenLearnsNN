import snakeGameBackend

game = snakeGameBackend.SnakeGame()

print(game.snake[0])

minR, minL, minU, minD = game.distToObs()

print(minR, minL, minU, minD)

fruitX, fruitY = game.distToFruit()

print(game.fruitPos)

print(fruitX, fruitY)

print(game.score)