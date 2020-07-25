import layer

class Network:
    def __init__(self, layers):
        self.layers = []

        for lay in layers:
            numIn = lay[0]
            numN = lay[1]
            self.layers.append(layer.Layer(numInputs = numIn, numNodes = numN))

    def __str__(self):
        return "This is a network with " + str(len(self.layers)) + " layers"

    def prop(self, input):
        layIn = input
        for layer in self.layers:
            layIn = layer.getOutputs(layIn)
        return layIn