def fibs(n):
    x = 0
    y = 1
    for i in range(n):
        yield x
        x, y = y, x + y 

for curr in fibs(8):
    print(curr, end = ' ')
    
