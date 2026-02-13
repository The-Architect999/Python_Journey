class Vehicle:
    def __init__(self, brand, milage_level):
        self.brand = brand
        self._fuel_level = 120
        self.milage_level = milage_level

    def drive(self):
        self._fuel_level -= self.milage_level
        return "vroom!"

    def drives_left(self):
        self.drives = self._fuel_level / self.milage_level
        return f"{self.drives:.0f} drives left"

    def refuel(self, amount):
        if amount < 0:
            raise ValueError("fuel cannot be negative!")
        else:
            self._fuel_level += amount
            return f"fuel level updated: {self._fuel_level}"


class ElectricVehicle(Vehicle):
    def __init__(self, brand, milage_level):
        super().__init__(brand, milage_level)


car1 = Vehicle("Tata", 10)
car2 = Vehicle("Mahindra", 12)
ev1 = ElectricVehicle("Tesla", 10)

my_garage = [car1, car2, ev1]

for v in my_garage:
    print(f"{v.brand} {v.drive()}")
    print(v.drives_left())

print(car1.refuel(50))

print(car1.refuel(-200))

# print(car1.drive())
# print(car1.fuel_level)
# print(car1.drives_left())
# print(car2.fuel_level)
# print(ev1.drive())
# print(ev1.fuel_level)
