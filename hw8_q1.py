"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW8 - Q1 
Date due: 2022-04-14
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def format_latin_text(string):
    for i in range(len(string)):
        string[i] = string[i].upper()
    for word in string:
        word.replace('U', 'V')
    string = ''.join(string)
    return string

def get_unformatted_text(file_name):
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("Error! Could not open file {}".format(file_name))
        return []
    text_lst = file.readlines()
    for i in range(len(text_lst)):
        text_lst[i].strip()        
    file.close()
    return text_lst

def print_formatted_latin(input_file_path):
    unformatted_text = get_unformatted_text(input_file_path)
    latin_text = format_latin_text(unformatted_text)
    print(latin_text)
    
def main():
    print_formatted_latin("imperatoria_verba.txt")
    
main()



    


    
