"""
Author: [Temilolwa Omomuwasan]
Assignment / Part: HW5 - Q2
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


user_input = input("Say something: ")
length = len(user_input)
changes = 0
total = ''

for x in user_input:
    if ord(x) >= 65 and ord(x) <= 90:
       changes += 1
       x_value = ord(x) + 32
       x_1 = chr(x_value)
       total += x_1
    else:
        total += x
print(total)
print("Number of changes:",changes)

