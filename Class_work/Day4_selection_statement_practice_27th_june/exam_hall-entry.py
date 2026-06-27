"""--------------------------Exam Hall Entry----------------------------- 
Problem Statement Students are allowed to enter the examination hall only if they are carrying their admit card. 
Accept input as: • 1 → Admit Card Available  
• 0 → Admit Card Not Available  
If the input is 1, display: Enter Examination Hall 
Otherwise, do not display anything. 

Sample Input 1 
Sample Output Enter Examination Hall """

#--------------------------Coding Section-----------------------------------

#taking input from the user
admit_card = int(input("Enter 1 if Admit Card is Available or 0 if Admit Card is Not Available: "))

#validating the input
if admit_card < 0 or admit_card > 1:
    exit("Invalid input..")

#checking if the admit card is available
if admit_card == 1:
    print("Enter Examination Hall")


#-----------------------------Output Section-----------------------------------


"""
Sample input: 1
Sample output: Enter Examination Hall

Sample input: 0
Sample output: (No output)
"""