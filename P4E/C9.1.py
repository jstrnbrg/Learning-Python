"""
Write a program that reads the words in words.txt and stores them as keys i
n a dictionary. It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a
string is in the dictionary.
"""

dictionary = {}

fhead = open("words.txt")
for line in fhead:
    words = line.split()
    for word in words:
        dictionary[word] = ""

print(dictionary)
