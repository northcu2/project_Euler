sumOfSquares = 0
squareOfSums = 0
for x in range(0,101):
    sumOfSquares = (x**2) + sumOfSquares
for y in range(0,101):
    squareOfSums = y + squareOfSums
print(((squareOfSums)**2)-(sumOfSquares))

input("Press any key to end:")