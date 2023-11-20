##Question 2

num = int(input("Enter a number: "))

for num in range(1, num + 1):
    print("*" * num)

##Question 3

integer = int(input("Enter an integer: "))
string = []

while integer != 0:
    num = str(integer % 2)
    string.append(num)
    integer //= 2

string.sort
print( "".join(string[::-1]))

##Question 4
##
lst = []
line = ''
for i in range(1,6):
    for num in range(0+i):
        lst.append(i)

print(lst)

lst = [i for i in range(1,6) for num in range(0+i)]
print(lst)

##Question 4b

lst = []
for i in range(9):
    if i % 2 == 0:
       lst.append(i)
    else:
       i *= -1
       lst.append(i)
print(lst)       
num = 1
lst = [i  if i % 2 == 0 else i * -1 for i in range(9)]
print(lst)

##Question 5

def number_of_words(filename):
    dic = {}
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return "File Not Found"
    for word in file:
        if not word in dic:
           dic[word] = 1
        else:
            dic[word] += 1


##Question 6

class Student:
    def __init__(self, name, gpa, class_list = []):
        self.name = name
        self.gpa = gpa
        self.class_list = class_list
    def add_class(self, name_of_class):
        self.class_list.append(name_of_class)
    def remove_class(self, name_of_class):
        for i in self.class_list:
            if self.class_list[i] == name_of_class:
               self.class_list.pop(i)
class Class:
    def __init__(self, name, instructor, list_of_student = []):
        self.name = name
        self.instructor = instructor
        self.list_of_student = list_of_student
    def add_student(self, name_of_student):
        self.list_of_student.append(name_of_class)
    def remove_student(self, name_of_student):
        for i in self.list_of_student:
            if self.list_of_student[i] == name_of_class:
               self.list_of_student.pop(i)
    def average_gpa(self):
        gpa = 0
        for student in self.list_of_student:
            gpa += student.gpa
        return gpa
    
        








