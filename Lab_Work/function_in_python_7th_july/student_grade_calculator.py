"""
Problem Statement 1: Student Grade Calculator

Write a Python program that defines a function calculate_grade(marks).

The function should:

Accept marks (0–100) as a parameter.
Return the grade according to the following criteria:
90 and above → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail
The main program should:

Accept marks of 5 students.
Call the function for each student.
Display the marks and corresponding grade."""



#-------------------------Coding section-----------------------------------

#function to caclulate student grade
def calculate_student_grade(marks):
    if marks>=90:
        return("A+")
    elif marks>=75:
        return(" A") 
    elif marks>=60:
        return(" B") 
    elif marks>=40:
        return(" C")
    else:
        return("Fail")
    
#main program 

for i in range(5):
    marks = int(input("Enter marks of student: " ))

    #calling a function 
    grade = calculate_student_grade(marks)
    
    print("Marks : ",marks ," , ","Grade : ", grade)


#-----------------------------Output Section--------------------------------

"""
Enter marks of student: 56
Marks :  56
Grade :   C
Enter marks of student: 89
Marks :  89
Grade :   A
Enter marks of student: 93
Marks :  93
Grade :  A+
Enter marks of student: 34
Marks :  34
Grade :  Fail
Enter marks of student: 70
Marks :  70
Grade :   B
"""    

