print("""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW1 - Q4
Date due: 2020-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
""")

print("Please enter your amount in the format of dollars and cents in two separate lines.")
Dollars = int(input(""))
Cents = int(input(""))

Dollars = int(Dollars * 100)
Total = int(Dollars + Cents)

Quarters = int(Total // 25)
Dimes = int(Total % 25) // 10
Nickels = int(Dimes % 10) // 5
Pennies = Total - ((Quarters * 25) + (Dimes * 10) + (Nickels * 5))

print('4 dollars and 37 cents are:', Quarters, 'quarters,', Dimes, 'dimes,', Nickels, 'nickels,', Pennies, 'pennies')
      



      
