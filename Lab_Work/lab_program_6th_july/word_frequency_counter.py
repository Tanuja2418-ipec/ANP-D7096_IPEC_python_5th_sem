"""Lab 2: Word Frequency Counter
Problem Statement:
Accept a sentence from the user and create a dictionary that stores the frequency of each word.

Example:

Input:
python is easy and python is powerful

Output:
{
'python': 2,
'is': 2,
'easy': 1,
'and': 1,
'powerful': 1
}
Additionally:

Display the most frequently occurring word.
Display all words in alphabetical order."""


#-------------------------------Coding section-------------------------------

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Creating an empty dictionary
frequency = {}

# Count the frequency of each word
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

# Display the frequency of each word
print("\nWord Frequency:")
print(frequency)

# Find the most frequently occurring word
most_word = max(frequency, key=frequency.get)

# Display the most frequent word
print("\nMost Frequent Word:")
print(most_word, ":", frequency[most_word])

# Display words in alphabetical order
print("\nWords in Alphabetical Order:")
for word in sorted(frequency):
    print(word, ":", frequency[word])


"""
Enter a sentence: This is a test sentence

Word Frequency:
{'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence': 1}

Most Frequent Word:
This : 1

Words in Alphabetical Order:
This : 1
a : 1
is : 1
sentence : 1
test : 1


Enter a sentence: I know I am not expert

Word Frequency:
{'I': 2, 'know': 1, 'am': 1, 'not': 1, 'expert': 1}

Most Frequent Word:
I : 2

Words in Alphabetical Order:
I : 2
am : 1
expert : 1
know : 1
not : 1
"""    