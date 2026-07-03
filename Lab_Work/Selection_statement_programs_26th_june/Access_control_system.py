"""--------------------------Multi-Level Access Control System---------------------------------- 
Problem Statement 
Assign access levels based on: 
Roles: • Admin  
       • Manager  
       • Employee  
       • Guest  
Conditions: • Admin + Security Clearance ≥ 5 → Full Access  
            • Manager + Experience > 5 Years → Department Access  
            • Employee + Experience > 2 Years → Limited Access  
            • Guest → Read-Only Access  
            • Inactive Account → No Access  
Sample Input Role: Admin Security 
             Clearance: 6 Account
             Status: Active 
Sample Output Access Level: FULL ACCESS """

#-------------------------------coding section--------------------------------

#take inputs from the user
role = input("Enter the role (Admin/Manager/Employee/Guest): ")
security_clearance = int(input("Enter the security clearance (0-10): "))
experience = int(input("Enter the experience in years: "))
account_status = input("Enter the account status (Active/Inactive): ")

#displaying the input to the user
print("Role: ", role)
print("Security Clearance: ", security_clearance)   
print("Experience: ", experience)
print("Account Status: ", account_status)

#checking the access level based on the conditions
if account_status.lower() == "inactive":
    print("Access Level: NO ACCESS")
elif role.lower() == "admin" and security_clearance >= 5:
    print("Access Level: FULL ACCESS")
elif role.lower() == "manager" and experience > 5:
    print("Access Level: DEPARTMENT ACCESS")
elif role.lower() == "employee" and experience > 2:
    print("Access Level: LIMITED ACCESS")
elif role.lower() == "guest":
    print("Access Level: READ-ONLY ACCESS")
else:
    print("Access Level: NO ACCESS")


#---------------------------------------output section-------------------------------------

"""
Sample Input Role: Admin Security 
             Clearance: 6 Account
             Status: Active 
Sample Output Access Level: FULL ACCESS


sample Input Role: Manager Security
            clearance: 4
            experience: 6
            status: Active
Sample Output Access Level: DEPARTMENT ACCESS
"""