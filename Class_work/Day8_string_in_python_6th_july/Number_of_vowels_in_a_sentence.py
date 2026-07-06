"""Write a python program to count the number of vowels in a given sentence."""

#------------------------------------Coding section-----------------------------------------

#taking input from user
sentence = input("Enter a sentence: ")  

#displaying the sentence to the user
print("The sentence you entered is: ", sentence)

#initializing a vowel count as 0
vowel = 0


#looping through each character in the sentence
for char in sentence:
    if ( char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
         char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        #incrementing the vowel count by 1
        vowel += 1

print("The number of vowels in the given sentence is: ", vowel)


#-----------------------------------output section----------------------------------------


"""
Enter a sentence: Hello World
The sentence you entered is:  Hello World
The number of vowels in the given sentence is:  3

Enter a sentence: This is a test sentence.
The sentence you entered is:  This is a test sentence.
The number of vowels in the given sentence is:  7
"""