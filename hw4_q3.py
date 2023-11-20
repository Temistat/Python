##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW4 - Q3
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
      
number =int(number)
for row in range(1, number + 1):
    line = ""
    space = " " * (number - row)
    line += space
    for row1 in range(1, row + 1):
        line +=  str(row1)
    print(line)
   
