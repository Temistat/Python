class Odometer:
    def __init__(self):
        self.miles = 0
    def __str__(self):
        string = "mileage: {}".format(self.miles)
        return string
    def get_mileage(self):
        return self.miles
    def add_mileage(self,miles):
        self.miles += miles
    def reset_mileage(self):
        self.miles = 0
        
