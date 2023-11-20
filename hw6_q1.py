"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW6 - Q1 
Date due: 2022-03-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def print_shifted_triangle(height, margin, symbol):
    space_number = height - 1
    for n in range(1, height * 2, 2):
        space = " " * (margin + space_number)
        space_number -= 1
        line = space + (n * symbol)
        print(line)

def print_pine_tree(levels, symbol):
    for n in range(2,levels + 2):
        print_shifted_triangle(n, levels - n + 1, symbol)
        
def main():
    num = int(input("Enter a positive, non-zero, integer: "))
    symbol = input("Enter a non-whitespace, non-alphanumeric character: ")
    diagram = print_pine_tree(num, symbol)
        
main()
