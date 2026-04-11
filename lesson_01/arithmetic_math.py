import math
from unittest import result

friends = 5
friends += 1
friends -= 2
friends *= 3
friends /= 4
friends **= 5
remainder = friends % 6

print(friends)
print(remainder)


x = 3.14
y = -4
z = 5

result1 = round(x)
result2 = abs(y)
result3 = pow(4, 3)
result4 = max(x, y, z)
result5 = min(x, y, z)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


x = 9.61
result6 = math.sqrt(x)
print(result6)

result7 = math.ceil(x)
print(result7)

result8 = math.floor(x)
print(result8)

radius = float(input("Enter the radius of a circle: "))


circumference = 2 * math.pi * radius
print(f"The circumference of a circle is: {round(circumference, 2)} cm")

area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)} cm²")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuse of the triangle is {round(c, 2)} cm")