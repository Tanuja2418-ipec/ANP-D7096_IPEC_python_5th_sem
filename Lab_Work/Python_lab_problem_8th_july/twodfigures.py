#----------------------Triangle----------------------------------

#function of calulate area of triangle
def calculate_area_of_triangle(base, height):
    return (1/2) * base * height

#function to calculate perimeter of triangle
def calculate_perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

#---------------------------Circle--------------------------------

#function to calculate area of circle
def calculate_area_of_circle(radius):
    return 3.14 * radius * radius

#function to calculate perimeter of circle
def calculate_perimeter_of_circle(radius):
    return 2 * 3.14 * radius

#-----------------------------Square------------------------------

#function to calculate area of square
def calculate_area_of_square(side):
    return side * side

#function to calculate perimeter of square
def calculate_perimeter_of_square(side):
    return 4 * side

#----------------------------Rectangle-----------------------------

#function to calculate area of rectangle
def calculate_area_of_rectangle(length, breadth):
    return length * breadth

#function to calculate perimeter of rectangle
def calculate_perimeter_of_rectangle(length, breadth):
    return 2 * (length + breadth)