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

#more exercises:
# 1. Map: The "Clean-up"
# In your mushroom business, batches are logged with extra spaces or inconsistent casing.
# Task: Clean up this list of mushroom names. Capitalize them and remove the extra spaces.
raw_labels = ["  cordyceps", "lion's mane  ", "  oyster  ", "reishi"]
print(list(map(lambda x: x.strip().capitalize(), raw_labels)))

# 2. Zip: The "Inventory Alert"
# You have names of supplies and their current stock levels. You need to identify what needs reordering.
# Task: Zip these two lists, then convert the result into a dictionary.
supplies = ['Agar', 'Alcohol', 'Petri Dishes', 'Substrate']
stock = [5, 2, 0, 12]
dict_of_suppliers = (dict(zip(supplies, stock)))
print(dict_of_suppliers)

# 3. Filter: The "Security Audit"
# As a fraud specialist, you need to flag transactions that look suspicious. We’ll define "suspicious" as any transaction over ₹10,000.
# Task: Filter the list to show only the normal (safe) transactions.
transactions = [1200, 45000, 900, 15000, 7500, 3200]
print(list(filter(lambda x: x <= 10000, transactions)))

# 4. Reduce: The "Word Smith"
# Let's step away from numbers. Remember that reduce can combine anything.
# Task: Take a list of characters and combine them into a single string, but add a hyphen between each letter.
chars1 = ['L', 'A', 'M', 'B', 'D', 'A']
print(reduce(lambda x, y: x + "-" + y, chars1))

# 2 and 3 combined:
sup = ['Agar', 'Alcohol', 'Petri Dishes', 'Substrate']
stoc = [5, 2, 0, 12]
# print(dict(zip(sup, stoc)))
no_stock = dict(filter(lambda x : x[1] == 0, (list(zip(sup, stoc)))))
print(no_stock)

# basics exercises:
# Task: Add the new_ids to active_batches so that you end up with one flat list of 6 items.
active_batches = [101, 102, 103]
new_ids = [104, 105, 106]
active_batches.extend(new_ids)
print(active_batches)
# Goal: [101, 102, 103, 104, 105, 106]

# Task: Try to retrieve the value for the key 'theme' from the dictionary.
config = {'sound': True, 'difficulty': 'Hard'}
print(config.get('theme', 'dark mode'))

# List: The "Task Manager" (.pop)
# You are processing a stack of tasks. You need to remove the last task from the list and assign it to a variable so you can "work" on it.
# Task: Remove the last item and store it in a variable called current_task.
tasks = ['Email', 'Meeting', 'Code']
tasks.pop()
current_task = tasks.copy()
print(current_task)
# Goal: tasks should be ['Email', 'Meeting'] and current_task should be 'Code'

# You have a default profile for a new user. The user then customizes their profile with specific settings.
# Task: Update the default_profile with the user_settings. The user's specific choices should overwrite the defaults, but keep the other defaults intact.

profile = {'notifications': True, 'theme': 'Light', 'role': 'User'}
updates = {'theme': 'Dark', 'notifications': False}
profile.update(updates)
print(profile)

# The "Methods" Boss Fight (Sets) ⚔️
# Scenario: You sent 5 scouts to find mushroom locations. Only 3 returned. You need to identify exactly who is missing so you can send a rescue party.

scouts = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
survivors = ['Alpha', 'Charlie', 'Echo']
missing = (set(scouts)).difference(set(survivors))
print(missing)

#back to functional exercises:
# Your sensors report temperature in Celsius, but your American business partner needs it in Fahrenheit.
# Formula: (C times 9/5) + 32
celsius_readings = [0, 20, 37, 100]
fahrenheit_readings = list(map(lambda x: x * 9/5 + 32, celsius_readings))
print(fahrenheit_readings)

# You are auditing a database. Usernames must be at least 5 characters long to be valid.
users = ['admin', 'root', 'superman', 'guest', 'architect']
valid_users = list(filter(lambda x: len(x) >= 5, users))
print(valid_users)
# Goal: A list containing only 'superman' and 'architect' (and maybe 'admin'? Count carefully!).
# trick question huh

# Zip: The "Price Tag" (Marketplace)
# You have a list of items and a corresponding list of prices.
items = ['Mushroom Kit', 'Scalpel', 'Alcohol']
prices = [2500, 500, 150]
combined_dict = dict(zip(items, prices))
print(combined_dict)
# Task: Create a Dictionary where items are keys and prices are values.

# You need to calculate the total number of combinations for a lock, 
# which is determined by multiplying a sequence of numbers.
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x,y : x * y, numbers))

#more exercise before decorators
#1. The Alias (Functions as Variables)
harvests = [15.5, 20.1, 12.0]
calculate_total_yield = sum
print(calculate_total_yield(harvests))

#2. The Strategy (Passing Functions as Arguments)
def melee(power): return power - 5   # Armor absorbs 5
def magic(power): return power       # Magic ignores armor
def execute_strike(attack_style, power):
    return attack_style(power)
print(execute_strike(melee, 20))

#3. The Factory (Returning Functions)
def create_limit(threshold):
    return lambda x: x >= threshold
flag_10k = create_limit(10000)
print(flag_10k(15000)) # Should print True

# The Missing Boss Fight: Exercise 4
def read_temp():
    return 24.5
def add_logging(func):
    print("--- Activating Sensor ---")
    # YOUR CODE HERE: 
    variable = []
    variable.append(func())
    print("--- Deactivating Sensor ---")
    return variable
print(add_logging(read_temp))




