""" Write a program to calculate area and perimeter
 of rectangle and validate it"""


#Input of Length of the retangle from the user
length = float(input("Enter the length of retangle (in m):"))

#Validating the length
if length < 0: 
    print("Length can not be negative")


#Input of Breath of the retangle from the user
breath = float(input("Enter the breath of retangle (in m):"))


#Validating the breath
if breath < 0: 
    print("Breath can not be negative")

#------------------------------------------------


#Displaying the Length to the user
print("The length is : ",length)

#Displaying the breath to the user
print("The length is : ",breath)


#------------------------------------------------

#Displaying the area of Retangle 
print ("The area of Retangle is : ", length*breath , "m^2")

#Displaying the Perimeter of Retangle 
print ("The Perimeter of Retangle is : ",2*(length+breath) , "m")


