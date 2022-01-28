#Learning about for loops
a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)

b = [20, 10, 5]
total = 0
for element in b:
    total = total + element
print(total)

c = list(range(1,10))
print(c)

total2 = 0
for i in range(1,5):
    total2 += i
print(total2)

total3 = 0
for i in range(1,8):
    if i% 3 == 0:
        total3 += i
print(total3)

total4=0
for number in range(1,100):
    if number % 3 == 0:
        total4 += number
    elif number % 5 == 0:
        total4 += number

print(total4)
