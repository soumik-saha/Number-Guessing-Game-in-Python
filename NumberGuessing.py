'''Number Guessing Game'''
'''This Game is developed by Soumik Saha'''
from random import randint, random

randNum = randint(1,100)
attempt = 0

while randNum:
    user = int(input("Guess The Number : "))
    
    if user==randNum:
        print("Congrats! You have done it in "+ str(attempt+1) +" try...")
        break
    elif user>randNum:
        print("Oops! Actual Number is Less than You Think...")
        attempt = attempt+1
    else:
        print("Oops! Actual Number is Greater than You Think...")
        attempt = attempt+1
