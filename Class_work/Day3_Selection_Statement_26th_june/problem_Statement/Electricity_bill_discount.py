""" Problem 1: Electricity Bill Discount 
Problem Statement An electricity provider offers a 10% discount on the total bill amount 
if the customer's bill is ₹5,000 or more. 
Otherwise, no discount is applied. Write a Python program to accept the total bill amount from the user and display the final amount to be paid.
 Sample Input 1 
 Enter the electricity bill amount: 6200
   Sample Output 1 Discount Applied!
     Final Bill Amount: ₹5580.0
       Sample Input 2 
       Enter the electricity bill amount: 4200 
       Sample Output 2 No Discount Applied! 
       Final Bill Amount: ₹4200 """
#------------------------------------------------------------
#------coding section------#


# Take input from the user for the electricity bill amount

electricity_bill_amount = float(input("Enter the electricity bill amount(in rupees): "))

# Check if the bill amount is greater than or equal to 5000 to apply the discount
if electricity_bill_amount >= 5000:
    discount = electricity_bill_amount * 0.10
    final_amount = electricity_bill_amount - discount
    print(f"Final Bill Amount: ₹{final_amount}")
    print("Discount Applied!")
else:
    final_amount = electricity_bill_amount
    print(f"Final Bill Amount: ₹{final_amount}")
    print("No Discount Applied!")


#-----------output section----------------#
"""
Enter the electricity bill amount(in rupees): 6200
Final Bill Amount: ₹5580.0 
Discount Applied! """