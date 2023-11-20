print("""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW1 - Q3 
Date due: 2020-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
""")

print("Please enter number of coins")
Quarters = int(input("Please enter number of quarters: "))
Dimes = int(input("Please enter number of dimes: "))
Nickels = int(input("Please enter number of nickels: "))
Pennies = int(input("Please enter number of pennies: "))

Quarters = Quarters * 25
Dimes = Dimes * 10
Nickels = Nickels * 5
Total = int(Quarters + Dimes + Nickels + Pennies)

Dollars = Total // 100
Cents = Total % 100

print('The total is', Dollars, 'dollars and', Cents, 'cents')
