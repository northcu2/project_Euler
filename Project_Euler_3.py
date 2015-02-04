numToTest = 2
testVar = 1
prime = 600851475143 
while testVar > 0 :
    if (prime % numToTest) != 0 :
        numToTest += 1


    else:
        prime = prime/numToTest

    if prime == numToTest:
        testVar = 0

print(numToTest)
input("Press any key to end.")