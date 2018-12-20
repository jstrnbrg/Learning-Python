def count(string, letter):
    count = 0
    for x in string:
        if x == letter:
            count += 1
    return count

print(count("amy is a banana", "n"))

word = "mamamia"

print(word.count("i"))
