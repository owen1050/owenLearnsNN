import snakeGameBackend, networkUtil, time, pyGameSnake, threading

game = snakeGameBackend.SnakeGame()

nu = networkUtil.NetworkUtil()

networks = []
numNetPerGen = 100

nu = networkUtil.NetworkUtil()

n1 = nu.genAllNNetwork([[8,32], [32,32], [32,32], [32,4]], 1)
bestNetworks = [n1]

generation = 0

while True:
    generation = generation + 1
    bias, weights = nu.getBiasAndWeights(bestNetworks[0])
    networks = []
    
    for i in range(numNetPerGen):
        networks.append(nu.genRandomNetworkBasedOffBiasAndWeight(bias, weights, 10))
    
    networks = networks + bestNetworks

    grades = []
    for net in networks:
        game = snakeGameBackend.SnakeGame()
        inc = 0
        while not game.gameOver:
            res = net.prop(game.getData())
            game.setSnakeDirection(res.index(max(res)))
            game.incSnake()
            #print("Head at: ", game.snake[0], "\t Direction: ", game.snakeDirection, "\t Data: " , res)
            inc = inc + 1

        grade = game.score * 100 + inc
        
        grades.append(game.score * 100 + inc)


    bestGrade = max(grades)
    bestGradeIndex = grades.index(bestGrade)
    net = networks[bestGradeIndex]

    pyGame = pyGameSnake()

    while not pyGame.game.gameOver:
        res = net.prop(pyGame.game.getData())
        pyGame.game.setSnakeDirection(res.index(max(res)))


    bestNetworks = []
    while len(bestNetworks) < numNetPerGen / 10:
        mi = grades.index(max(grades))
        bestNetworks.append(networks[mi])
        grades.pop(mi)
        networks.pop(mi)

    print("The best grade for generation", generation ,"was" , bestGrade)