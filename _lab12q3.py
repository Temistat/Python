class Passenger:
    def __init__(self, name, citizenship, num_bags):
        self.name = name
        self.citizenship = citizenship
        self.num_bags = num_bags
    def __str__(self):
        string = '{} is a citizen of {} and has {} bags'.format(self.name,self.citizenship,self.num_bags)
        return string
    def remove_bag(self):
        self.num_bags -= 1
    def add_bag(self):
        self.num_bags += 1

class Airplane:
    def __init__(self, number, aircraft, departure_location, arrival_location,departure_time, arrival_time):
        self.number = number
        self.aircraft = aircraft
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = []
    def __str__(self):
        string = '{} ({}) departs {} at {} and arrives at {} at {}'.format(self.number,self.aircraft,self.departure_location,self.departure_time,self.arrival_location,self.arrival_time)
        return string
    def print_passengers(self):
        line = ''
        print('There are {} passengers on this flight: '.format(len(self.passengers)))
        for name in self.passengers:
            print(name)

    def add_passenger(self, p):
        if p in self.passengers:
            return False
        else:
           self.passengers.append(p)
           return True
    def remove_passenger(self, p):
        for i in range(len(self.passengers)):
            if not p in self.passengers:
               return False 
            elif self.passengers[i] == p:
               self.passengers.pop(i)
               return True
            
    def get_passenger_count(self):
        num = len(self.passengers)
        return num

def main():
     flight_eu = Airplane(6783, "Airbus A320", "London", "Paris", "12:00","14:00")
     bob = Passenger("Bob", "France", 2)
     alice = Passenger("Alice", "France", 1)
     henry = Passenger("Henry", "UK", 1)
     flight_eu.add_passenger(bob)
     flight_eu.add_passenger(alice)
     flight_eu.add_passenger(henry)
     flight_eu.add_passenger(henry)
     print(flight_eu)
     flight_eu.print_passengers()
     print("There are ", flight_eu.get_passenger_count(), " passengers on this flight")
     flight_eu.remove_passenger(bob)
     flight_eu.print_passengers()


main()     
