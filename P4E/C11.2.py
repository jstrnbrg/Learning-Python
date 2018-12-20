"""
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and print
 out the average.
"""
import re

count = 0
sum = 0
fhead = open("mbox-short.txt")

for line in fhead:
    line = line.rstrip()
    if re.findall('^New Revision: ([0-9.]+)', line):
        x = re.findall('^New Revision: ([0-9.]+)', line)
        y = int(x[0])

        if len(x) > 0:
            count += 1
            sum = sum + y

average = sum / count
print(average)
