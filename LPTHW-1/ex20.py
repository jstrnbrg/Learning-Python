from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())
#create function called print_all with one argument f
#when run, it prints the file passed in as f via the .read method

def rewind(f):
    f.seek(0)
#create function called rewind with one argument f
#if run, it runs .seek (0) on the file passed in via f
#which means that it resets the line counetr to 0

def print_line(line_count, f):
    print(line_count, f.readline(), end = "")
# create function called print_line that takes two arguments
#line_count and f
#when run, it performs .readline on f, taking into account line_count
#and prints just that line

current_file = open(input_file)
#we open the file passed in via input_file and
# save it to a new var called current_file

print("First let's print the whole file:\n")

print_all(current_file)
#we perform the function print_all on current_file

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1

print_line(current_line, current_file)
#we perform the function print_line on the current_file,
#taking into account the current_line var

current_line += 1
#then we increment current_line by 1

print_line(current_line, current_file)
#and we run print_line again

current_line +=  1
#then we increment current_line by 1

print_line(current_line, current_file)
#and we run print_line again
