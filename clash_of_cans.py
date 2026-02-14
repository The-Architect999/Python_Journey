# clash of cans

# need to add a few dictionaries that store all the information on levels and stats

# recalls everything at one place
class IngameObjects():
    pass


class Troops(IngameObjects):
    def __init__(self):
        # default counters, to be updated with the library
        self.dammage = 0
        self.health = 0
        self.quant = 0
        self.level = 1

    def deploy(self, location: tuple):
        self.loaction = location
        # to learn more to add here
        # need to check if i should use a __srt__ or just add a name in args
        return f"{self} Deployed!"

    def Train(self, quantity):
        self.quantity = quantity


# children - Troolps to set defaults
class Archers (Troops):
    def __init__(self):
        pass


# only one instance needed
archer = Archers()


class Barbarians (Troops):
    def __init__(self):
        pass


# only one instance needed
barbarian = Barbarians()


class WallBreakers (Troops):
    def __init__(self):
        pass


# only one instance needed
wallbreaker = WallBreakers()


# class of defences:
class Defences(IngameObjects):
    def __init__(self, location):
        self.loaction = location
        self.status = "idle"

    def active(self):
        self.level = 1
        self.status = False
        # not sure if i should set the status to a bool or a str "currently upgrading"
        # to explore

    def upgrade(self):
        if self.status == "upgrading":
            return f"Building already being upgraded!"
        else:
            # to code for cancel upgrade
            # to do the cost and time codint - yet to learn
            self.level += 1
            # time and level check needed
            # also want to add a want to cancel upgrade code
            return f"{self} is now being upgraded to {self.level}"
            # i think ill need to add names in the args as well to get it to print the building name
            # need to check for alternatives to do that as i already have the name as class when i need to call it

    def defend(self, under_attack):
        self.under_attack = under_attack
        if self.active == "under construction":
            return None
        else:
            # need to get range here
            pass

# yet to check what args to pass to parent for defences


class ArcherTower(Defences):
    def __init__(self, location: tuple):
        super().__init__(location)


class Cannon(Defences):
    def __init__(self, location: tuple):
        super().__init__(location)


class Mortar(Defences):
    def __init__(self, location: tuple):
        super().__init__(location)


# Class of empire buildings:
class MainBuildings(IngameObjects):
    def __init__(self):
        self.level = 1
        # to code
        pass


class Townhall(MainBuildings):
    def __init__(self):
        pass

    def nothing(self):
        # to code or not to code that is the question
        pass


class ClanCastle(MainBuildings):
    def __init__(self, level):
        self.level = 1

    def requesttroops(self):
        # to code
        pass


class Villagers(IngameObjects):
    # to code random villagers walking around after - GUI
    pass


# to be continued..........
