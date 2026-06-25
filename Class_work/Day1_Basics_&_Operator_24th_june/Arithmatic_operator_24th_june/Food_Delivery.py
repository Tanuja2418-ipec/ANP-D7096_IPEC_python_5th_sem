""" Food Delivery Business Profit Analysis
Scenario: A food delivery startup wants to calculate its daily profit and package distribution details.
Problem Statement: Write a Python program that:
1.
Calculates total revenue generated.
2.
Calculates profit after deducting expenses.
3.
Determines how many complete delivery boxes can be prepared.
4.
Finds remaining food packets.
5.
Predicts revenue after a certain number of days assuming revenue doubles daily.
Input:
•
Number of orders
•
Price per order
•
Daily expenses
•
Total food packets
•
Packets per box
•
Number of days
Output:
•
Total Revenue
•
Profit
•
Complete Boxes
•
Remaining Packets
•
Future Revenue"""


#Coding Section

Number_of_orders = int(input("Enter the number of orders: "))
Price_per_order = float(input("Enter the price per order (in Rs): "))
