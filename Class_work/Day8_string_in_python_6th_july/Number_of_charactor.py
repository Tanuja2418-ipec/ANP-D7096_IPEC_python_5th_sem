""" Write a python program to count the number of uppercase characters and lowercase characters in a given sentence, without using any library function."""

# taking input from user
sentence = input("Enter a sentence: ")

# displaying the sentence to the user
print("The sentence you entered is: ", sentence)

# initializing counters for uppercase and lowercase characters
uppercase = 0
lowercase = 0

# looping through each character in the sentence
for char in sentence:
    if char >= 'A' and char <= 'Z':
        #incrementing the uppercase count by 1
        uppercase += 1
    elif char >= 'a' and char <= 'z':
        #incrementing the lowercase count by 1
        lowercase += 1

# displaying the counts
print("The number of uppercase characters in the given sentence is: ", uppercase)
print("The number of lowercase characters in the given sentence is: ", lowercase)

