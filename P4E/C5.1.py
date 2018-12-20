'''
Write a program which repeatedly reads numbers until the user enters “done”.
Once “done” is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and
except and print an error message and skip to the next number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
"""
total = 0
count = 0
min = None
max = None
numbers = []

while True:
    number1 = input("Enter a number: ")
    if number1 == "done":
        break
    numbers.append(number2)
    total = total + int(number1)
    count += 1
average = total / count

for x in numbers:
    if max == None or x > max:
        max = x

for y in numbers:
    if min == None or y < min:
        min = y

print(total, count, average)
print(total, max, min)

"""


count = 0
numbers = []

while True:
    number1 = input("Enter a number: ")
    if number1 == "done":
        break
    number1 = int(number1)    
    numbers.append(number1)
    count += 1


print(max(numbers))
print(min(numbers))
print(type(max(numbers)))
