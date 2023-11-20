import math

Base = float(input('Enter the length of the triangle base: '))
Side = float(input('Enter the length of the triangles side A: '))
Gamma = float(input('Enter the value of angle Gamma in degrees: '))
Area = (Base * Side) * (math.sin(math.radians(Gamma)) / 2)
print('The area of the triangle is', Area)

