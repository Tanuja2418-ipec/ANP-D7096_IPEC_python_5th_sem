"""ATM PIN Verification
Problem Statement
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. 
The user can keep entering the PIN until it matches the correct one.
Display "Access Granted" when the correct PIN is entered.
Sample Output
Enter PIN: 1234 Incorrect PIN Enter PIN: 9876 Incorrect PIN Enter PIN: 4589 Access Granted
"""

#-----------------------Coding Section-----------------------------

#Correct PIN
correct_pin = 4589

#Taking input of the pin from the user
pin = int(input("Enter the PIN : "))

while pin != correct_pin:
    print("Incorrect PIN")
    pin = int(input("Enter the PIN : "))  
print("Access Granted")



