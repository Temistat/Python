def count_digits(lst):
    dic = {}
    for num in lst:
        if num in dic:
           dic[num] += 1
        else:
           dic[num] = 1
    return dic      

           

