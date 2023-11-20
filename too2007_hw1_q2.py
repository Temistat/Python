##a
def shift(lst, k):
    for i in range(k):
        num = lst.pop(0)
        lst.append(num)
    return lst    
     
##b
def shift(lst, k, direction = left):
    if direction == 'left'
        for i in range(k):
            num = lst.pop(0)
            lst.append(num)
        return lst
    else:
        for i in range(k):
            num = lst.pop(-1)
            lst.insert(0, num)
        return lst
