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
