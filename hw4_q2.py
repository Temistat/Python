##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW4 - Q2 
##Date due: 2022-03-03
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

number = float(input("Enter a positive integer: "))
number_check = number % 1

while (number < 0) or (number_check != 0):
      number = float(input("Please enter a positive integer: "))
      number_check = number % 1
formula = (2 * number) - 1
formula = int(formula)
space_number = 0
for n in range(formula, 0, -2):
    space = " " * space_number
    space_number +=1
    hourglass = space + (n * "*")
    print(hourglass)
space_number -=2
for n in range(3, formula + 2, 2):
    space = " " * space_number
    space_number -=1
    hourglass = space + (n * "*")
    print(hourglass)
