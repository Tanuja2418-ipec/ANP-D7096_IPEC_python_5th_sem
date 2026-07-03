"""write a python program to create a tuple of 10 products given by the user. 
Display the lowest price, highest price, count the number of product where price is greater than 4000.
Note : Along with the price you are required to store the name of the products while displaying the lowest
and highest price products display the name of the product along with the price."""


#------------------------coding section----------------------------

#creating an empty list to store user input
list = []

print("Please enter 10 products with their prices:")
for i in range(10):
    print("Enter the details of the product ", i + 1)
    #taking input from the user for product name 
    name = input("Enter the name of the product: ")
    #taking input from the user for product price
    price = float(input("Enter the price of the product: "))
    #inserting the name and price as a tuple into the list
    list.append((name, price))

# converting the list to a tuple
products_tuple = tuple(list)

print("------------------------------------------------------------------")
print("The tuple of products is:", products_tuple)
print("------------------------------------------------------------------")

# Finding lowest and highest priced products
lowest = products_tuple[0]
highest = products_tuple[0]

count = 0

for product in products_tuple:
    if product[1] < lowest[1]:
        lowest = product

    if product[1] > highest[1]:
        highest = product

    if product[1] > 4000:
        count += 1

# Displaying results
print("\n----- Result -----")
print("Lowest Priced Product :", lowest[0], "- ₹", lowest[1])
print("Highest Priced Product:", highest[0], "- ₹", highest[1])
print("Number of products with price greater than ₹4000:", count)