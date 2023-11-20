"""
Author: [Temilolwa Omomuwasan]
Assignment / Part: HW5 - Q1
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

password = input("Enter a password: ")
length = len(password)
lower_case = 0
upper_case = 0
number = 0
symbol = 0

if length >= 8:
    for x in password:
        if x.islower():
            lower_case += 1
        elif x.isupper():
            upper_case += 1
        elif x.isdigit():
            number += 1
        elif x.isalpha() == False:
            symbol += 1
    if lower_case >= 2 and upper_case >= 2 and number >= 1 and symbol >= 1:
        print("True")
    else:
        print("False")
else:
    print("False")

