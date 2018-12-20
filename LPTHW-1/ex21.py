def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Substracting {a} and {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(50, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
what = height - ((iq / 2) * weight) + age
print(f"That becomes: {what}. Can you do it by hand?")
