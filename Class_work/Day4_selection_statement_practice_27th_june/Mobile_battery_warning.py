"""------------------------------Mobile Battery Warning------------------------------
 Problem Statement A smartphone displays a low battery warning only when the battery percentage falls below 15%.
 Write a Python program to accept the battery percentage. 
 If the battery is below 15, display: Connect Charger Immediately 
 Otherwise, display nothing. 
 
 Sample Input 10
 Sample Output Connect Charger Immediately"""


#--------------------------Coding Section-----------------------------------

#taking input from the user
battery_percentage = float(input("Enter the battery percentage:"))

#checking if the battery is below 15%
if battery_percentage < 15:
    print("Connect Charger Immediately")


#-----------------------------Output Section-----------------------------------

"""
Sample input: 10
Sample output: Connect Charger Immediately

Sample input: 20
Sample output: (No output)"""