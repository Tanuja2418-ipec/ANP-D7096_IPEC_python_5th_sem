"""Write a Python program to find how
 many slices remain after equal distribution."""


"COding Section"

Pizza_Slices = int(input("Enter the Total number of pizza Slices: "))
Number_of_Children = int(input("Enter the total number of children: "))


Remaining_Slices = Pizza_Slices % Number_of_Children

"Output"

print("Remaining Slices are ",Remaining_Slices )