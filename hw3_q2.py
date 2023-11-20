##Author: [Temiloluwa Omomuwasan]
##Assignment / Part: HW3 - Q2 
##Date due: 2022-02-24
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

import random

pokemon_level = int(input("What is this Pokémon's level? "))
pokemon_speed = int(input("What is this Pokémon's speed? "))
random_value = random.randrange(0,256)
threshold_value = pokemon_speed / 2

if threshold_value > random_value:
   damage_multiplier = ((2 * pokemon_level + 5) / (pokemon_level + 5))
   damage_multiplier = str(damage_multiplier)
   print("The Pokémon's move will be", damage_multiplier + "x stronger!")
else:
    print("The Pokémon's move will be 1x stronger!")

