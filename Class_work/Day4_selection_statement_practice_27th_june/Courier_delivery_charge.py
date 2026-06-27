"""-------------------------------------Courier Delivery Charge----------------------------
 Problem Statement A courier company calculates delivery charges based on the package weight. 
 • Weight up to 2 kg → ₹50  
 • Weight greater than 2 kg and up to 5 kg → ₹100  
 • Weight greater than 5 kg → ₹180  
 
 Write a Python program to display the delivery charge. 
 
 Sample Input 4 
 Sample Output Delivery Charge = ₹100 """

#--------------------------Coding Section-----------------------------------   

#taking the input from the user
weight = float(input("Enter the package weight in kg: "))

#Validation the weight
if weight < 0:
    exit("Invalid weight. Please enter a positive value.")

#Calculating the delivery chage based on the weight
if weight <= 2:
    delivery_charge = 50
elif weight > 2 and weight <= 5:
    delivery_charge = 100
else:
    delivery_charge = 180

print("Delivery Charge = Rs", delivery_charge)


#-----------------------------Output Section-----------------------------------

"""   
Sample input: 6
Sample output: Delivery Charge = Rs 180

Sample input: 1
Sample output: Delivery Charge = Rs 50

Sample input: 4
Sample output: Delivery Charge = Rs 100"""