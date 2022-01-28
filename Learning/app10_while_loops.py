#Learning about while loops

#Calculating the sum of 10
from re import X
from unicodedata import numeric


total = 0
j = 1
while j < 10:
    total += j
    j +=1

print (total)

#Given a list with an unknowable number of integers (that are descending and includes negative integers), write code that will calculate the sum of the positive integers
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
x = 0
total2 = 0
while given_list2[x] > 0:
    total2 += given_list2[x]
    x += 1

print(total2)

#Given a list with an unknowable number of integers (that are descending), write code that will calculate the sum of the positive integers
given_list3 = [5, 4, 4, 3, 1]
number_of_items3 = len(given_list3)
x = 0
total3 = 0
while True:
    total3 += given_list3[x]
    x += 1
    if (number_of_items3 - 1) >= x:
        break

print(total3)

#Given a list with an unknowable number of integers (that are descending and have negative integers), write code that will calculate the sum of the negative integers
given_list4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1 ,-2, -3, -4 -5 ,-6 , -7, -8 , -9, -10]
number_of_items4 = len(given_list4)
x = 0
total4 = 0
while number_of_items4 > x:
    if given_list4[x] < 0:
        total4 += given_list4[x]
    x += 1

print(total4)