##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW3 - Q2 
##Date due: 2022-02-24
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

day = input("Enter the day the call started at: ")
time = int(input("Enter the time the call started at (hhmm): "))
length = float(input("Enter the duration of the call (in minutes): "))

if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr" or day == "Fri":
    if time >= 600 and time <= 2100:
        cost = length * 0.50
    elif time <= 600 or time >= 2100:
          cost = length * 0.30
elif day == Sat or day == Sun:
      cost = length * 0.15
     
print("This call will cost", cost)
