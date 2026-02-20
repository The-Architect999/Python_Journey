# clash of cans

# need to add a few dictionaries that store all the information on levels and stats

# recalls everything at one place
class IngameObjects():
    pass


class Troops(IngameObjects):
    def __init__(self, name):
        # default counters, to be updated with the library
        self.dammage = 0
        self.health = 0
        self.quantity = 0
        self.level = 1
        self.name = name
        

    def deploy(self, location: tuple):
        self.loaction = location
        # to learn more to add here
        # need to check if i should use a __srt__ or just add a name in args
        return f"{self.name} Deployed!"

    def train(self, quantity):
        self.quantity += quantity

    def training_queue (self, roster : dict, queue : list):
        self.roster = roster #{archer: 1, barbarian: 2} 
        self.queue = queue #[archre, barbarian]
        for recruits in queue:
            recruits.train(roster.get(recruits))


    def __str__(self):
        return self.name


# children - Troolps to set defaults
class Archers (Troops):
    def __init__(self, name):
        super().__init__(name)


# only one instance needed
archer = Archers('archer')


class Barbarians (Troops):
    def __init__(self, name):
        super().__init__(name)


# only one instance needed
barbarian = Barbarians('barbarian')


class WallBreakers (Troops):
    def __init__(self, name):
        super().__init__(name)


# only one instance needed
wallbreaker = WallBreakers('wallbreaker')


# class of defences:
class Defences(IngameObjects):
    def __init__(self, location):
        self.loaction = location
        self.status = "idle"

    def active(self):
        self.level = 1
        self.status = '' #idle/upgrading/destroyed/locked-on

    "recomendation - for calling the name directly, to try"
    # def upgrade(self):
    # # This automatically grabs "ArcherTower" or "Cannon"
    # class_name = self.__class__.__name__
    # return f"{class_name} is now upgrading to {self.level}"

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

    def defend(self, all_enemies : list, enemies_in_range : list):
        all_enemies = all_enemies # have to make a master list for deploy so this list gets updated automatically 
        enemies_in_range = enemies_in_range # have to figure this out based on location and targeting, also haven't learned time math yet
        self. valid_targets = [] # list of valid targets for the defence building
        if self.active == "under construction":
            return None
        else:
            valid_targets += set(all_enemies).intersection(set(enemies_in_range))
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

