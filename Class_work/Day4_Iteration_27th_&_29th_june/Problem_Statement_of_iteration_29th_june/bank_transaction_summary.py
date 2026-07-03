"""Bank Transaction Summary
Problem Statement
A customer keeps entering transaction amounts.
Positive numbers indicate deposits, while negative numbers indicate withdrawals.
The customer enters 0 to finish.
Display:
•
Total Deposit
•
Total Withdrawal
•
Final Balance"""

#----------------------------coding section------------------------------------

# Initialize variables
total_deposit = 0
total_withdrawal = 0
final_balance = 0

# Take the first transaction
transaction = float(input("Enter transaction amount (0 to stop): "))

# Continue until the user enters 0
while transaction != 0:

    # Check if it is a deposit
    if transaction > 0:
        total_deposit += transaction
        balance += transaction

    # Check if it is a withdrawal
    elif transaction < 0:
        total_withdrawal += abs(transaction)  # Store withdrawal as a positive value
        balance += transaction                # Subtract from balance

    # Take the next transaction
    transaction = float(input("Enter transaction amount (0 to stop): "))

# Display the results
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", final_balance)


#-----------------------------output section---------------------------------


"""
Output:
Enter transaction amount (0 to stop): 100
Enter transaction amount (0 to stop): -50
Enter transaction amount (0 to stop): 200
Enter transaction amount (0 to stop): -30   
Enter transaction amount (0 to stop): 0
Total Deposit: 300.0
Total Withdrawal: 80.0
Final Balance: 220.0

"""