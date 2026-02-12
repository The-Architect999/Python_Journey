class Vehicle:
    def __init__(self, brand, milage_level):
        self.brand = brand
        self.fuel_level = 120
        self.milage_level = milage_level

    def drive(self):
        self.fuel_level -= self.milage_level
        return "vroom!"

    def drives_left(self):
        self.drives = self.fuel_level / self.milage_level
        return f"{self.drives:.0f} drives left"


class ElectricVehicle(Vehicle):
    def __init__(self, brand, milage_level):
        super().__init__(brand, milage_level)
        self.milage = self.milage / 2


car1 = Vehicle("Tata", 10)
car2 = Vehicle("Mahindra", 12)
ev1 = ElectricVehicle("Tesla", 10)


print(car1.drive())
print(car1.fuel_level)
print(car1.drives_left())
print(car2.fuel_level)
print(ev1.drive())
print(ev1.fuel_level)
