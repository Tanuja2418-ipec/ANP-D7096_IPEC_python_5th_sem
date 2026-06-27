"""--------------------------ATM Cash Withdrawal--------------------------------  
Problem Statement A customer can withdraw money only if the requested amount does not 
exceed the available balance. 
Accept the account balance and withdrawal amount. 
• If withdrawal amount is less than or equal to balance, display: Transaction Successful 
• Otherwise display: Insufficient Balance 

Sample Input 
5000 
4500 

Sample Output 
Transaction Successful """


#--------------------------Coding Section-----------------------------------

#taking input from the user
account_balance = float(input("Enter the account balance(in Rs.): "))
withdrawal_amount = float(input("Enter the withdrawal amount(in Rs.): "))

#Validating the account balance and withdrawal amount
if account_balance < 0 or withdrawal_amount < 0:
    exit("Invalid input. Please enter a positive value for account balance and withdrawal amount.")

#Checking if the withdrawal amount is less than or equal to the account balance
if withdrawal_amount <= account_balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")


#-----------------------------Output Section-----------------------------------

"""
Sample input:
Enter the account balance(in Rs.): 5000
Enter the withdrawal amount(in Rs.): 4500
Sample output:
Transaction Successful

Sample input:
Enter the account balance(in Rs.): 3000
Enter the withdrawal amount(in Rs.): 3500
Sample output:
Insufficient Balance
"""