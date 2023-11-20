##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW3 - Q4 
##Date due: 2022-02-24
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

import math

value_a = float(input("Please enter value of a: "))
value_b = float(input("Please enter value of b: "))
value_c = float(input("Please enter value of c: "))
                
discriminant = (value_b ** 2) - (4 * value_a * value_c)

if value_a == 0 and value_b == 0 and value_c == 0:
    print("This equation has an infinite number of solutions")
elif (value_a == 0 and value_b == 0) or (value_a == 0 and value_c == 0):
      print("This equation has no solution")
elif discriminant == 0:
      Solution = -value_b / (2 * value_a)
      print("This equation has 1 solution: x =", Solution)
elif discriminant < 0:
      print("This equation has no real solution")
elif discriminant > 0:
      Solution_1 = ((-1 * value_b) + math.sqrt(discriminant)) / (2 * value_a)
      Solution_2 = ((-1 * value_b) - math.sqrt(discriminant)) / (2 * value_a)
      print("This equation has 2 solution: x =", Solution_1, "x =", Solution_2)
