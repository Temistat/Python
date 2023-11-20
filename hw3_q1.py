##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW4 - Q1 
##Date due: 2022-02-24
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

user_current = float(input("Enter this user's current XP: "))

if user_current < 18.5:
    user_current = str(user_current)
    print("Level 1 Player (XP:", user_current + ")")
elif  18.5 <= user_current <= 24.9:
    user_current = str(user_current)
    print("Level 2 Player (XP:", user_current + ")")
elif  25.0 <= user_current <= 29.9:
    user_current = str(user_current)
    print("Level 3 Player (XP:", user_current + ")")
elif  30.0 <= user_current <= 39.9:
    user_current = str(user_current)
    print("Level 4 Player (XP:", user_current + ")")
elif  40.0 <= user_current <= 50.0:
    user_current = str(user_current)
    print("Level 5 Player (XP:", user_current + ")")
else:
    print("ERROR: Please enter a valid XP value.")
