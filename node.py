class Node:
    def __init__(self, bias = 0, numInputs = 1):
        self.bias = bias
        self.weights = []
        for i in range(numInputs):
            self.weights.append(0)

    def __str__(self):
        return "This is a node with bias " + str(self.bias) + " and weights " + str(self.weights)

    def setBias(self, bias):
        self.bias = bias

    def setAllWeights(self, weight):
        for i in range(len(self.weights)):
            self.weights[i] = weight

    def setWeights(self, weights):
        if len(self.weights) != len(weights):
            return "impossible, mismatch in weights length"
        else:
            self.weights = weights

    def setWeight(self, index, value):
        self.weights[index] = value

    def getOutput(self, inputs):
        out = 0
        for i in range(len(inputs)):
            out = out + self.weights[i] * inputs[i]
        
        out = out + self.bias
        return self.relu(out)

    def relu(self, input):
        if input < 0:
            return 0
        else:
            return input
