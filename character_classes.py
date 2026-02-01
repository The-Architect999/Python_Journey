# OOP first class
class character:
    def __init__(self, name, age, architype):
        self.name = name
        self.age = age
        self.architype = architype

    def vocab1(self, statement):
        return (statement)


joy = character("Architect", 25, "calculated")
greeting1 = joy.vocab1("hello")
print(f"{greeting1}, i'm {joy.name}")
greeting2 = joy.vocab1("woof")
dog = character("Doggo", 8, "annoying")
print(f"{greeting2}, i'm {dog.name}")
