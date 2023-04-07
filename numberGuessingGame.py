#Author: Michael@MGCodeSolutions

from random import randint

#Get players name
name = input("\n\nLet's play a game. What is your name?\n\n")

print("\nHello " + name + "\nLets pick your player skill level.")

#Set the player level for number of guesses
lvl = input("\nExpert (e) \nIntermediate (i) \nBeginner (b)\n\n")

if lvl == str("e"):
    level = 3
if lvl == str("i"):
    level = 4
if lvl == str("b"):
    level = 5

#Greeting to start game
print("\nI'm thinking of as number from 1 to 10.\nYou get " + str(level) + " chances, lets see if you can guess it...\n")


# generate random integer values
#from random import randint

#Generate random integer
for _ in range(10):
    value = randint(1 , 10)
    number = (value)
	
#Establish players guess and start count
print(name + " what is your guess?\n\n")
guess = input()
count = 1


#Loop to check players guess against random generated number and count guesses
while int(count) < int(level) and int(guess) != int(number):
    
    if int(guess) < number:
        print("Too low, guess a bigger number " + (name))
        count = int(count) + 1
        guess = input()
    
    if int(guess) > number:
        print("Too high, guess a smaller number " + (name))
        count = int(count) + 1
        guess = input()

#Correct guess finish
if int(guess) == int(number):
    print("\nGreat job " + (name) + ", you got it!!!!!")
    print("It took you " + str(count) + " attempt(s).\n")
    print("Sincerely, Michael@MGCodeSolutions\n")
    count = int(count) + 10
    #print("back side count " + str(count))
#Out of tries finish
if int(count) == int(level):
    print("\nYou're out of guesses " + (name))
    print("My number was " + str(number))
    print("Better luck next time.\n")
    print("Sincerely, Michael@MGCodeSolutions\n")
    
 

