"""
Problem Statement 2: List Analysis using Functions

Write a Python program that defines the following functions:

find_max(numbers)
find_min(numbers)
find_average(numbers)
The program should:

Accept a list of 10 integers from the user.
Call all three functions.
Display the maximum value, minimum value, and average of the list."""


#-------------------------output section--------------------------------

#function to find max number in a list
def find_max(numbers):
    return max(numbers)

#function to find min number in a list
def find_min(numbers):
    return min(numbers)
#function to find average of the list
def find_average(numbers):
    sum = 0 
    for i in range(len(numbers) + 1):
        sum = sum + i
    average = sum/10 
    return average

#main program 
#creating a empty list 
numbers = []

for i in range(10):
    num = int(input("Enter any number : "))
    numbers.append(num)

#displaying the list 
print(numbers)

print("The maximum number in the list : ", find_max(numbers))
print("The minimum number in the list : ", find_min(numbers))
print("The average of the list : ", find_average(numbers))


#---------------------------Output Section------------------------------------

"""
Enter any number : 1
Enter any number : 2
Enter any number : 3
Enter any number : 4
Enter any number : 5
Enter any number : 6
Enter any number : 7
Enter any number : 8
Enter any number : 9
Enter any number : 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Tne maximum number is the list :  10
Tne minimum number is the list :  1
The average of the list :  5.5

"""

