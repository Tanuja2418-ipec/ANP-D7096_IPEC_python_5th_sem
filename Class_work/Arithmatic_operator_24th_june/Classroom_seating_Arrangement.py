"""Write a Python program to determine how many complete rows can be formed. """


"Coding Section"

Total_Students = int(input("Enter the number of students: "))
Students_per_row = int(input( "Enter the NUmber of student per row: "))

Number_of_complete_Rows = Total_Students  // Students_per_row



"Output" 
print("The number of complete rows: ", Number_of_complete_Rows)