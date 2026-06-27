"""----------------------------Parking Entry Validation----------------------  
Problem Statement Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, display: Entry Allowed 
• Otherwise display: Entry Denied 

Sample Input 0 S
ample Output Entry Denied """


#--------------------------Coding Section-----------------------------------

#taking input from the user
parking_pass = int(input("Enter the parking pass (1 for Valid Pass/0 for No Pass): "))

#validating the input
if parking_pass < 0 or parking_pass > 1:
    exit("Invalid input")

#checking if the parking pass is valid
if parking_pass == 1:
    print("Entry Allowed")
else:
    print("Entry Denied")


#-----------------------------Output Section-----------------------------------

""" 
Sample input: 1
Sample output: Entry Allowed
Sample input: 0
Sample output: Entry Denied"""

