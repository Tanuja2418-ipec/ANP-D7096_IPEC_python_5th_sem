""" -----------------------------Scholarship Eligibility-------------------------------  
Problem Statement A university provides a scholarship only to students who score 90 or above. 

Write a Python program to accept a student's percentage and determine whether the student is eligible. 
• If percentage is 90 or above, display: Scholarship Approved 
• Otherwise display: Scholarship Not Approved 

Sample Input 92 
Sample Output Scholarship Approved """


#--------------------------Coding Section----------------------------------------


#Taking input from the user
percentage = float(input("Enter the student's percentage: "))

#Validating the percentage
if percentage < 0 or percentage > 100:
    exit("Invalid percentage. Please enter a value between 0 and 100.")

#checking if the student is eligible for scholarship
if percentage >= 90:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")


#---------------------------Output section----------------------------------------

""" 
Sample input:
Enter the student's percentage: 92
Sample output: Scholarship Approved"""