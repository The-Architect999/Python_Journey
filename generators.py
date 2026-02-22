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

for i in fib(20):
    print(i)

        

    
    





