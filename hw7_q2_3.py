"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW7 - Q3
Date due: 2022-04-07
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def is_haiku(input_string):
    lst = input_string.split('/')
    syl_line_1 = lst[0].split(",")
    syl_line_2 = lst[1].split(",")
    syl_line_3 = lst[2].split(",")
    if (len(lst) == 3) and (len(syl_line_1) == 5) and(len(syl_line_2) == 7) and (len(syl_line_3) ==5)  :
       line = "True"
    else:
        line = "False"
    return line

def haiku_string_parser(input_string):
    line_1 = ""
    line_2 = ""
    line_3 = ""
    check = is_haiku(input_string)
    if check == "True":
       lst = input_string.split('/')
       word_line_1 = lst[0].split(",")
       for word in word_line_1:
           line_1 += word
       word_line_2 = lst[1].split(",")
       for word in word_line_2:
           line_2 += word
       word_line_3 = lst[2].split(",")
       for word in word_line_3:
           line_3 += word
       line = "{} \n {} \n {}".format(line_1,line_2,line_3)
    else:
        line = "Not a haiku"
    return line
    
def main():
    haiku_string = input("Enter string: ")
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)

main()    

    
    
