class SuperList(list):
    def __init__(self, given):
        super().__init__(given)

    def __len__(self):
        return 1000
# would need to do this if i didnt use (list) in the parent class
    # def append(self, x):
    #     self.given.append(x)

    # def __repr__(self):
    #     return str(self.given)


superlist = SuperList([1, 2, 3, 4, 5, 6])
print(len(superlist))
superlist.append(7)
print(superlist)
print(issubclass(SuperList, list))
