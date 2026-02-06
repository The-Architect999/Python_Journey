# clash of cans
class Cans:
    def __init__(self, types, dammage, attack):
        self.types = types
        self.dammage = dammage
        self.attack = attack

# class of troops


class Archers (Cans):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant

    def deploy(self, location):
        self.location = tuple(location)
        # to code
        pass


class Barbarians (Cans):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant

    def deploy(self, location):
        self.location = tuple(location)
        # to code
        pass


class WallBreakers (Cans):
    def __init__(self, location, quant):
        self.location = location
        self.quant = quant

    def deploy(self, location):
        self.location = tuple(location)
        # to code
        pass

# class of defences:


class Defences:
    def active(self, status):
        self.status = status
        if status == "under construction":
            return f"{self} is currently being upgraded!"


class ArcherTower(Defences):
    def __init__(self, location, types, damage, health):
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

# to be continued..........
