import pokemon_class
class ProfessorTrainer:
    def __init__(self, professor_name, filepath):
        self.professor_name = professor_name
        self.party = []
        load_pokemon(self)

    def load_pokemon(self):
        try:
            file = open(filepath, 'r')
        except FileNotFoundError:
            return
        file.readline()
        for line in file:
            line = line.strip().split(',')
            new_line = Pokemon(line[0], line[1], line[2], line[3], line[4], line[6], line[7], line[8])
            self.party.append(new_line)
        file.close()
        
    def __str__(self):
        print("ProfessorTrainer object {} and contains the following Pokemon objects:".format(self.professor_name))
        for item in self.party:
            print('{}, called {}{}'.format(item.pokemon_name,item.nickname,item.types))
                                                                                                  

def main():
     their_professor = ProfessorTrainer("Gary Oak", "save_file_2.csv")
     print(their_professor)

main()        
                                                                                                   
                                                                                                   
                                                                                                                                                        
