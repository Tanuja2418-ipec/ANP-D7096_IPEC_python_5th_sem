"""Login System with Maximum Attempts
Problem Statement
A system allows only three login attempts.
The correct username is admin and the password is python123.
If the credentials are correct, display "Login Successful".
Otherwise, after three unsuccessful attempts, display "Account Locked".
Sample Output
Attempt 1 Username: admin Password: abc Invalid Credentials Attempt 2 Username: admin Password: python123 Login Successful"""


#-------------------------------Coding Section------------------------------------------------

# Correct username and password
correct_username = "admin"
correct_password = "python123"

# Initialize attempt counter
attempt = 1

# Allow a maximum of 3 attempts
while attempt <= 3:

    # Take username and password from the user
    username = input(f"Attempt {attempt} Enter Username: ")
    password = input("Enter Password: ")

    # Check if the credentials are correct
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break

    # If credentials are incorrect
    else:
        print("Invalid Credentials")
        attempt += 1

# If all 3 attempts are used
if attempt > 3:
    print("Account Locked")


#------------------------------------output section--------------------------------------------

"""
Sample Output
Attempt 1 Username: admin 
          Password: abc 
          Invalid Credentials 
Attempt 2 Username: admin
          Password: xyx123 
          Invalid Credentials        
Attempt 3 Username: admin 
          Password: python123 
          Login Successful

"""