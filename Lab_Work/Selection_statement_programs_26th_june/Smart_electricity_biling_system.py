"""  ----------------------Smart Electricity Billing System--------------------------------

Problem Statement Calculate electricity bill 
using: Units          Rate 
       0-100        ₹5/unit 
       101-300      ₹7/unit 
       Above 300    ₹10/unit 

Additional Rules: • Commercial consumers pay 20% extra.  
                  • Bills above ₹5000 attract 5% surcharge.  
                  • Senior citizens receive 10% discount. 

Sample Input 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y 

Sample Output 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103 """

#------------------------------coding Section----------------------------------

# Taking input from the user
units_consumed = int(input("Enter Units Consumed: "))
consumer_type = input("Enter Consumer Type (Residential/Commercial): ")
senior_citizen = input("Senior Citizen (Y/N): ")

# Calculate base bill based on units consumed
if units_consumed <= 100:
    base_bill = units_consumed * 5
elif units_consumed <= 300:
    base_bill = 100 * 5 + (units_consumed - 100) * 7
else:
    base_bill = 100 * 5 + 200 * 7 + (units_consumed - 300) * 10

# Calculate commercial charge if applicable
commercial_charge = 0
if consumer_type == "commercial":
    commercial_charge = base_bill * 0.20

# Calculate surcharge if applicable
surcharge = 0
if base_bill + commercial_charge > 5000:
    surcharge = (base_bill + commercial_charge) * 0.05

# Calculate senior citizen discount if applicable
senior_discount = 0
if senior_citizen == "Y":
    senior_discount = (base_bill + commercial_charge - surcharge) * 0.10

# Calculate final bill amount
final_bill = base_bill + commercial_charge + surcharge - senior_discount

# Display the bill details
print("Base Bill: ₹", format(base_bill, ".2f"))
print("Commercial Charge: ₹", format(commercial_charge, ".2f"))
print("Surcharge: ₹", format(surcharge, ".2f")) 
print("Senior Citizen Discount: ₹", format(senior_discount, ".2f"))
print("Final Bill Amount: ₹", format(final_bill, ".2f"))

#------------------------------output Section-----------------------------------------

"""
Sample Input
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial
Senior Citizen (Y/N): Y

Sample Output
Base Bill: ₹4500.00 
Commercial Charge: ₹900.00
Surcharge: ₹270.00
Senior Citizen Discount: ₹567.00
Final Bill Amount: ₹5103.00
"""