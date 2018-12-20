# Reading binary files using urllib


# This program reads all of the data in at once across the network
# This program will work if the size of the file is less than the size of the memory of your computer.
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

"""
In order to avoid running out of memory, we retrieve the data in blocks
(or buffers) and then write each block to your disk before retrieving
the next block.
"""

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb') # opens/creates file cover3.jpg in write-only mode
size = 0
while True:
    info = img.read(100000) #read at max 100k characters from img
    if len(info) < 1: break # break out of loop if length of info is 0
    size = size + len(info) #  add length of info to size (running counter)
    fhand.write(info) # write info to fhand

print(size, 'characters copied.')
fhand.close()
