#Creating the wordle game

#Importing the possible wordle words
with open("Learning/wordle-allowed-guesses.txt") as wordlefile:
    lines = wordlefile.readlines()

#Creating a list of the possible wordle words
wordlewordlist = []
for x in range(len(lines)):
    word = lines[x]
    word = word[0:5]
    wordlewordlist.append(word)

#Choosing the wordle word of the day 
import random
wordlewordoftheday = random.choice(wordlewordlist)
print(wordlewordoftheday)

#Checking letters and position
#Checking letters
def letter_check(letter, wod):
    for j in range(5):
        if letter == wod[j]:
            if j == 0:
                return True
            else:
                return j
    return False



#Creating the game
#Asking user for input (6 guesses)
for guess in range(6): 
    if guess == 0:
        print("\n \nThis is your", guess+1,"st out of 6 guesses")
    if guess == 1:
        print("\n \nThis is your", guess+1,"nd out of 6 guesses")
    if guess == 2:
        print("\n \nThis is your", guess+1,"rd out of 6 guesses")
    if guess > 2:
        print("\n \nThis is your", guess+1,"th out of 6 guesses")

    userguess = str(input("Type a 5 letter guess for the wordle word of the day: "))

    while len(userguess) != 5:
        print("Enter a valid guess")
        userguess = str(input("Enter your valid guess: "))
    
    #Checking if the word is right
    if userguess == wordlewordoftheday:
        print("\nCongratulations you solved the wordle word of the day!")
        exit()
    
    for i in range(5):
        
        letterInWord = letter_check(userguess[i], wordlewordoftheday)
        
        if  letterInWord != False:

            print("The letter: ",userguess[i], " is in the word")

            if userguess[i] == wordlewordoftheday[i]:
                print(" and it is in the correct place")
            else:
                print("\n")
        else:
            print("The letter: ",userguess[i], " is NOT in the word")
            #TODO: Adam: Store the letter that is not in the word in a new list which we can check against

    '''
    #Checking if the user gets the right letter and the right placement
    for letter1 in range(5):
        #Checking if the user gets the right letter
        letter=False
        #Checking if the user gets the right position
        position=False
       

        if userguess[letter1] == wordlewordoftheday[letter1]:
            print("The letter", wordlewordoftheday[letter1], "is found in the word and is in the correct position") 
    #Checking if the user gets the right letter but in the wrong placement
        elif userguess[letter1] == wordlewordoftheday[0]:
            print("The letter", userguess[letter1], "is found in the word")
        elif userguess[letter1] == wordlewordoftheday[1]:
            print("The letter", userguess[letter1], "is found in the word")
        elif userguess[letter1] == wordlewordoftheday[2]:
            print("The letter", userguess[letter1], "is found in the word")
        elif userguess[letter1] == wordlewordoftheday[3]:
            print("The letter", userguess[letter1], "is found in the word")
        elif userguess[letter1] == wordlewordoftheday[4]:
            print("The letter", userguess[letter1], "is found in the word")
    '''
print("\n\nBetter luck next time! The wordle word of the day was", wordlewordoftheday)