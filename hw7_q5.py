"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW7 - Q5
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_matryoshka_list(original_list):
    lst = []
    lst_1 = []
    for i in range(len(original_list)):
        if i < len(original_list) - 1:
           if original_list[i + 1] > original_list[i]:
              lst.append(original_list[i])
           else:
              lst.append(original_list[i]) 
              lst_1.append(lst)
              lst = []
        else:
            lst.append(original_list[i])
            lst_1.append(lst)
    return lst_1


def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)
    print(matryoshka_list)

main()
