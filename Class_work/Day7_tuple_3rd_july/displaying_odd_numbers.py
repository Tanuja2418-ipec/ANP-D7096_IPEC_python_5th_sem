"""Write a python program to create a tuple of 15 numbers given by the user and display all the odd numbers from the tuple."""

#------------------------coding section----------------------------


#creating an empty list to store user input
numbers = []
print("Please enter 15 numbers:")
for i in range(15):
    num = int(input("Enter number : "))
    numbers.append(num)

# converting the list to a tuple
numbers_tuple = tuple(numbers)


print("------------------------------------------------------------------")


#displaying the tuple
print("The tuple of numbers is:", numbers_tuple)


print("------------------------------------------------------------------")


# displaying odd numbers
print("Odd numbers in the tuple:")
for n in numbers_tuple:
    if n % 2 != 0:
        print(n, end=" ")


""" 
Output : 

Please enter 15 numbers:
Enter number : 34
Enter number : 23
Enter number : 45
Enter number : 12
Enter number : 67
Enter number : 89
Enter number : 90
Enter number : 11
Enter number : 22
Enter number : 33
Enter number : 44
Enter number : 55
Enter number : 66
Enter number : 77
Enter number : 88
------------------------------------------------------------------
The tuple of numbers is: (34, 23, 45, 12, 67, 89, 90, 11, 22, 33, 44, 55, 66, 77, 88)
------------------------------------------------------------------
Odd numbers in the tuple: 23 45 67 89 11 33 55 77
"""