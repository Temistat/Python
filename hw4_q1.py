"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW4 - Q1 
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

number = float(input("Please enter a positive integer: "))
number_check = number % 1

while (number < 0) or (number_check != 0):
      number = float(input("Please enter a positive integer: "))
      number_check = number % 1
      
number = int((number * 2) + 1)
print("Executing while-loop...")

for n in range(2, number, 2):
 print(n)

print("Executing for-loop...")

for n in range(2, number, 2):
 print(n)

