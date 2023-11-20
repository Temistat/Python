import random

def get_random_word(filepath):
    file = open(filepath, 'r')
    file.strip()
    lst =[]
    for line in file:
        lst_1 = line.split()
        lst.append(lst_1)
    word =random.random(lst)
    return word
    
        
        
        
