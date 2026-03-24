#putting it together
#exercise 1,2 and 4

# def fraud_check(fn):
#     def wrap (*args, **kwargs):
#         print ('Initiating Transaction!')
#         try:
#             result = fn(*args, **kwargs)
#             return result            
#         except (FraudAlert, InsufficientFunds) as err:
#             return (f'TRY AGAIN! {err}')
#     return wrap

# def log_transaction(func):
#     def wrapper(*args, **kwargs):
#         print(f"LOG: Accessing secure system for {func.__name__}...")
#         return func(*args, **kwargs)
#     return wrapper


# class FraudAlert(Exception):
#     pass

# class InsufficientFunds(Exception):
#     pass

# class BankVault:
#     def __init__(self, name, initial_balance):
#         self.name = name
#         self.balance = initial_balance

#     @log_transaction
#     @fraud_check
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFunds ('Insufficient Funds!')
#         elif amount < 0:
#             raise FraudAlert ('amount should be Positive!')
#         else:
#             self.balance -= amount
#             return f"Withdrawl for {amount} Sucessful, New Balance: {self.balance}"
    

# my_vault = BankVault("Arthur", 5000)
# print(f"Account for {my_vault.name} opened with ₹{my_vault.balance}")
# print(my_vault.withdraw(50000))
# print(my_vault.withdraw(-5000))
# print(my_vault.withdraw(5000))

# data_feed = ["Chamber1,22", "Chamber2,ERROR", "Chamber3-25", "Chamber4,28"]

# def data_cleaner(datasets):
#     for data in datasets:
#         cache = {}
#         try:
#             temp = data.split(',')
#             cache = {'id': temp[0], 'temp': int(temp[1])}
#             yield cache
#         except (IndexError,ValueError) as err:
#             print(f'{err} for: {data}')
#         finally:
#             print (f'{data}: Done!')


def process_log(func):
    def wrapper(*args, **kwargs):
        print("--- OPENING FILE STREAM ---")
        result = func(*args, **kwargs)
        # Note: A generator doesn't "finish" here, 
        # but the creation of the generator does!
        return result
    return wrapper

# Simulated File Content
raw_file_data = """Chamber1,22
Chamber2,ERROR
Chamber3-25
Chamber4,28"""

@process_log
def file_reader(data):
    # .splitlines() turns the big string into a list of lines
    for line in data.strip().splitlines():
        try:
            temp = line.split(',')
            yield {'id': temp[0], 'temp': int(temp[1])}
        except (IndexError, ValueError) as err:
            print(f'{err} for line: {line}')
        finally:
            print (f'{line}: Done!')
        pass

# --- TEST IT ---
for record in file_reader(raw_file_data):
    print(f"FETCHED: {record}")



