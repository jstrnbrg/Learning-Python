#from sys import maths

x = 2
y = 4
z = 5

def if_else():
    if x == y and x == z:
        print("all numbers equal")
    elif x < y or x < z:
        print("x is smaller than y or smaller than z")
    else:
        print("weird numbers")

if_else()
