num3 = 0
num5 = 0
sum3 = 0
sum5 = 0
for num3 in range(0,1000,3):
    sum3 = sum3 + num3
    
for num5 in range(0,1000,5):
	if num5 % 3 == 0:
		sum5 = sum5 + 0
	else:
	    sum5 = sum5 + num5
print (sum3+sum5)    
input("Press any key to quit:")    