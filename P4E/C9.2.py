"""
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines that
start with “From”, then look for the third word and keep a running count
of each of the days of the week. At the end of the program print out the
contents of your dictionary (order does not matter).
"""

fhead = open("mbox-short.txt")

days = {}

for line in fhead:
    if line.startswith("From "):
        words = line.split()
        third = words[2]
        if third not in days:
            days[third] = 1
        if third in days:
            days[third] += 1
                
print(days)
