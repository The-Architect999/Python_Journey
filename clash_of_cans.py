# clash of cans

# recalls everything at one place
class IngameObjects():
    pass

# to use as a call back for every army function and building


class Army(IngameObjects):
    def __init__(troop_capacity):
        pass

# parent class - Troops


class Troops(Army):
    def __init__(self, types, dammage, health):
        self.types = types
        self.dammage = dammage
        self.health = health

    def attack(self, target):
        target -= self.dammage
        return f"{self.name} attacked {target} for {self.damage} damage!"


# children -actual troops to assign attributes and set defaults
class Archers (Troops):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant
        self.level = 1

    def deploy(self, location):
        self.location = tuple(location)
        # to code after learning inputs - GUI
        pass


class Barbarians (Troops):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant

    def deploy(self, location):
        self.location = tuple(location)
        # to code after learning inputs - GUI
        pass


class WallBreakers (Troops):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant

    def deploy(self, location):
        self.location = tuple(location)
        # to code after learning inputs - GUI
        pass

# class of defences:


class Defences:
    def active(self, status):
        self.status = status
        if status == "under construction":
            return f"{self} is currently being upgraded!"

    def upgrade(self, level):
        # i think it will be better if i store the data outside the classes
        # as when i call them, i can use: class(input, stored data)
        # to explore
        pass

    def defend(self, under_attack):
        self.under_attack = under_attack
        if self.active == "under construction":
            return None
        else:
            # need to get range here
            pass


class ArcherTower(Defences):
    def __init__(self, location, types, damage, health):
        # will set location as a tuple for the top left tile to the bottom right tile
        self.location = location
        self.types = types
        self.damage = damage
        self.health = health

    def defend(self):
        # to code
        pass


class Cannon(Defences):
    def __init__(self, location, types, damage, health):
        self.location = location
        self.types = types
        self.damage = damage
        self.health = health

    def defend(self):
        # to code
        pass


class Mortar(Defences):
    def __init__(self, location, types, damage, health):
        self.location = location
        self.types = types
        self.damage = damage
        self.health = health

    def defend(self):
        # to code
        pass


# Class of empire buildings:
class MainBuildings:
    # to code
    pass


class Townhall(MainBuildings):
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def nothing(self):
        # to code or not to code that is the question
        pass


class ClanCastle(MainBuildings):
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def requesttroops(self):
        # to
        pass


class Villagers(IngameObjects):
    # to code random villagers walking around after - GUI
    pass


# to be continued..........
