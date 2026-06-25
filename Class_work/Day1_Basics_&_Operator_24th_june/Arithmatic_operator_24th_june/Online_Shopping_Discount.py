""" Write a Python program to calculate the final payable amount after applying the discount"""


"Coding Section"

price = float(input("Enter the price of the product(in Rs) :  "))
Discount = float(input("Enter the discount to be applied( in %) : "))


Final_price = price - Discount

"Output"

print("The final amount is : Rs ", Final_price)