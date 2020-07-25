from node import Node

class Layer:
    def __init__(self, numInputs = 1, numNodes = 1):
        self.nodes = []
        for i in range(numNodes):
            newNode = Node(bias = 0, numInputs = numInputs)
            self.nodes.append(newNode)

    def __str__(self):
        return "This is a layer with " + str(len(self.nodes)) + " nodes which each have " + str(len(self.nodes[0].weights)) + " inputs"

    def getOutputs(self, inputs):
        outputs = []
        for node in self.nodes:
            outputs.append(node.getOutput(inputs))

        return outputs

    def setAllBias(self, bias):
        for node in self.nodes:
            node.setBias(bias)
