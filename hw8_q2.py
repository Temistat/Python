"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW8 - Q2
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def clean_up(input_file_name , a_list_characters_to_remove, output_file_name):
    new_line = ""
    try:
        file = open(input_file_name, 'r')
    except FileNotFoundError:
        new_file = open(output_file_name, 'w')
        print("INPUT FILE NOT FOUND", file=output_file_name)
        new_file.close()
    else:
        lst = file.readlines()
        for i in range(len(lst)):
            lst[i].strip() 
        for line in lst:
            for word in line:
                for char in word:
                    if not char in a_list_characters_to_remove:
                       new_line += char
        file.close()               
        new_file = open(output_file_name, 'w')
        new_file.write(new_line)
        new_file.close()
    
def main():
    clean_up("the_social_contract.txt", ["a", "i", "o", "u", "e"], "clean.txt")

main()
