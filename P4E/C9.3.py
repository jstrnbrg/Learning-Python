"""
Write a program to read through a mail log, build a his- togram using
a dictionary to count how many messages have come from each email address,
 and print the dictionary.
"""

name = input("Enter file name: ")
fhead = open(name)

messages = {}

for line in fhead:
    if line.startswith("From "):
        words = line.split()
        address = words[1]
        if address not in messages:
            messages[address] = 1
        else:
            messages[address] += 1

print(messages)

maximum = max(messages, key=messages.get)
print(maximum)

# don't use two sperate if statements that apply to the same thing twice
