"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW10 - Q2
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

from hw10_q1 import Weapon
from random import randint

class Duelist:
    def __init__(self, duelist_name,weapon):
        self.duelist_name = duelist_name
        self.weapon_inventory = weapon
        self.number_of_weapons = len(self.weapon_inventory)
    def __str__(self):
        weapon_1 = self.weapon_inventory[0].weapon_name
        weapon_2 = self.weapon_inventory[1].weapon_name
        weapon_3 = self.weapon_inventory[2].weapon_name
        string = "Duelist object '{}', carrying {}, {}, and {} Weapon objects.".format(self.duelist_name,weapon_1,weapon_2,weapon_3)
        return string
    def get_winner_of_duel_name(self, opponent):
        random_num = randint(0, self.number_of_weapons - 1)
        random_num_opp = randint(0, opponent.number_of_weapons - 1)
        if self.number_of_weapons == 0 and opponent.number_of_weapons == 0:
             winner = "NO CONTEST"
        elif self.number_of_weapons > 0 and opponent.number_of_weapons > 0:
             weapon_A = self.weapon_inventory[random_num]
             print("Duelist {} picked a {}".format(self.duelist_name, weapon_A.weapon_name)) 
             weapon_B = opponent.weapon_inventory[random_num_opp]
             print("Duelist {} picked a {}".format(opponent.duelist_name, weapon_B.weapon_name))
             if weapon_A.strength > weapon_B.strength:
                stronger = weapon_A
                if stronger.does_break:
                   winner = opponent.duelist_name
                else:
                   winner = self.duelist_name
             elif not weapon_A.strength > weapon_B.strength:
                  stronger = weapon_B
                  if stronger.does_break:
                     winner = self.duelist_name
                  else:
                     winner = opponent.duelist_name 
             else:
                  print("Both duelists picked weapons of the same strength! The winner will be decided purely by pseudo-randomly gener") 
                  random_number = randint(1,3)
                  if random_number == 1:
                     winner = self.duelist_name
                  else:
                     winner = opponent.duelist_name
        elif self.number_of_weapons > 0 or opponent.number_of_weapons > 0:
             if self.number_of_weapons > 0:
                winner = self.duelist_name
             else:
                 winner = opponents.duelist_name
        return winner
        
def main():
    # Creating my Weapon objects
    weapon_1 = Weapon("Rickenbacker 4001c64", 0.8)
    weapon_2 = Weapon("Hofner 500/1", 0.6)
    weapon_3 = Weapon("Squier VI", 0.4)
    weapon_4 = Weapon("Rickenbacker 330", 0.8)
    weapon_5 = Weapon("Fender Vintera 60s Mustang", 0.6)
    weapon_6 = Weapon("Gretsch 6122", 0.4)
    # Creating my Duelist objects
    bass_player = Duelist("Aki Mizuguchi", [weapon_1, weapon_2, weapon_3])
    guitarist = Duelist("Yori Asanagi", [weapon_4, weapon_5, weapon_6])
    # Testing the get_winner_of_duel_name method of the Duelist object 'bass_player' a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner = bass_player.get_winner_of_duel_name(guitarist)
        print("THE WINNER OF DUEL #{} IS {}!".format(duel_number + 1, winner), end="\n\n")
main()                
        
