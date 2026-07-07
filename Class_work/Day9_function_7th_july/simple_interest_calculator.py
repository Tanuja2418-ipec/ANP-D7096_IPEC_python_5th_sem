"""Write a python program to calculate simple interest using function"""

#-------------------------------coding section------------------------------


#function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal*rate*time)/100

#---------------------------------------------------------------------------

#main program
principal = float(input("Enter principle (in Rs.) : "))
rate = float(input("Enter rate (in percentage) : "))
time = int(input("Enter years (in years) : "))

print("Simple Interest : Rs ", calculate_simple_interest(principal, rate, time))


#------------------------Output section-------------------------------------

"""
Enter principle (in Rs.) : 4000
Enter rate (in percentage) : 7.6
Enter years (in years) : 3
Simple Interest : Rs  912.0
"""