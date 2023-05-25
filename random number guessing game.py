#Brian Webb
#ITEC209
#2/27/2023
#Random Number Guessing Game
import random

n = random.randrange(1, 100)
guess = int(input("Enter any number: "))
count = 0

while n != guess:
    if guess < n:
        print("Too low, try again")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high, try again!")
        guess = int(input("Enter number again: "))
    count += 1

print("You guessed it right!!")
print("Number of guesses:", count)
