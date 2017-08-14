import Testing
import NeuralNetUtil
import NeuralNet

print "testPenData"
tempList = []
i = 0
while i < 5:
	print "running iteration #", i+1
	nnet, testAccuracy = Testing.testPenData()
	tempList.append(testAccuracy)
	i = i + 1

print "accuracy average:", Testing.average(tempList)
print "accuracy standard deviation:", Testing.stDeviation(tempList)
print "max accuracy:", max(tempList)

print "testCarData"
tempList = []
i = 0
while i < 5:
	print "running iteration #", i+1
	nnet, testAccuracy = Testing.testCarData()
	tempList.append(testAccuracy)
	i = i + 1

print "accuracy average:", Testing.average(tempList)
print "accuracy standard deviation:", Testing.stDeviation(tempList)
print "max accuracy:", max(tempList)
