"""
This program counts the distribution of the hour of the day for
 each of the messages. You can pull the hour from the “From” line by
 finding the time string and then splitting that string into parts using
 the colon character. Once you have accumulated the counts for each hour,
 print out the counts, one per line, sorted by hour as shown below.

"""
import string
import re

messages = {}
most = []

name = input("Enter file name: ")
try:
    fhead = open(name)
except:
    print("Unable to open file")
    exit()

# without regular expressions
"""
for line in fhead:
    line = line.rstrip()
    if not line.startswith("From "): continue # if line not starts with "From " then jump back to beginning of for loop
    words = line.split()
    time = words[5]
    end = time.find(":")
    important = time[:end]
    if important not in messages:
        messages[important] = 1
    else:
        messages[important] += 1

lst = list(messages.items())
lst.sort()

for key, val in lst:
    print(key, val)
"""
print("x"*40)
#with regular expressions
for line in fhead:
    line = line.rstrip()
    x = re.findall("^From .* ([0-9][0-9]):", line)
    if len(x) > 0:
        print(x)
