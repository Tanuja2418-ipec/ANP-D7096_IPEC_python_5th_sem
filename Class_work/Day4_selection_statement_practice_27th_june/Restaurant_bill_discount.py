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

#Calculatin the discount based on the bill amount
if bill_amount < 1000:
    discount = 0
elif bill_amount >= 1000 and bill_amount < 3000:
    discount = 10
else:
    discount = 20

print("The Discount applied is:", discount, "%")


#-------------------------------Output Section-----------------------------------
"""
Sample Input: 3200
Sample Output: The Discount applied is: 20 %

Sample Input: 1500
Sample Output: The Discount applied is: 10 %
"""