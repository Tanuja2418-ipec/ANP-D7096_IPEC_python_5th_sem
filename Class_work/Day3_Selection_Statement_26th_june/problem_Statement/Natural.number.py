""" Check if a number is a natural number.
A natural number is a positive integer greater than zero. 
This program checks if the input number is a natural number or not.
Sample Input 1: 5
Sample Output 1: The number is a natural number.
Sample Input 2: -3
Sample Output 2: The number is not a natural number."""


#------------------------------------------------------------
#------coding section------#    
#Take input from the user for a number
number = int(input("Enter a number: "))

#------------------------------------------------------------
#validate if the number is a natural number
if number > 0:
    print("The number is a natural number.")
else:
    print("The number is not a natural number.")    



#-----------output section----------------#
"""Enter a number: 5
The number is a natural number. 
Enter a number: -3
The number is not a natural number."""
