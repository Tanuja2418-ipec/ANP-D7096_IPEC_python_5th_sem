"""------------------------Electricity Consumption Category-------------------------- (if...elif...else Statement) 
Problem Statement An electricity department categorizes households based on monthly electricity consumption. 
• Up to 100 units → Low Consumption  
• 101–300 units → Moderate Consumption  
• Above 300 units → High Consumption  

Write a Python program to display the consumption category. 

Sample Input 245 
Sample Output Moderate Consumption"""


#--------------------------Coding Section-----------------------------------    

#taking the input from the user
consumption_units = float(input("Enter the monthly electricity consumption in units: "))

#Validating the consumption units
if consumption_units < 0:
    exit("Invalid consumption units. Please enter a positive value.")
    
#Categorizing the consumption category
if consumption_units <= 100:
    print("Low Consumption")
elif 101 <= consumption_units <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")

#-----------------------------Output Section-----------------------------------

""" 
Sample input: 245
Sample output: Moderate Consumption

Sample input: 80
Sample output: Low Consumption

Sample input: 350
Sample output: High Consumption"""