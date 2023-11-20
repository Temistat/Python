import random

Random_number = random.randint(0,100)

Even = (Random_number % 2) == 0
Number = Random_number > 50

print(Random_number, 'is even:', Even)
print(Random_number, 'is greater than 50:', Number)
