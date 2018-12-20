from sys import argv
script, filename = argv
txt = open(filename)
#opens the file specified as filename
# and gives it the variable txt

print(f"Here's your file {filename}")
print(txt.read())
#reads and prints the var txt

print("Type your filename again:")
file_again = input(">")
#asks to input name of file and
#stores that name in the var file_again

txt_again = open(file_again)
#opens the file specified by the var file_name
#and gives it a new var txt_again

print(txt_again.read())
#reads txt_again and prints contents
