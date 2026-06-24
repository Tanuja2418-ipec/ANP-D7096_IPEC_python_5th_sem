""" Write a Python program to calculate the remaining balance after withdrawal. """

"Coding Section"

"Input: • Current Balance  • Withdrawal Amount  "
"Output: • Remaining Balance "

Current_Balance = float(input("Enter the Current Amount : "))
Withdrawal_Amount = int(input("Enter the amount to withdraw : "))

Remaining_Balance = Current_Balance - Withdrawal_Amount 


"Output"

print("Remaining Balance is : ",Remaining_Balance)