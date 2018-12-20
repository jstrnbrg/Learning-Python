import urllib.request
lines = 0
chars = 0

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    lines +=1
    if lines <3:
        print(line.decode().strip())
    for char in line:
        chars +=1



print(lines)
print(chars)
