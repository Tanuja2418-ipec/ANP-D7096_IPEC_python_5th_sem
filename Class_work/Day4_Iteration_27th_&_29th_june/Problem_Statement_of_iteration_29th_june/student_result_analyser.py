"""Student Result Analyzer
Problem Statement
A teacher wants to analyze the marks of N students.
Accept the marks of each student (out of 100).
Finally display:
•
Highest Marks
•
Lowest Marks
•
Average Marks
•
Number of students who passed (Marks ≥ 40)
•
Number of students who scored distinction (Marks ≥ 75)"""


#------------------------------coding section--------------------------------------


# Accept the number of students
n = int(input("Enter the number of students: "))

# Accept marks of the first student
marks = float(input("Enter marks of Student 1: "))

# Initialize variables
highest = marks
lowest = marks
total = marks

# Initialize counters
if marks >= 40:
    passed = 1
else:
    passed = 0

if marks >= 75:
    distinction = 1
else:
    distinction = 0

# Accept marks for the remaining students
for i in range(2, n + 1):
    marks = float(input(f"Enter marks of Student {i}: "))

    # Add marks to total
    total += marks

    # Check for highest marks
    if marks > highest:
        highest = marks

    # Check for lowest marks
    if marks < lowest:
        lowest = marks

    # Count passed students
    if marks >= 40:
        passed += 1

    # Count distinction students
    if marks >= 75:
        distinction += 1

# Calculate average marks
average = total / n

# Display the results
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Number of Students Passed:", passed)
print("Number of Students with Distinction:", distinction)