import snakeGameBackend, networkUtil, time

game = snakeGameBackend.SnakeGame()

nu = networkUtil.NetworkUtil()

networks = []
numNetPerGen = 100

nu = networkUtil.NetworkUtil()

n1 = nu.genAllNNetwork([[8,32], [32,32], [32,32], [32,4]], 1)
bestNetworks = [n1]

while True:
    bias, weights = nu.getBiasAndWeights(bestNetworks[0])
    networks = []
    
    for i in range(numNetPerGen):
        networks.append(nu.genRandomNetworkBasedOffBiasAndWeight(bias, weights, 4))
    num = 10
    if len(bestNetworks) < 10:
        num = len(bestNetworks)
    networks = networks + bestNetworks[0:num-1]

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
    bestNetworks = []
    for gi in range(len(grades)):
        if grades[gi] == bestGrade:
            bestNetworks.append(networks[gi])

    print(bestGrade, len(bestNetworks), len(networks))
    #print(bias, weights)