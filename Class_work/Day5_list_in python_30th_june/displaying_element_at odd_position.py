"""Python program to display element at odd position in a list"""


#---------------------------coding Section---------------------------


#creating a list to store the numbers
numbers = [40, 90, 23, 87, 10, 50, 60, 70, 80, 100]

#displaying numbers to the user
print("The numbers entered by the user are: ")  
print(*numbers)

#displaying elements at odd positions
print("Elements at odd positions are: ")
for i in range(1, len(numbers), 2):
    print(numbers[i])

    