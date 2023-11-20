def create_oscars_dict(file_name):
    dic = {}
    lst = []
    try:
        file = open(file_name, 'r', encoding="utf8")
    except FileNotFoundError:
        print("File Not Found")
        return None
    file.readline()
    for line in file:
        line = line.strip().split(',')

        lst.append(line)
    for line in lst:
        if lst[5] != "" and lst[7] != "":
              if lst[3] == "Best Actor" or lst[3] == " Best Actress":
                 name = lst[5]
                 movies = lst[7]
                 dic[name] = movies
    file.close()             
    return dic

def print_films(oscars_dict, name):
    movies = oscars_dict[name]
    if movies == "":
       print("Actor/actress not found")
    else:
       print("{} was nominated for the following films: {}".format(name, movies))

import random
def main():
    file_name = input("What is the name of the file: ")
    oscars_dict = create_oscars_dict(file_name)
    name = input("Enter the name of an Oscars nominee: ")
    while name != "q" or name != "Q":
        key_lst = []
        for key in oscars_dict:
            key_lst.append(key)
        if name == "random":
           name = key_lst[random.randint(0, len(lst))]
        print_films(oscars_dict, name)
        name = input("Enter the name of an Oscars nominee: ")

main()

    
