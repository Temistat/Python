class Character:
    def __init__(self, name, power, speed):
        self.name = name
        self.power = power
        self.speed = speed
    def add_power(self, power):
        self.power = self.power + power
        return self.power
    def remove_speed(self, speed):
        self.speed =- speed
        return self.speed
character = Character("temi", 100, 100)
print(character.add_power(50))
print(character.remove_speed(50))
