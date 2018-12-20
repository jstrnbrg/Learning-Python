"""
Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values
from these lines. When you reach the end of the file, print out the average
spam confidence.
"""

fname = input("Enter file name: ")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        opened = open(fname)
    except:
        print("Failed to open file: ", fname)
        exit()

    count = 0
    total_spam = 0

    for line in opened:
        line = line.rstrip()
        if not line.startswith("X-DSPAM-Confidence"):
            continue
        start = line.find(":")
        extract = line[start + 2:]
        print(extract)
        count += 1
        spam = float(extract)
        total_spam += spam


    average = total_spam/count
    print("The average is: ", average)
