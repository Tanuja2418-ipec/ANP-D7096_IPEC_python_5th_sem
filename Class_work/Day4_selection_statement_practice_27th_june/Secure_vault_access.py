"""----------------------Secure Vault Access------------------------- 
 Problem Statement:
 A digital vault can only be opened if the user enters the correct security code. 
 Write a Python program that accepts the entered security code. 
 If the entered code is 7890, 
 display: "Access Granted to the Vault." 
 Otherwise, do nothing. 

 Sample Input 
 7890 

 Sample Output 
 Access Granted to the Vault. """ 


#--------------------------Coding Section-----------------------------------


#Taking input from the user
security_code = int(input("Enter the security code: "))

#validating the security code
if security_code < 0 or security_code > 9999:
    exit("Invalid security code. Please enter a 4-digit code.")

#checking if the entered security code is correct
if security_code == 7890:
    print("Access Granted to the Vault.")


#----------------------Output section-----------------------------------


"""
Sample input: 7890

Sample output: Access Granted to the Vault.

"""
