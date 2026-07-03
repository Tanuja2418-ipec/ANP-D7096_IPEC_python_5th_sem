"""problem statement :
write a program to create a list and delete the element from the list .
Ask the user for the element to be deleted and display the updated list after deletion.
"""
#--------------------------------------Coding Section---------------------------------

#Creating a List of 12 elements
list = [10, 20, 67, 40, 57, 60, 70, 42, 90, 10, 40, 17]

#displaying the numbers
print("The Numbers are : " )
print(list)

print("--------------------------------------------------------------")

#Removing the element from the list
element = int(input("Enter the element to be deleted: "))
list.remove(element)

#displaying the updated list after deletion
print("Updated list after deletion of", element, ":")
print(list)


#---------------------------------output Section----------------------------------
"""
Output 1 :-  

The Numbers are :
[10, 20, 67, 40, 57, 60, 70, 42, 90, 10, 40, 17]
--------------------------------------------------------------
Enter the element to be deleted: 40
Updated list after deletion of 40 :
[10, 20, 67, 57, 60, 70, 42, 90, 10, 40, 17]


Output 2 :-

The Numbers are :
[10, 20, 67, 40, 57, 60, 70, 42, 90, 10, 40, 17]
--------------------------------------------------------------  
Enter the element to be deleted: 100
Traceback (most recent call last):
  File "deletion_of_element.py", line 19, in <module>
    list.remove(element)
ValueError: list.remove(x): x not in list

"""