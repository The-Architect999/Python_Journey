# inheritence
class User:
    def sign_in(self):
        return ('logged in')

# using the original class to make sure the sub class
# has acess to sign_in


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacked with the power of {self.power}')


class Archer(User):
    def __init__(self, name, no_of_arrows):
        self.name = name
        self.no_of_arrows = no_of_arrows

    def attack(self):
        print(f'{self.name} attacking with arrows. arrows left: {self.no_of_arrows}')


wizard1 = Wizard("merlin", 50)
archer1 = Archer('jack', 100)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
