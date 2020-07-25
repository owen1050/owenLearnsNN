import network

n = network.Network([[2,4], [4,2]])
print(n)
for lay in n.layers:
    for node in lay.nodes:
        node.setBias(1)
        node.setAllWeights(1)

print(n.prop([1,1]))