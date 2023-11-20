import random


level = int(input("What is your level?: "))
chance = 120 - (20 * level)

rare_item = random.randrange(0,100) < chance

print("Your loot box contains a rare item:", rare_item)

