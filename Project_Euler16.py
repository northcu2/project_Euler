initial = 2**1000
sumx = sum(map(int, str(initial))) 
# The map and sum are both built in functions of Python,
# The map function seems to turn the int x in to a string of single digits.
# The map function then seems to be turning those strings into int data types.
# The sum function then adds up all of this single digit integers,
# thus solving the problem. 
print(sumx)
input("Press any key to quit:")