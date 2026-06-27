"""-----------------------------Restaurant Bill Discount---------------------------
 Problem Statement A restaurant offers discounts based on the total bill amount. 
 • Bill below ₹1000 → No Discount  
 • ₹1000–₹2999 → 10% Discount  
 • ₹3000 or more → 20% Discount  
 
 Write a Python program to determine the applicable discount. 
 
 Sample Input 3200 
 Sample Output 20% Discount Applied """


#-------------------------------Coding Section-----------------------------------

#Taking input from the user
bill_amount = float(input("Enter the total bill amount(in Rs): "))

#Validating the bill amount
if bill_amount <= 0:
    exit("Invalid bill amount.Bill amount must be positive.")

#Calculating the discount based on the bill amount
if bill_amount < 1000:
    discount = 0
elif bill_amount >= 1000 and bill_amount < 3000:
    #applying 10% discount for bill amount between ₹1000 and ₹2999
    discount = 10
else:
    #applying 20% discount for bill amount ₹3000 or more
    discount = 20

print("The Discount applied is:", discount, "%")


#-------------------------------Output Section-----------------------------------
"""
Sample Input: 3200
Sample Output: The Discount applied is: 20 %

Sample Input: 1500
Sample Output: The Discount applied is: 10 %
"""