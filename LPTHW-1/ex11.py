print("How old are you? ", end= '')
age = input("Enter your age: ")
print("How tall are you? ", end= '')
height = int(input())
print("How much do you weigh? ", end= '')
weight = int(input())
useless = weight * height

print(f"So you're {age} years old, {height} cm tall and {weight} kg heavy.")
print(f"Useless is {useless}")
