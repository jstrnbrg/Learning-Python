import math

def vol(radius):
    """Returns the volume of a sphere"""
    volume = (4.0/3.0) * math.pi * radius**3
    print(volume)

vol(2)
