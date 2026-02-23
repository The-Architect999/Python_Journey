# def hello():
#     return 'helooooo'

# greet = hello() #function passes as a variable to another variable
# print(greet)
# del hello # built in function that deletes the function
# print(greet) #returns the variable even when the func is deleted

# #calling the function inside another function:
# def hello (func):
#     func()

# def greeting():
#     print('still here')

# a = hello(greeting)
# print(a)

# #HOC
# def greet1(func):
#     func()
# #or
# def greet2():
#     def func():
#         return 5
#     return func

# #FINALLY DECORATORS!!!
# #Decorator Pattern  - 4 parametres
# def my_decorator(func): #function wrapped over another function
#     def wrap_func(*args, **kwargs): #another function
#         func(*args, **kwargs) #calls the function
#     return wrap_func #returns the function

# @my_decorator
# def hello(a, b):
#     print(a, b)

# hello('p', ':>')
# #function speed checker
# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     for i in range(100000000):
#         i*5

# long_time()

# #exercise
# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': False #changing this will either run or not run the message_friends function.
# }
# def authenticated(fn):
#     def wrap(*args, **kwargs):
#         if args[0]['valid'] == True: #args pack all positional arguments as a tuple
#             fn(*args, **kwargs)
#         else:
#             print('invalid user')
#     return wrap

# @authenticated
# def message_friends(user: dict):
#     print('message has been sent')
# message_friends(user1)


#exercises
# Apply your decorator to this:
def audit_log (fn):
    def wrap(*args, **kwargs):
        print('--- AUDIT START: Intercepting transaction ---')
        result = fn(*args, **kwargs)
        print('--- AUDIT COMPLETE: Transaction secured ---')
        return result
    return wrap

@audit_log
def transfer_funds(amount):
    print(f"Processing transfer of ${amount}...")

transfer_funds(500)

#Exercise 2: The Surplus Modifier (Altering the Output)
def caloric_surplus(fn):
    def wrap(*args, **kwargs):
        kcal = fn(*args, **kwargs)
        return kcal * 1.15
    return wrap

@caloric_surplus
def calculate_maintenance(weight_kg):
    return weight_kg * 33

print(calculate_maintenance(60))

# Exercise 3: The Fraud Firewall (Argument Inspection)
def fraud_check (fn):
    def wrap (*args, **kwargs):
        if args[0]['status'] == 'Flagged':
            return "ALERT: Transaction blocked. Security team notified."
        else:
            return fn(*args, **kwargs)
    return wrap
        
@fraud_check
def approve_loan(user_data, amount):
    return f"SUCCESS: Loan of ₹{amount} approved for {user_data['name']}."
user_clean = {'name': 'Arthur', 'status': 'Active'}
user_suspect = {'name': 'Dutch', 'status': 'Flagged'}

# This should print the SUCCESS message
print(approve_loan(user_clean, 400000))

# This should print the ALERT message, completely blocking the loan
print(approve_loan(user_suspect, 400000))