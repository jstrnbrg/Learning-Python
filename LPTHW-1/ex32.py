#Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = [[1,2,3],[4,5,6]]

for i in range(len(elements)):
    for x in range(len(elements[1])):
        print("Result: ", elements[i][x])
    #elements.append(i)

for i in elements:
    print(f"Element was: {i}")
