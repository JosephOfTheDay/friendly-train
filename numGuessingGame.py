#New number guessing game

import random
import sys
timesGuessed = 0

print("What is your name?:  ")
name  = str(input())
print("enter a number:  ")
maximum = int(input())

print("Hello, " + name + " we are going to play a game. I have a secret number between 1 and " + str(maximum) +" and your job is to guess this number in as little amounts of guesses as you can! Good Luck!")

secNumber = random.randint(1, maximum)

while timesGuessed <10:
    timesGuessed = timesGuessed+1
    print('enter a guess')
    guess = int(input())
    
    if guess < secNumber:
        print("your guess was too low! Guess again!")
        
    elif guess > secNumber:
        print('your guess was too high! Guess again!')
    elif guess > secNumber and timesGuessed >1:
        print('your guess was still too high! Guess again!')
    
    elif guess == secNumber:
        print("you got it! my secret number was," + str(secNumber) + " you guessed it in " + str(timesGuessed) + "guesses! good job " +name+"!")
        timesGuessed = 10
        