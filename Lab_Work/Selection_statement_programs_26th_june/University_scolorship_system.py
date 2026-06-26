"""  --------------------------University Scholarship System----------------------------
Problem Statement:  Scholarship is awarded based on percentage: 
Percentage   Scholarship 
   95+             100% 
   90-94            75% 
   85-89            50% 
   80-84            25% 
   Below 80         No Scholarship 

Conditions: 
• Family income must be below ₹8,00,000.  
• Students with disciplinary actions receive no scholarship.  

Sample Input 
Percentage: 92 
Family Income: 500000 
Disciplinary Action (Y/N): N 

Sample Output 
Scholarship Awarded: 75% """


#------------------------------coding Section---------------------------------- 

# Taking input from the user
percentage = float(input("Enter Percentage: ")) 
family_income = float(input("Enter Family Income (in ₹): ")) 
disciplinary_action = input("Disciplinary Action (Y/N): ")

# Check if family income is below ₹8,00,000 and no disciplinary action
if family_income < 800000 and disciplinary_action == 'N':
    if percentage >= 95:
        print("Scholarship Awarded: 100%")
    elif percentage >= 90:
        print("Scholarship Awarded: 75%")
    elif percentage >= 85:
        print("Scholarship Awarded: 50%")
    elif percentage >= 80:
        print("Scholarship Awarded: 25%")
    else:
        print("Scholarship Awarded: No Scholarship")

else:
    print("Scholarship Awarded: No Scholarship")

#------------------------------output Section-----------------------------------------

"""
Sample Input
Percentage: 92
Family Income: 500000
Disciplinary Action (Y/N): N

Sample Output 
Scholarship Awarded: 75% 
"""
