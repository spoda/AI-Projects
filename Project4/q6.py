import Testing
import NeuralNetUtil
import NeuralNet


print "TestPenData"

neurons = 0
while neurons <= 40:
	print" neurons running: ", neurons
	tempList = []
	i = 0
	while i < 5:
		print "iteration: ", i+1
		nnet, testAccuracy = Testing.buildNeuralNet(Testing.penData, maxItr = 200, hiddenLayerList = [neurons])
		tempList.append(testAccuracy)
		i = i + 1

	print "accuracy average:", Testing.average(tempList)
	print "accuracy standard deviation:", Testing.stDeviation(tempList)
	print "max accuracy:", max(tempList)
	neurons = neurons + 5
	
print " "
print "TestCarData"

neurons = 0
while neurons <= 40:
	print" neurons running: ", neurons
	tempList = []
	i = 0
	while i < 5:
		print "iteration: ", i+1
		nnet, testAccuracy = Testing.buildNeuralNet(Testing.carData, maxItr = 200, hiddenLayerList = [neurons])
		tempList.append(testAccuracy)
		i = i + 1

	print "accuracy average:", Testing.average(tempList)
	print "accuracy standard deviation:", Testing.stDeviation(tempList)
	print "max accuracy:", max(tempList)
	neurons = neurons + 5
