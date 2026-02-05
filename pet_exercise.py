class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True
    my_cats = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.my_cats.append(self)

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Roger(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Simon('Simon', 4)
cat2 = Sally('Sally', 2)
cat3 = Roger('Roger', 7)

for c in Cat.my_cats:
    print(c.name)

my_pets = Pets(Cat.my_cats)
my_pets.walk()
