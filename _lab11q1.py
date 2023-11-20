my_dict = {"a": 15 , "c": 35 , "b": 20}

keys = my_dict.keys()
print(keys)
values = my_dict.values()
print(values)
pairs = my_dict.items()
print(pairs)

key_lst = []
keys = tuple(keys)
for key in keys:
    key_lst.append(key)
key_lst.sort()
order_lst = []
for key in key_lst:
    print("{},{}".format(key,my_dict[key]))

##values_lst = []
##values = tuple(values)
##for values in values:
##    values_lst.append(values)
##values_lst.sort()
##v_order_lst = []
##for key in key_lst:
##    print("{},{}".format(value,my_dict[key]))

get solution
