fname = input("Enter file name: ")

try:
    file = open(fname)
except:
    print("Failed to open file: ", fname)
    exit()

for line in file:

    print(line.upper())
