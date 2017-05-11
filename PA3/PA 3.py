# Katerina Chinnappan
# kachinna@ucsc.edu
# programming assignment 3
# Python program that plays an interactive guessing game 
# with the user.Your program will generate a random integer 
# in the range 1 to 10, then allow the user three guesses to
# determine the integer

import random
numberOfGuesses = 0
print("\n")
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")
print("\n")
#the random number between 1 and 10
number = random.randint(1, 10)
while numberOfGuesses < 3:
    #increment the number of guesses as soon as while loop starts
    numberOfGuesses = numberOfGuesses + 1;
    #depending on numberOfGuesses, display appropriate message
    if numberOfGuesses == 1:
        userInput = int(input("Enter your first guess: "))
    elif numberOfGuesses == 2:
        userInput = int(input("Enter your second guess: ")) 
    elif numberOfGuesses == 3:
        userInput = int(input("Enter your third guess: "))
    #if guess is < number and # of guesses does not == 3
    if userInput < number and numberOfGuesses != 3:
        print("Your guess is too low. Guess again.")
        print("\n")
    #if guess < number and # of guesses == 3, display lose message    
    elif userInput < number and numberOfGuesses == 3:
        print("Your guess is too low. You lose.")
        print("\n") 
    #if guess > number and # of guesses != 3    
    elif userInput > number and numberOfGuesses != 3:
        print("Your guess is too high. Guess again.")
        print("\n")
    #if guess > number and # of guesses == 3, display lose message    
    elif userInput > number and numberOfGuesses == 3:
        print("Your guess is too high. You lose.")
        print("\n")
    #if guess == number, break from while loop  
    elif userInput == number:
        break

#if guess == number, display win message
if userInput == number:
    print("You win!")

#if # of guesses >= 3, reveal the random number
if numberOfGuesses >= 3:
    print("The number was " + str(number),".")


    
