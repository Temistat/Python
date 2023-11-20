print("""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW1 - Q2 (etc.)
Date due: 2020-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
""")

Current_population = 330109174
Years = int(input("Please enter the number of years: "))
print(Years)

Years =  int((Years * 365) * 86400)

Birth = Years / 7
Death = Years / 13
New_Immigrant = Years / 35
New_Citizens = Birth + Death + New_Immigrant

Estimated_population = int(Current_population + New_Citizens)
print(Estimated_population)




