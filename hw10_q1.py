"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW10 - Q1 
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import random
class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name = weapon_name
        self.strength = strength
    def __str__(self):
        string = '{} Weapon object (strength: {})'.format(self.weapon_name,self.strength)
        return string
    def does_break(self):
        random_num = random.randint(0,1.0)
        if random_num < (self.strength / 2):
           return True
        else:
           return False
def main():
    some_weapon = Weapon("Rickenbacker 4003", 0.6)
    number_of_tests = 100
    number_of_breaks = 0
    for i in range(number_of_tests):
        if some_weapon.does_break():
            number_of_breaks += 1
    percentage = (number_of_breaks / number_of_tests) * 100
    print("The {} broke {}% of the time in {} tests!".format(some_weapon.weapon_name, round(percentage),number_of_tests))

main()        
