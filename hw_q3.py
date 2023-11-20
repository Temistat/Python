"""
Author: [Temiloluwa Omomuwasan]
Assignment / Part: HW9 - Q2
Date due: 2022-04-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def get_battle_stats(hp,attack,defense,special_attack,special_defense,speed):
    dic = {}
    dic["HP"] = hp
    dic["Attack"] = attack
    dic["Defense"] = defense
    dic["Sp.Atk"] = special_attack
    dic["Sp.Def"] = special_defense
    dic["Speed"] = speed
    return dic

def create_entry(number,name,type_1,type_2,health_points,attack,defense,special_attack,special_defense,speed,generation,is_legendary):
    dic = {}
    dic["Number"] = number
    dic["Name"] = name
    dic["Types"] = (type_1, type_2)
    dic["BattleStats"] = get_battle_stats(health_points,attack,defense,special_attack,special_defense,speed)
    dic["Generation"] = generation
    dic["Legendary"] = is_legendary
    return dic

def create_pokedex(filepath):
    dic = {}
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return {}
    file.readline
    for lines in file:
        lst = lines.strip().split(",")
        entry = create_entry(lst[0],lst[1],lst[2],lst[3],lst[5],lst[6],lst[7],lst[8],lst[9],lst[10],lst[11],lst[12])
        dic[lst[1]] = entry
    file.close()    
    return dic

def main():
    filepath = "pokemon.csv"
    pokedex = create_pokedex(filepath)
    pokemon_key = "Glaceon"
    try:
        my_favorite_pokemon = pokedex[pokemon_key]
    except KeyError:
        print("ERROR: Pokemon {} does not exist!".format(pokemon_key))
    else:
        print("PRINTING {}'S INFORMATION..." .format(pokemon_key))
        for key in my_favorite_pokemon.keys():
            print("{}: {}".format(key, my_favorite_pokemon[key]))
        
main()    
