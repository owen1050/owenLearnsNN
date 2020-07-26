import networkUtil

networks = []
numNetPerGen = 5

nu = networkUtil.NetworkUtil()

n1 = nu.genAllOnesNetwork([[2,16], [16,16], [16,4]])

bias, weights = nu.getBiasAndWeights(n1)

for i in range(numNetPerGen):
    networks.append(nu.genRandomNetworkBasedOffBiasAndWeight(bias, weights, 0.2))

for network in networks:
    print(network, network.prop([1,2]))