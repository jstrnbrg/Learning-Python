"""
 Write a simple program to simulate the operation of the grep command on
 Unix.
 Ask the user to enter a regular expression and count the number of
 lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
"""
import re

count = 0
expression = input("Enter a regular expression: ")

fhead = open("mbox-short.txt")

for line in fhead:
    line = line.rstrip()
    if re.search(expression, line):
        count +=1

print(count)

"""
    x = line.search(expression)
    print (x)
"""
