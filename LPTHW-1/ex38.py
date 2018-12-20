#Doing things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"
#a string called ten_things
print("Wait there are not 10 things in that list. Let's fix that.")

print(ten_things)

stuff = ten_things.split(' ')
#we perform .split() on ten_things and save the result to stuff

print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
#a list called more_stuff

for x in stuff:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    if len(stuff) >= 10:
        exit(0)
# as long as there aren't 10 items in stuff
# take more_stuff, pop the last item and store it in next_one
#print Adding next_one
#append stuff with next_one
#print the length of the list stuff

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1]) # print the second item
print(stuff[-1]) # print the last item
print(stuff.pop()) # print the list stuff without the last item
print(' '.join(stuff)) # print the list joined by spaces
print('#'.join(stuff[3:5])) # print item 3 and 4 of the list, joined by a #
