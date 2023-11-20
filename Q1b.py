##Author: [Your name here]
##Assignment / Part: HW2 - Q2a (etc.)
##Date due: 2021-02-17
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

Weight = float(input("Please enter weight in pounds: "))
Weight = Weight * 0.453592
Height = float(input("Please enter height in inches: "))
Height = Height * 0.0254
BMI = Weight / (Height ** 2)
print("BMI is:", BMI)
