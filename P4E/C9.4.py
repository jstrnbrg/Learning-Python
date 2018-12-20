"""
This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from
(i.e., the whole email address). At the end of the program,
 print out the contents of your dictionary.
"""
import string

messages = {}
most = []

name = input("Enter file name: ")
try:
    fhead = open(name)
except:
    print("Unable to open file")
    exit()

for line in fhead:
    line = line.rstrip()
    if not line.startswith("From "): continue # if line not starts with "From " then jump back to beginning of for loop
    words = line.split()
    address = words[1]
    start = address.find("@")
    important = address[:start]
    if important not in messages:
        messages[important] = 1
    else:
        messages[important] += 1

for key, value in list(messages.items()):
    most.append((value, key))


most.sort(reverse=True)

for key, value in most[:1]:
    print(value, key)
