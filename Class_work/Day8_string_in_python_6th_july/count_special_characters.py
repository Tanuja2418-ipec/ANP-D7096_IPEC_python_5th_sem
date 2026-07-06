""" Write a python program to count the number of special characters in a given sentence."""

#-------------------------------------coding section-----------------------------------------

#taking input from user
sentence = input("Enter a sentence: ")

#displaying the sentence to the user
print("The sentence you entered is: ", sentence)

#initializing a special character count as 0
special_characters = 0

# looping through each character in the sentence
for x in sentence:
    if x.isalnum() == False and x.isspace() == False:
        # incrementing the special character count by 1
        special_characters += 1

# displaying the count
print("The number of special characters in the given sentence is: ", special_characters)


#-----------------------------------output section----------------------------------------

"""
Enter a sentence: Hello, World!
The sentence you entered is:  Hello, World!
The number of special characters in the given sentence is:  2

Enter a sentence: This is a test sentence.
The sentence you entered is:  This is a test sentence.
The number of special characters in the given sentence is:  1
"""
