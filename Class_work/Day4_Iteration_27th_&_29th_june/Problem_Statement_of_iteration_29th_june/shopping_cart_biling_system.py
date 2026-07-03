"""Shopping Cart Billing System
Problem Statement
A supermarket allows a customer to purchase multiple products.
The customer first enters the number of products.
For each product, enter:
•
Product Name
•
Quantity
•
Price per Unit
Finally display:
•
Individual Product Cost
•
Total Bill Amount
•
Most Expensive Product
•
Cheapest Product
•
Average Product Cost"""


#------------------------coding section------------------------------------


# Accept the number of products
n = int(input("Enter the number of products: "))

# Accept details of the first product
name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

# Calculate the cost of the first product
cost = quantity * price

# Initialize variables
total_bill = cost
highest_cost = cost
lowest_cost = cost
most_expensive = name
cheapest = name

# Display the cost of the first product
print(name, "Cost =", cost)

# Accept details for the remaining products
for i in range(2, n + 1):

    print("\nProduct", i)

    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))

    # Calculate product cost
    cost = quantity * price

    # Display individual product cost
    print(name, "Cost =", cost)

    # Add to total bill
    total_bill = total_bill + cost

    # Check for most expensive product
    if cost > highest_cost:
        highest_cost = cost
        most_expensive = name

    # Check for cheapest product
    if cost < lowest_cost:
        lowest_cost = cost
        cheapest = name

# Calculate average product cost
average_cost = total_bill / n

# Display final results
print("\nTotal Bill Amount:", total_bill)
print("Most Expensive Product:", most_expensive, "-", highest_cost)
print("Cheapest Product:", cheapest, "-", lowest_cost)
print("Average Product Cost:", average_cost)


#-----------------------------output section---------------------------------

"""
Output:
Enter the number of products: 3
Product 1
Enter Product Name: Apple
Enter Quantity: 2
Enter Price per Unit: 3
Apple Cost = 6.0
Product 2
Enter Product Name: Banana
Enter Quantity: 5
Enter Price per Unit: 1
Banana Cost = 5.0
Product 3
Enter Product Name: Orange
Enter Quantity: 3
Enter Price per Unit: 2
Orange Cost = 6.0
Total Bill Amount: 17.0
Most Expensive Product: Apple - 6.0
Cheapest Product: Banana - 5.0
Average Product Cost: 5.666666666666667

"""