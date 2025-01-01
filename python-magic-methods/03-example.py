class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year='{self.year}')"


# Create an instance of Car
my_car = Car('Toyota', 'Etios', 2021)
print(str(my_car))
print(repr(my_car))