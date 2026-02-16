# map, filter, zip, reduce
# not formatted just practicing

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

# Lambdas exercises
x = [1,2,3,4,5]
print((reduce(lambda acc, item: acc * item, x)))

my_list = [5,4,3]
#square
print(list(map(lambda x: x * x, my_list)))
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#list sorting - based on the second balue
# a.sort(key = lambda x: x[1])
# print(a)
print(sorted(a, key=lambda x: x[1]))

#comprehensions:
#list comprehensions:
# lis = []
# for x in "hello":
#     lis.append(x)
# print(lis)

# list = [param for param in iterable]
print([char for char in 'hello'])
print([char for char in range(0, 101)])
#return power of 2
print(list(map(lambda x: x ** 2, [char for char in range(0, 101)])))
#or 
print([char ** 2 for char in range(0, 101)])
#exclude odd numbers from the power of 2
print(list(filter(lambda x: x % 2 == 0, [char**2 for char in range(0, 101)])))
#or
print([char ** 2 for char in range(0, 101)if char % 2 == 0 ])

#set and dict comprehensions:
#same as list but with {}
print({char ** 2 for char in range(0, 101)})

#dicts need both key and value

simple_dict = {'a':1, 'b': 2}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
#modifies the given dict
print(my_dict)
# another_dict = {num:num*2 for num in [1,2,3]}
# print(another_dict)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
# This is the "Functional" way to combine them
another_dict = {k: v * 2 for k, v in zip(keys, values)}
print(another_dict)
#another way: nested loops
another_dict = {x: num * 2 for x in ['a', 'b', 'c'] for num in [1, 2, 3]}
print(another_dict)
names = ['Sisi', 'Bibi', 'Titi']
scores = [10, 20, 30]
new_dict = {k:v * 2 for k,v in zip(names, scores)}

#comprehensions exercise:
#find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = {char for char in some_list if some_list.count(char) > 1}
print(duplicates)


#Fnuctional Exercises:
# 1. Map: The "Audit" (Currency Conversion)
# Rate: 1 USD = 83 INR.
prices_usd = [10, 25.5, 100, 2]
prices_inr = (list(map(lambda x: x * 83, prices_usd)))
print(prices_inr)

# 2. Zip: The "Unit Stats" (Clash of Cans)
# You need to pair your troop types with their current health levels for a UI display.
# Task: Combine these two lists into a list of tuples using zip.
troops = ['Archer', 'Cannon', 'Wall_breaker']
health = [80, 150, 200]
troop_health = (list(zip(troops, health)))
print(troop_health)

# 3. Filter: The "Quality Control" (Mushroom Lab)
# You’re auditing your Cordyceps batches. Any batch with a contamination level above 15% must be discarded.
# Task: Use filter and a lambda to keep only the safe batches.

Contamination_levels = [5, 12, 18, 2, 25, 7]
less_than15 = (list(filter(lambda x: x < 15, Contamination_levels)))
print(less_than15)

# 4. Reduce: The "Grand Total" (Transaction Summary)
# You need the final "Settlement" amount for the day.
# Task: Use reduce to sum up all transaction values into a single number.
# from functools import reduce (done earlier)
daily_ledger = [1500, -200, 3000, -150, 450]
daily_total = reduce(lambda acc, x: acc + x, daily_ledger, 0)
print(daily_total)


