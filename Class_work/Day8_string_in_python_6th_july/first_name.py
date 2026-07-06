""" write a python program to ask the user to input the name and display the first name from it without using the library function."""

#--------------------------------------------coding section-----------------------------------------

#input from the user
name = input("Enter the name : ")

#initializing the first_name 
first_name = ""

for x in name:
    if (x>="A" and x<="Z") or (x>="a" and x<="z"):
        first_name += x
    else:
        break
print("First name : ", first_name)    
