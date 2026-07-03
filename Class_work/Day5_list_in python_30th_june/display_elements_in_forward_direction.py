"""Python program to display elements of listin forward direction using backword indexing"""


#---------------------------coding Section---------------------------

#creating a list to store the numbers
numbers = [40, 90, 23, 87, 10, 50, 60, 70, 80, 100]

#displaying numbers to the user
print("The numbers entered by the user are: ")
print(*numbers)

#displaying elements in forward direction using backward indexing
print("Elements in forward direction using backward indexing are: ")
for i in range(-1, -len(numbers) - 1, -1):
    print(numbers[i])

    