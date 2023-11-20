"""
Author: [Temilolwa Omomuwasan]
Assignment / Part: HW5 - Q5
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

encoded_string = input("Enter an encoded string: ")
key = int(input("Enter a key: "))
length = len(encoded_string)
total = ''

for x in range(length - 1, -1, -1 * (key + 1)):
    if not encoded_string[x].isdigit():
       total += encoded_string[x] 

print(total)

