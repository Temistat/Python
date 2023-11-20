import random

chance = 0.5
limit = 11

for row in range(1, limit):
    line = ""
    if (random.random() < chance):
        for col in range(1, row + 1):
            line = line + str(col * row) + "\t"
    else:
        for col in range(row, 0, -1):
            line = line + str(col * row) + "\t"
    print(line)        
