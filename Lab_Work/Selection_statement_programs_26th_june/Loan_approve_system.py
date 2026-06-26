"""  2. Loan Approval System Problem Statement A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  

Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 

Sample Output 
Loan Status: Manual 
Review Reason: Income criteria not satisfied. """


#--------------------------Coding section---------------------------------


#taking input from user
credit_score = int(input("Enter Credit Score: "))

#validating credit score input
if credit_score < 0 or credit_score > 850:
    exit("Credit Score must be between 0 and 850. Please enter a valid credit score.")

#---------------------------------------------------------------------------------------------

annual_income = int(input("Enter Annual Income: "))

#validating annual income input
if annual_income < 0:
    exit("Annual Income cannot be negative. Please enter a valid income.")

#----------------------------------------------------------------------------------------------

existing_loan_amount = int(input("Enter Existing Loan Amount: "))

#validating existing loan amount input
if existing_loan_amount < 0:
    exit("Existing Loan Amount cannot be negative. Please enter a valid loan amount.")

#---------------------------------------------------------------------------------------------  


#conditions for loan approval
if credit_score >= 750:
    credit_score_condition = True
else:
    credit_score_condition = False

if annual_income >= 800000:
    annual_income_condition = True
else:
    annual_income_condition = False

if existing_loan_amount <= 200000:
    existing_loan_condition = True
else:
    existing_loan_condition = False
