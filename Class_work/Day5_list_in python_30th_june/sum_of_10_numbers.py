"""Write a python program to find the sum of 10 numbers entered by the user."""


#-------------------coding Section---------------------------

#creating a list to store the numbers
numbers = [40, 90, 30, 20, 10, 50, 60, 70, 80, 100]

#displaying numbers to the user
print("The numbers entered by the user are: ")
print(*numbers)

#finding sum
sum = 0
for x in numbers:
    sum += x

#displaying the sum
print("The sum of the numbers is: ", sum)