# #generators
# print(range(100)) #creates the numbers one by one
# print(list(range(100))) #creates a list in memory
# # for a list operation, this is what python does underneath the hood:
# def make_list (num):
#     result = []
#     for n in range(num):
#         result.append(n*2)
#     return result

# print(make_list(100))

# #example generator function
# #this is how the range generator acts: 
# def generator_function(num):
#     for i in range(num):
#         yield i 
# g = generator_function(1)
# next(g) # 0
# print(next(g)) # 1 - the stop value for the generator
 
# # for item in generator_function(1): 
# #     print(item) 

# using the decorator we made to test the difference
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper
    
# @performance # using the generator
# def long_time():
#     print('1')
#     for i in range(1000000000):
#         i*5

# @performance #using a list of numbers
# def long_time2():
#     print('2')
#     for i in list(range(1000000000)):
#         i*5

# long_time()
# long_time2()

# #underneath the hood of for loops
# def special_for(iterable):
#     iterator = iter(iterable) 
#     #iter function to tell python(iterables only)
#     while True:
#         try:
#             print(iterator) #iter(iterable) returns physical address
#             print(next(iterator)) # returns values in iterable
#         except StopIteration:
#             break

# special_for([1,2,3])

#making a generator
# class MyGen():
#     current = 0
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self): 
#         return self #makes the class an iterable
    
#     def __next__(self): #runs in the for loop as in iterable
#         if MyGen.current < self.stop:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration
    
# gen = MyGen(0,100)
# for i in gen:
#     print(i)

#known exercise
#Fibonacci Numbers

def fib(number):
    start = 0
    start1 = 1
    counter = 0
    while number > counter:
        counter += 1
        v = start
        start += start1
        start1 = v
        yield v
    StopIteration

for i in fib(2):
    print(i)

#EXERCISES
#Exercise 1: The Infinite Transaction ID (Infinite Streams)
def generate_transaction_ids(start):
    while True:
        yield f'TRXN-{start}'
        start += 1

id_stream = generate_transaction_ids(5000)

# A loop simulating 5 new transactions coming into the network
print("--- INCOMING TRANSACTIONS ---")
for _ in range(5):
    # Use the next() function to manually crank the generator once
    new_id = next(id_stream) 
    print(f"Assigned ID: {new_id}")

# Exercise 2: The Suspicious Activity Parser (Data Filtering)
# The massive dataset (Pretend this is 2 million rows long)
daily_batch = [
    {'user': 'Arthur', 'amount': 12000},
    {'user': 'Dutch', 'amount': 85000},
    {'user': 'John', 'amount': 400},
    {'user': 'Micah', 'amount': 150000},
    {'user': 'Sadie', 'amount': 50000} # Exactly 50k should NOT be flagged
]

def flag_high_risk(transaction_data):
    for x in transaction_data:
        if x['amount'] > 50000:
            yield x['user']

# --- TEST CASES ---
print("--- HIGH RISK ALERTS ---")
for suspect in flag_high_risk(daily_batch):
    print(f"ALERT: Investigate account -> {suspect}")

# GOAL OUTPUT: Dutch, Micah

#3 chaining generators
# The Raw Data (Pretend this is a massive 500GB text file)
server_logs = [
    "TXN-001,Arthur,450",
    "TXN-002,Dutch,85000",
    "TXN-003,John,1200",
    "TXN-004,Micah,150000",
    "TXN-005,Sadie,900"
]

# 1. Build the Parser Generator
def parse_logs(log_stream):
    for x in log_stream:
        temp = []
        cache = {}
        temp = x.split(',')
        cache['id'] = temp[0]
        cache['user'] = temp[1]
        cache['amount'] = int(temp[2])
        yield cache

# 2. Build the Filter Generator
def filter_massive_transactions(parsed_stream):
    for x in parsed_stream:
        if x['amount'] > 50000:
            yield x['user']

# --- THE PIPELINE ---
# Watch how we plug the generators into each other like pipes:
parsed_data_stream = parse_logs(server_logs)
fraud_alerts_stream = filter_massive_transactions(parsed_data_stream)

print("--- INITIATING PIPELINE ---")
# The for loop cranks the final pipe, which automatically pulls from the first pipe!
for alert in fraud_alerts_stream:
    print(f"CRITICAL: Freeze account for {alert}")

# GOAL OUTPUT: Dutch, Micah