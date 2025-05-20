import random

target = random.randint(1,9)
guessedint = int(input('Enter the number for your guess between 1 and 9'))
while target != guessedint :
    guessedint = int(input('Try again please enter your new guess'))

print('Well guessed ')
