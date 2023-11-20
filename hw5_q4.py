"""
Author: [Temilolwa Omomuwasan]
Assignment / Part: HW5 - Q4
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

string = input("Please enter a string of lowercase letters: ")
length = len(string)

for x in range(0,length):
    if x < length - 1:
       if string[x] < string[x + 1]:
          line = "is not decreasing"
       elif string[x] > string[x + 1]:
            line = "is decreasing"
    elif x == length - 1:
         if string[x] < string[x - 1]:
            line = "is decreasing"
         elif string[x] > string[x - 1]:
              line = "is not decreasing"
print(string, line)
     
