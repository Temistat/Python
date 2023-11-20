"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW7 - Q4 
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import super_secrect_module

    
def is_impostor(information,corrupter_function):
    lst = corrupter_function(information)
    lst.append("b")
    if lst == information:
       line = "False"
    else:
       line = "True"
    return line   
    
    

def main():
    original_list = [1, 2, 3]
    print(is_impostor(original_list, super_secrect_module.corrupter))

main()
