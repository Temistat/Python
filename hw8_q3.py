"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW8 - Q3
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_longest_word(file_name):
    space = " "
    num = 0
    longest_word = ""
    main_lst = []
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        return []
    else:
        for line in file:
            lst = line.strip().split(space)
            main_lst.extend(lst)
        for word in main_lst:
            if len(word) >= num:
               num = len(word) 
               longest_word = word
        file.close()           
    return longest_word

def main():
    file_path = "los_justos.txt"
    print(get_longest_word(file_path))

main()
    
