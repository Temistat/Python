class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age
        self.fav_treats = []
    def rename(self, name):
        self.name = name
    def birthday(self):
        self.age += 1
    def add_treat(self, treat):
        self.fav_treats.append(treat)
    def __str__(self):
        string = '{} is a type {} that is {} years old'.format(self.name, self.pet_type, self.age)
        line = ''
        for treat in self.fav_treats:
            line += treat
        string_1 = 'Favorite treats: {}\n'.format(line)
        return string string_1

def main():
    pets = []
    command = input('Enter a command: ')
    while command != 'q' and command != 'Q':
        if command == 'adopt':
           name = input('What is the name of the pet? ')
           pet_type = input('What type of pet is it? ')
           age = input('How old is the pet? ')
           pet_name = Pet(name, pet_type, age)
           pets.append(pet_name)
        elif command == 'treat':
            pet_name = input('Who is this treat for? ')
            treat = input('What is the name of the treat? ')
            for pet in pets:
                if pet.name == pet_name:
                   pet.add_treat(treat)
        elif command == 'rename':
            current_name = input('What is the current name of the pet? ')
            new_name = input('What is the new name of the pet? ')
            for pet in pets:
                if pet.name == current_name:
                    pet.rename(new_name)
        elif command == 'birthday':
             pet_name = input('Whose birthday is it?')
             for pet in pets:
                 if pet.name == current_name:
                    pet.birthday
        elif command == 'pets':
            for name in pets:
                print(name)
        command = input('Enter a command: ')        
        
main()

    
        
        
    
