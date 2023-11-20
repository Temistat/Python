import math

def get_data():
    lst = []
    number = input("Please enter a number or Q to Quit: ")
    while number != "q" or number != "Q":
        lst += number
        number = input("Please enter a number or Q to Quit: ")
    return lst

def calculate_average():
    lst = get_data()
    num = 0 
    for i in range(len(lst)):
        num += i
    average = num / len(lst)
    return average

def calculate_median():
    lst = get_data()
    lst.sort()
    num = 0
    if len(lst) % 2 == 0:
       mid = len(lst) / 2
       for i in range(mid - 1, mid +1):
           num += lst[i]
       median = number / 2
    else:
        mid = math.floor(len(lst) / 2)
        
        median = lst[mid]
    return median

def calculate_maximum():
    lst = get_data()
    num = 0
    for i in range(len(lst)):
        if lst[i] > num:
           num = i
    return num


def calculate_minimum():
    lst = get_data()
    lst = lst.sort()
    minimum = lst[0]
    return minimum


    
