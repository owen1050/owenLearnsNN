import network, random

class NetworkUtil:
    def getBiasAndWeights(self, net):
        biases = []
        weights = []

        for lay in net.layers:
            layerBias = []
            layerWeight = []
            for node in lay.nodes:
                layerBias.append(node.bias)
                layerWeight.append(node.weights)

            biases.append(layerBias)
            weights.append(layerWeight)

        return biases, weights

    def genRandomNetworkBasedOffBiasAndWeight(self, biases, weights, mult):
        netParams = []

        for i in range(len(biases)):
            i0 = len(biases[i])
            i1 = len(weights[i][0])
            netParams.append([i1, i0])
        
        net = network.Network(netParams)

        nodeCount = 0
        layerCount = 0
        for lay in net.layers:
            nodeCount = 0
            for node in lay.nodes:
                node.setBias(biases[layerCount][nodeCount] + random.random()*mult-mult/2)
                oldWeights = weights[layerCount][nodeCount]
                newWeights = []
                for w in oldWeights:
                    newWeights.append(w + random.random()*mult-mult/2)
                node.setWeights(newWeights)
                nodeCount = nodeCount + 1
            layerCount = layerCount + 1

        return net

    def genAllNNetwork(self, param, n):
        net = network.Network(param)

        for lay in net.layers:
            for node in lay.nodes:
                numWeights = len(node.weights)
                node.setBias(n)
                weights = []
                for i in range(numWeights):
                    weights.append(n)
                node.setWeights(weights)

        return net