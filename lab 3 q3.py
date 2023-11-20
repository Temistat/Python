highest_exam = float(input("Enter your highest exam grade: "))
highest_exam = highest_exam * (30 / 100)
second_highest_exam = float(input("Enter your second highest exam grade: "))
second_highest_exam = second_highest_exam * (20 / 100)
third_highest_exam = float(input("Enter your third highest exam grade: "))
third_highest_exam = third_highest_exam * (15 / 100)
homework = float(input("Enter your average homework grade: "))
homework = homework * (20 / 100)
lab = float(input("Enter your average lab grade: "))
lab = lab * (15 / 100)

average = float(highest_exam + second_highest_exam + third_highest_exam + homework + lab) 

if average > 92:
    print("A")
elif 92 > average >= 90:
    print("A-")
elif 89 > average >= 87:
    print("B+")
elif 86 > average >= 83:
    print("B")
elif 82 > average >= 80:
    print("B-")
elif 79 > average >= 77:
    print("C+")
elif 76 > average >= 73:
    print("C")
elif 72 > average >= 70:
    print("C+")
elif 69 > average >= 67:
    print("D+")
elif 66 > average >= 60:
    print("D")
else:
    print("F")

    
