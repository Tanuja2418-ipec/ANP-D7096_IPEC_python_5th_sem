"""  Write a program to check if a person is eligible to vote based on their age.
The program should accept the age of the person as input and display whether they
are eligible to vote or not. 
A person is eligible to vote if they are 18 years old or older.
sample Input 1
Enter your age: 20
sample Output 1
You are eligible to vote."""

#------------------------------------------------------------
#------coding section------#

# Take input from the user for their age
age = int(input("Enter your age(in years): "))

#------------------------------------------------------------
#validate the age 
if age < 0:
    print("Invalid age. Please enter a valid age.")

#------------------------------------------------------------
    
#verify if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#-----------output section----------------#
"""Enter your age(in years): 20
You are eligible to vote."""

