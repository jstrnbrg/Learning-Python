from sys import argv
from os.path import exists
# import two methods

script, from_file, to_file = argv
#set argv to take in 3 arguments

#print(f"Copying from {from_file} to {to_file}")
in_data = open(from_file).read()
# initialise var in_data by opening from_file and
#reading its contents and push these to in_data


print(f"The input file is {len(in_data)} bytes long")
#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, "w")
#open the to_file in write mode and create var out_file
out_file.write(in_data)
#write contents stored in var in_data into out_file

#print("Alright, all done.")

out_file.close()
