import sys
sys.path.append('C:\\z_admin\\School\\Assignments\\add100\\python\\pe2_1.3-packages')

from math_operations import calculator,geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result: ", result)

rect_area = geometry.area_rectangle(6, 3)
tri_area = geometry.area_triangle(8, 6)
circ_area = geometry.area_circle(10)

print(f"Rectangle area: {rect_area}")
print(f"Triangle area: {tri_area}")
print(f"Circle area: {circ_area}")