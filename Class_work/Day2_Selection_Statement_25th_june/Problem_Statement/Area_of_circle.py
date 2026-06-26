""" Write a program to calculate area of circle and validate it"""

#Input of Radius from user
radius = float(input("Enter the radius of Circle (in m):"))

#Validating the radius
if radius < 0 :
    print("Radius Can not be negative.")
    
#--------------------------------------------

#Displaying the radius to the user
print("Radius is : ", radius)

#--------------------------------------------

#Displaying Area of circle
print("The Area of circle is : ", 3.14*radius*radius , "m^2")


