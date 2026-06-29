""" Employee Salary Statistics
Problem Statement
A company has N employees.
Accept the salary of each employee and determine:
•
Highest salary
•
Lowest salary
•
Average salary
•
Number of employees earning more than ₹50,000"""


#-------------------------------Coding section---------------------------

# Accept the number of employees
n = int(input("Enter the number of employees: "))

# Accept the salary of the first employee
salary = float(input("Enter salary of Employee 1: "))

# Initialize variables
highest = salary
lowest = salary
total = salary

# Count employees earning more than 50000
if salary > 50000:
    count = 1
else:
    count = 0

# Accept salaries of the remaining employees
for i in range(2, n + 1):
    salary = float(input(f"Enter salary of Employee {i}: "))

    # Add salary to total
    total += salary

    # Check for highest salary
    if salary > highest:
        highest = salary

    # Check for lowest salary
    if salary < lowest:
        lowest = salary

    # Count employees earning more than 50000
    if salary > 50000:
        count += 1

# Calculate average salary
average = total / n

# Display the results
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning more than ₹50,000:", count)