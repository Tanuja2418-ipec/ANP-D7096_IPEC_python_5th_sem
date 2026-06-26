"""  1. Smart Income Tax Calculator
Problem Statement A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable. 
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
Sample Output Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0 """


#--------------------------Coding section---------------------------------

#taking input from user
income = float(input("Enter Annual Income(in rupees): "))

#validating income input
if income < 0:
    exit("Income cannot be negative. Please enter a valid income.")
#-------------------------------------------------------------------------


age = int(input("Enter Age(in years): "))

gender = input("Enter Gender (M/F): ")

#calculating tax based on income slabs
if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = (income - 500000) * 0.10
elif income <= 2000000:
    tax = (income - 1000000) * 0.20 + 50000
else:
    tax = (income - 2000000) * 0.30 + 250000

#calculating rebates based on age and gender
senior_citizen_rebate = 0
if age >= 60:
    senior_citizen_rebate = tax * 0.05
    
women_rebate = 0
if gender == "F":
    women_rebate = tax * 0.02

#calculating final tax payable
final_tax = tax - senior_citizen_rebate - women_rebate

#displaying the results
print(f"Tax before rebate: ₹{tax:.2f}")
print(f"Senior Citizen Rebate: ₹{senior_citizen_rebate:.2f}")
print(f"Women Rebate: ₹{women_rebate:.2f}")
print(f"Final Tax Payable: ₹{final_tax:.2f}")


#----------------------------------------------------------------------

#------------------output section--------------------------------------

"""  Enter Annual Income(in rupees): 1200000
Enter Age(in years): 65
Enter Gender (M/F): F
Tax before rebate: ₹240000.00
Senior Citizen Rebate: ₹12000.00
Women Rebate: ₹4800.00
Final Tax Payable: ₹223200.00"""