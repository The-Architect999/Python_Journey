class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Dora', 2)
cat2 = Cat('snowbell', 3)
cat3 = Cat('azamon', 4)


def get_oldest(c1, c2, c3):

    oldest_cat = c1

    if c2.age > oldest_cat.age:
        oldest_cat = c2

    if c3.age > oldest_cat.age:
        oldest_cat = c3

    return f"The oldest cat is {oldest_cat.name}, {oldest_cat.age} years old"


print(get_oldest(cat1, cat2, cat3))
