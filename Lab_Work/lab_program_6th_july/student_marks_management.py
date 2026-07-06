""" Lab 1: Student Marks Management
Problem Statement:
Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks.

Perform the following operations:

Display all student names and marks.
Add a new student with marks.
Update the marks of an existing student.
Delete a student by name.
Display the student who scored the highest marks."""



#---------------------------------coding section-------------------------------------------


# Create a  blank dictionary
students = {}

print("Enter details of 5 students : ")
for i in range(5):
    #taking input of name
    name = input("Enter student name: ")
    #taking input of marks
    marks = int(input("Enter marks: "))
    students[name] = marks

# Display all student names and marks
print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Add a new student
new_name = input("\nEnter new student name: ")
new_marks = int(input("Enter marks: "))
students[new_name] = new_marks

print("\nAfter Adding New Student:")
for name, marks in students.items():
    print(name, ":", marks)

# Update marks of an existing student
update_name = input("\nEnter the student name to update marks: ")

if update_name in students:
    new_marks = int(input("Enter new marks: "))
    students[update_name] = new_marks
    print("Marks updated successfully.")
else:
    print("Student not found.")
    new_marks = int(input("Enter new marks: "))

# Step 5: Delete a student
delete_name = input("\nEnter the student name to delete: ")

if delete_name in students:
    del students[delete_name]
    print("Student deleted successfully.")
else:
    print("Student not found.")


# Step 6: Display all students after update and delete
print("\nUpdated Student Records:")
for name, marks in students.items():
    print(name, ":", marks)

# Step 7: Display the student with the highest marks
highest_student = max(students, key=students.get)

print("\nHighest Scorer:")
print("Name :", highest_student)
print("Marks:", students[highest_student])


#-------------------------Output section-------------------------------------


"""
Enter details of 5 students : 
Enter student name: Vihaan
Enter marks: 65
Enter student name: vamika
Enter marks: 98
Enter student name: rohan
Enter marks: 49
Enter student name: Vyom
Enter marks: 90
Enter student name: Niharika
Enter marks: 87

Student Marks:
Vihaan : 65
vamika : 98
rohan : 49
Vyom : 90
Niharika : 87

Enter new student name: Pamila
Enter marks: 79

After Adding New Student:
Vihaan : 65
vamika : 98
rohan : 49
Vyom : 90
Niharika : 87
Pamila : 79

Enter the student name to update marks: Vihaan
Enter new marks: 80
Marks updated successfully.

Enter the student name to delete: rohan
Student deleted successfully.

Updated Student Records:
Vihaan : 80
vamika : 98
Vyom : 90
Niharika : 87
Pamila : 79

Highest Scorer:
Name : vamika
Marks: 98
"""