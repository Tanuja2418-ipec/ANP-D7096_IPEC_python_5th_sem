""" Write a Python program to calculate the value of money after 
a certain number of years assuming it doubles every year."""

"Coding Section"

Initial_Amount = float(input("Enter the Initial Amount(in rupees) : "))
Number_of_Years = int(input("Enter the Number of Years: "))

Final_Amount = Initial_Amount * (2 ** Number_of_Years)


"Output"

print("The final amount is: Rs ", Final_Amount)