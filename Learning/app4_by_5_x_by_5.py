#The purpose of this code is to find number which are divisible by 7 and a multiple of 5 between the number 1500 and 2700

for x in range (1500,2700,5):
    calculation = x % 7
    if calculation == 0:
        print(x)
