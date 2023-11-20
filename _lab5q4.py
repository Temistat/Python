user_input = input("Word 1: ")
user_input_1 = input("Word 2: ")
distance = 0

for x in user_input:
    if not x in user_input_1:
       distance += 1

print(user_input, "and", user_input_1, " Hamming distance is", distance)
