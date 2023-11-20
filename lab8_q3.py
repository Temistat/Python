import random

def shuffle_create(lst):
    shuffle_lst = []
    for i in range(len(lst)):
        
        if not lst[i] in shuffle_lst:
           shuffle_lst += lst[i] 
    return shuffle_lst

shuffle_create(["A", 0, 0, 5, 1, 3, 2])


def shuffle_in_place(lst):
    pass
    
