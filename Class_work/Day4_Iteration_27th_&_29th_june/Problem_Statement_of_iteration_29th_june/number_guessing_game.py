"""Number Guessing Game
Problem Statement
A secret number is 37.
Keep asking the user to guess the number until the correct number is entered.
Display whether the entered number is too high, too low, or correct."""


#--------------------------coding section------------------------------------------


secret_number = 37

#taking input of number from the user
num = int(input("Enter the Number : "))

while num != 37:
    if num < 37:
        print("Number is too low.")
    else: 
        print("Number is too high.")

    num = int(input("Enter the Number : ")) 
     
print("Number is Correct.")        
