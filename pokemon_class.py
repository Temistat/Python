import random
class Pokemon:
    def __init__(self, pokemon_name, nickname, level, types_1, types_2, hp, attack, speed):
        self.pokemon_name = pokemon_name
        self.nickname = nickname
        self.level = level
        self.types = (types_1, types_2)
        self.hp = hp
        self.stats = {"attack": attack , "speed": speed}
    def __str__(self):
        return "{} pokemon object {} of type(s) {}{}{}, level {}".format(self.pokemon_name,
                                                                        self.nickname,
                                                                        self.types[0],
                                                                        '/' if self.types[1] != '' else '',  
                                                                        self.types[1],
                                                                        self.level)
    
    def will_land_critical_hit(self):
        random_value = random.random(0, 256)
        threshold_value = self.stats["speed"] / 2
        return threshold_value > random_value
   
    def attack(self):
        if will_land_critical_hit(self):
           multiplier = ((2 * self.level) + 5) / (self.level + 5)
           self.stats["attack"] *= multiplier
        return self.stats["attack"]
    def __gt__(self,other):
        return self.stats["speed"] > other.stats["speed"]
        






##def main():
##     your_TA = Pokemon("Acideon", "Apoorva", 50, "Fire", "Water", 180, 135, 70)
##     print(your_TA.pokemon_name)
##     print(your_TA.nickname)
##     print(your_TA.level)
##     print(your_TA.types)
##     print(your_TA.hp)
##     print(your_TA.stats)
##main()

##def main():
##     starter_pokemon = Pokemon("Aegislash", "Napoleon", 75, "Steel", "Ghost", 160, 55, 80)
##     number_of_tests = 10
##     for test_number in range(number_of_tests):
##         attack_power = starter_pokemon.attack()
##         print("In move #{}, {} '{}' attacked with {} power.".format(test_number + 1,
##                                                                     starter_pokemon.pokemon_name,
##                                                                     starter_pokemon.nickname,
##                                                                     attack_power))
##main()

##def main():
##     trainer_pokemon = Pokemon("Glaceon", "Miu", 80, "Ice", "", 200, 55, 90) 
##    # speed stat: 90
##     rival_pokemon = Pokemon("Sylveon", "Ayaka", 75, "Fairy", "", 160, 55,
##    80) # speed stat: 80
##     winner = "{}".format(trainer_pokemon.pokemon_name if trainer_pokemon >
##    rival_pokemon else rival_pokemon.pokemon_name)
##     print(winner)
##main()
