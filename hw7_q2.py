"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW7 - Q2 
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def is_haiku(input_string):
    lst = input_string.split('/')
    syl_line_1 = lst[0].split(",")
    syl_line_2 = lst[1].split(",")
    syl_line_3 = lst[2].split(",")
    if (len(lst) == 3) and (len(syl_line_1) == 5) and(len(syl_line_2) == 7) and (len(syl_line_3) ==5)  :
       line = "True"
    else:
        line = "False"
    return line    



