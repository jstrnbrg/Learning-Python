import string
fhand = open('romeo.txt')
counts = dict() # make new empty dictionary called counts
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower() # make everything in line lowercase
    words = line.split() # split line into words and assign that to words, which is a list
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1


# Sort the dictionary by value
lst = list() #make new empty list called lst
for key, val in counts.items(): # loop through the key-value pairs in counts
    lst.append((val, key)) # append pairs to lst

lst.sort(reverse=False)
for key, val in lst[:10]:
    print(key, val)
