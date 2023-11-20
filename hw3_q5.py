##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW3 - Q2 
##Date due: 2022-02-24
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

first_side = float(input("Length of the first side: "))
second_side = float(input("Length of the second side: "))
third_side = float(input("Length of the third side: "))

if first_side == second_side and first_side == third_side and third_side == second_side:
    triangle = "an equilateral triangle"
elif first_side == second_side or first_side == third_side or third_side == second_side:
      if first_side == 90 or second_side == 90 or third_side == 90:
          triangle = "an isosceles right triangle"
      else:
          triangle = "an isosceles triangle"
else:
     triangle = "a triangle that is not an isosceles and not an equilateral (i.e. scalene)"

print(first_side, second_side, third_side, "form", triangle)        
