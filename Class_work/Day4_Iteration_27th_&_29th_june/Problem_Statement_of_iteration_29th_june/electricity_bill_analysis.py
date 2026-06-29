"""Electricity Bill Analysis
Problem Statement
An electricity department wants to analyze electricity consumption of N houses.
Accept the monthly units consumed by each house.
Calculate and display:
•
Total units consumed
•
Average units consumed
•
Highest consumption
•
Lowest consumption
"""


#-----------------------------coding section-----------------------------


# Accept the number of houses
n = int(input("Enter the number of houses: "))

# Initialize variables
total = 0

# Take the units for the first house
units = int(input("Enter units consumed by House 1: "))
highest = units
lowest = units
total = units

# Take input for the remaining houses
for i in range(2, n + 1):
    units = int(input(f"Enter units consumed by House {i}: "))

    # Add units to total
    total += units

    # Check for highest consumption
    if units > highest:
        highest = units

    # Check for lowest consumption
    if units < lowest:
        lowest = units

# Calculate average consumption
average = total / n

# Display the results
print("Total Units Consumed:", total)
print("Average Units Consumed:", average)
print("Highest Consumption:", highest)
print("Lowest Consumption:", lowest)

