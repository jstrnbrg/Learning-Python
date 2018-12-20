'''
Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list.
If the word is not in the list, add it to the list.
When the program completes, sort and print the resulting words
in alphabetical order.
'''

fhead = open('romeo.txt')
final = []
for line in fhead:
    words = line.split()
    for word in words:
        if word not in final:
            final.append(word)
final.sort()
print(final)
