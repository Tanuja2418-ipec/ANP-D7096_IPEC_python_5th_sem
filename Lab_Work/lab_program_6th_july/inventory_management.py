""" Lab 4: Inventory Management
Problem Statement:
Create a dictionary to maintain the stock of products in a shop.

Example:

{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10
}
Implement the following:

Add a new product.
Update the stock of an existing product.
Remove a product from inventory.
Display products having stock less than 20.
Display the total number of items available in the inventory."""

#--------------------------coding section-------------------------------


# Inventory Management

# Create an empty dictionary
inventory = {}

# Take input for 4 products
for i in range(4):
    product = input("Enter product name: ")
    stock = int(input("Enter stock: "))
    inventory[product] = stock

# Display all products and stock
print("\nInventory:")
for product in inventory:
    print(product, ":", inventory[product])

# Add a new product
product = input("\nEnter new product name: ")
stock = int(input("Enter stock: "))
inventory[product] = stock

# Display inventory after adding
print("\nAfter Adding New Product:")
for product in inventory:
    print(product, ":", inventory[product])

# Update stock of an existing product
product = input("\nEnter product name to update: ")

if product in inventory:
    inventory[product] = int(input("Enter new stock: "))
    print("Stock updated successfully.")
else:
    print("Product not found.")

# Display inventory after updating
print("\nAfter Updating Stock:")
for product in inventory:
    print(product, ":", inventory[product])

# Remove a product
product = input("\nEnter product name to remove: ")

if product in inventory:
    del inventory[product]
    print("Product removed successfully.")
else:
    print("Product not found.")

# Display inventory after removing
print("\nAfter Removing Product:")
for product in inventory:
    print(product, ":", inventory[product])

# Display products having stock less than 20
print("\nProducts with stock less than 20:")
for product in inventory:
    if inventory[product] < 20:
        print(product, ":", inventory[product])

# Display total number of items in inventory
total = 0

for product in inventory:
    total = total + inventory[product]

print("\nTotal number of items in inventory:", total)



#---------------------------output section--------------------------------

"""
Enter product name: Laptop
Enter stock: 15
Enter product name: Mouse
Enter stock: 40
Enter product name: Keyboard
Enter stock: 25
Enter product name: Monitor
Enter stock: 10

Inventory:
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10

Enter new product name: Printer
Enter stock: 12

Enter product name to update: Laptop
Enter new stock: 20
Stock updated successfully.

Enter product name to remove: Mouse
Product removed successfully.

Products with stock less than 20:
Monitor : 10
Printer : 12

Total number of items in inventory: 57
"""