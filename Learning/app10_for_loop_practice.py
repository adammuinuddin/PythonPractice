#Practice with for loops
from random import randint

x = randint(1,10)
print(x)
user_guess = 0

while user_guess != x:
    user_guess = int(input("Guess the number you think the computer chose: "))
print("Good guess!")

