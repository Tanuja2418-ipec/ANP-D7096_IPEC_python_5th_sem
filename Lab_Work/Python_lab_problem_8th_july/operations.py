"""
Problem Statement: Geometry Calculator Using Python Module

Develop a menu-driven Python application that demonstrates the use of User-Defined Modules and Functions.

Requirements

You are required to create a Python module named twodfigures.py that contains functions to perform the 
following calculations for different two-dimensional shapes:

Triangle
    Calculate Area
    Calculate Perimeter
Circle
    Calculate Area
    Calculate Circumference (Perimeter)
Square
    Calculate Area
    Calculate Perimeter
Rectangle
    Calculate Area
    Calculate Perimeter
Create another Python file named operations.py that imports the twodfigures module and performs the following tasks:

Display a menu for selecting one of the following figures:
     Square
     Circle
     Triangle
     Rectangle
Based on the user's choice, ask for the required dimensions of the selected figure.
Example:
Circle → Radius
Square → Side
Rectangle → Length and Breadth
Triangle → Three sides (for perimeter) and Base & Height (for area)
Display a second menu to choose the required operation:
Area
Perimeter
Call the appropriate function from the twodfigures module based on the user's selections. 
Display the calculated result in a user-friendly format. Allow the user to perform multiple calculations until 
they choose to exit the application.
"""

#-----------------------------------coding section-----------------------------------------------

# Importing the user-defined module
import twodfigures

# Loop runs until the user chooses Exit
while True:

    # Display the main menu
    print("---------------------GEOMETRY CALCULATOR-----------------------")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    #Asking user to choose a shape to perform operation
    choice = int(input("Enter your choice: "))

    # Exit condition
    if choice == 5:
      exit()

   
    print("\nChoose Operation")
    print("1. Area")
    print("2. Perimeter")

    #Asking user to choose operation to perform on the shape
    operation = int(input("Enter your choice: "))

    # ---------------- SQUARE ----------------
    if choice == 1:

        # Asking user to input side of square
        side = float(input("Enter side of square: "))

        # Calculating Area of square
        if operation == 1:
            result = twodfigures.square_area(side)
            print("Area of Square =", result)

        # Calculating Perimeter of square
        elif operation == 2:
            result = twodfigures.square_perimeter(side)
            print("Perimeter of Square =", result)

        # Invalid operation
        else:
            print("Invalid Operation!")

    # ---------------- CIRCLE ----------------
    elif choice == 2:

        # Asking user to input radius of circle
        radius = float(input("Enter radius of circle: "))

        # Calculation are of circle
        if operation == 1:
            result = twodfigures.circle_area(radius)
            print("Area of Circle =", result)

        # Calculating Circumference of the circle
        elif operation == 2:
            result = twodfigures.circle_perimeter(radius)
            print("Circumference of Circle =", result)

        #invalid operation
        else:
            print("Invalid Operation!")

    # ---------------- TRIANGLE ----------------
    elif choice == 3:

        # Calculating the Area of triangle
        if operation == 1:

            # Asking user to Input base and height
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            result = twodfigures.triangle_area(base, height)
            print("Area of Triangle =", result)

        # Calculating Perimeter of the triangle
        elif operation == 2:

            # Asking user to Input all three sides
            side1 = float(input("Enter first side: "))
            side2 = float(input("Enter second side: "))
            side3 = float(input("Enter third side: "))

            result = twodfigures.triangle_perimeter(side1, side2, side3)
            print("Perimeter of Triangle =", result)
       
        #invalid operation
        else:
            print("Invalid Operation!")

    # ---------------- RECTANGLE ----------------
    elif choice == 4:

        # Asking user to Input length and breadth
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        # Calculating Area of rectangle
        if operation == 1:
            result = twodfigures.rectangle_area(length, breadth)
            print("Area of Rectangle =", result)

        # calculating Perimeter of rectange
        elif operation == 2:
            result = twodfigures.rectangle_perimeter(length, breadth)
            print("Perimeter of Rectangle =", result)

        #invalid operation
        else:
            print("Invalid Operation!")

    # Invalid figure choice
    else:
        print("Invalid Choice!")


#--------------------------Output Section----------------------------


"""
---------------------GEOMETRY CALCULATOR-----------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 2

Choose Operation
1. Area
2. Perimeter
Enter your choice: 1

Enter radius of circle: 7
Area of Circle = 153.93804002589985

---------------------GEOMETRY CALCULATOR-----------------------
1. Square
2. Circle
3. Triangle
4. Rectangle
5. Exit
Enter your choice: 5

"""