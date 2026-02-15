# map, filter, zip, reduce

from functools import reduce

# 1 map
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(str.capitalize, my_pets)))
# use str.capitalize - to call the function from the given class (string)

# 2 Zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, sorted(my_numbers))))
# sorted() for in memory[Temporary] and .sort for in place [Permanent]

# 3 Filter
scores = [73, 20, 65, 19, 76, 100, 88]


def passing_marks(item):
    return item > 50


print(list(filter(passing_marks, scores)))

# Reduce
all_data = my_numbers + scores


def accumulator(accumulate, item):
    return accumulate + item


print((reduce(accumulator, all_data, 0)))


# boss fight: one liner
numbers = [1, 2, 3, 4, 5, 6]


def if_odd(num):
    return num % 2 == 0


def squares(n):
    return n * n


print(list(map(squares, (filter(if_odd, numbers)))))
