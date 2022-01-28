#ask user for a number and tell them is it is odd or even
user_number = int(input("Type in a number: "))
function = user_number % 2
if function == 0:
    print("Your number", user_number, "is even")
else:
    print("Your number", user_number, "is odd")