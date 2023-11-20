##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW4 - Q4
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

line = ""
number = int(number)
for n in range(1, number + 1):
    num = n
    even = 0
    odd = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    if even > odd:
        line = line + str(num) + " "
print(line)

