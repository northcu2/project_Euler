number = 1
test = 0
print("This calculation took 58.40 seconds on an i5 4300 - U clocked at 1.9GHz, please be patient.")
print("Calculating...")
while( test == 0):
    if number % 11 == 0 and number % 12 == 0 and number % 13 == 0 and number % 14 == 0 and number % 15 == 0 and number % 16  == 0 and number % 17 == 0 and number % 18 == 0 and number % 19 == 0 and number % 20 == 0:
        test += 1
        print(number)
    else:
        number += 1

input("Press any key to end.")
