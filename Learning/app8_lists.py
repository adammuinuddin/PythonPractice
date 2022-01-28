#Learning about lists

a = ["adam", 3, 10, "i", -1]
print(a)
a.append("hello my name is adam")
a.append(123123)
print(a)
a.append([1,3,5,7,9])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[2])

b = ["banana", "apple", "microsoft"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp 
print(b)
