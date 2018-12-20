a = int(input("Side a = "))
b = int(input("Side b = "))
c = int(input("Side c = "))

if a != b and b != c and a != c:
    print("This is a scalene triangle.")

elif a == b and b ==  c:
    print("This is an equilateral triangle.")

else:
    print("This is an isosceles triangle.")
