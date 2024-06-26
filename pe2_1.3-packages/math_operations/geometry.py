# geometry.py

def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def area_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def area_circle(radius):
    """Calculate the area of a circle."""
    from math import pi
    return pi * radius ** 2