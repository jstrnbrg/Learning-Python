"""
Write a program that reads a file and prints the letters
in decreasing order of frequency.
Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation, or anything other than the letters a-z.
Find text samples
from several different languages and see how letter frequency varies
between languages. Compare your results with the tables at
https://wikipedia.org/wiki/Letter_frequencies.
"""

import string
from string import digits

dict1 = {}
count = 0

#name = input("Enter file name: ")
try:
    fhead = open("sentence.txt")
except:
    print("Unable to open file")
    exit()

for line in fhead:
    line = line.rstrip()
    line = line.lower()

    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', digits))

    words = line.split()

    for word in words:
        chars = list(word)
        print(chars)
        print("-"*40)

        for char in chars:
            count += 1
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1


lst = list(dict1.items())
lst.sort()
for key, val in lst:
    print(key, val/count*100,"%")
print("Count: ", count)




"""
    if important not in messages:
        messages[important] = 1
    else:
        messages[important] += 1

lst = list(messages.items())
lst.sort()

print(lst)
for key, val in lst:
    print(key, val)

"""
