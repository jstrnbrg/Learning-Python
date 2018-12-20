"""num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0,2):
    for y in range(0,3):
        print(num_list[x][y])
"""
# for each x, cycle though all yself.
# for example. for x=0, cycle through y=0, y=1 and y=2
# then increment x to x=1
# print[x][y]

import random
import sys
import os

random_num = random.randrange(0,101)

while(random_num != 15):

    random_num = random.randrange(0,101)
    print(random_num)

i = 0

while (i <= 20):
        if (i%2 == 0):
            print(i)
        elif (i == 9):
            break
        i += 1

def addnum(x, y):
    sumNum = x + y
    return sumNum
    # unless you return var, it will only be availbe inside the deef scope.

print(addnum(2,6))

long_String = "hello, how are you?"
print(long_String.capitalize())
print(long_String.find("hello"))
print(long_String.isalpha())
print(long_String.isalnum())
print(len(long_String))
print(long_String.replace("how", "pups"))
print(long_String.strip())

quote_list = long_String.split(" ")
print(quote_list)

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
