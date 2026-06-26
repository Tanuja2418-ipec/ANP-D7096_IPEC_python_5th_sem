""" -------------------E-Commerce Premium Membership Eligibility---------------------------
Problem Statement A customer becomes Premium Member 
if: • Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  

Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  

Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 

Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000."""

#------------------------------coding Section----------------------------------

# Taking input from the user
total_purchases = float(input("Enter Total Purchases (in ₹): "))    
orders_completed = int(input("Enter Orders Completed: "))
customer_rating = float(input("Enter Customer Rating: "))

# Check if total purchases exceed ₹1,00,000
if total_purchases > 100000:
    print("Premium Membership Status: Eligible")
    print("Reason: Purchase amount exceeded ₹100000.")


if total_purchases > 50000 and orders_completed >= 20 and customer_rating >= 4.5:
    print("Premium Membership Status: Eligible")
    print("Reason: All eligibility criteria met.")
else:
    print("Premium Membership Status: Not Eligible")
    print("Reason: Eligibility criteria not met.")

#------------------------------output section-----------------------------------------


"""  
Sample input
Total purchases: 120000
Orders completed: 10
Customer rating: 4.0

Sample output
Premium Membership Status: Eligible
Reason: Purchase amount exceeded ₹100000.
"""