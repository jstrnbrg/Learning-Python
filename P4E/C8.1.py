"""
Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns
a new list that contains all but the first and last elements.
"""

t = ["Hi", "my", "name", "is", "John", "how", "are", "you"]

def chop(xxx):
    return xxx[1:len(xxx)-1]

def middle(xxx):
    new = xxx[2:len(xxx)-1]
    return new

print(chop(liste))
print(middle(liste))
