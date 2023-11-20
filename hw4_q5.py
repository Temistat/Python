##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW4 - Q5
##Date due: 2022-03-03
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

import turtle

number = float(input("Enter a positive integer: "))
number_check = number % 1

while (number < 0) or (number_check != 0):
      number = float(input("Please enter a positive integer: "))
      number_check = number % 1

number = int(number)
zellij_set = 20
inner_angle = 360 / number

for n in range(1, zellij_set + 1):
    if n ==1:
       for m in range(number):
           turtle.forward(100)
           turtle.right(inner_angle)
    else:
        turtle.right(360 / zellij_set)
        for m in range(number):
           turtle.forward(100)
           turtle.right(inner_angle)
        
           




      
