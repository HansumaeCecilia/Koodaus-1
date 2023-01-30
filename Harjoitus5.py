class Car:
    def __init__(self, make, model, year, registration, color):
        self.make = make
        self.model = model
        self.year = year
        self.registration = registration
        self.color = color

    def __str__(self):
        
    #teksti = self.make + " " + self.model + " (" + str(self.year) + ") " + self. registration + " " + self.color + " "
        teksti = f"Auton tiedot: {self.make} {self.model} {self.year} {self.registration} {self.color}" #f-string yksinkertaistaa ylläolevan komennon
        return teksti

car1 = Car("Mercedes Benz,", "CLA,", 2015,"ABC-123,", "black")
car2 = Car("Audi", "A6,", 2004, "BCD-234,", "blue")
car3 = Car("Opel", "Corsa,", 2010, "CDE-345,", "red")

print(car1)
print(car2)
print(car3)