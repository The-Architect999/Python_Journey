# ==========================================
# SECURITY UTILITIES & DATA PIPELINE TOOLKIT
# ==========================================

# 1. DECORATOR: The Firewall
class FraudAlert(Exception):
    pass

class InsufficientFunds(Exception):
    pass

def fraud_check(fn):
    def wrap (*args, **kwargs):
        print ('Initiating Transaction!')
        try:
            result = fn(*args, **kwargs)
            return result            
        except (FraudAlert, InsufficientFunds) as err:
            return (f'TRY AGAIN! {err}')
    return wrap

#2 logge_transactions
def log_transaction(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Accessing secure system for {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper


# 2. GENERATOR: The Data Filter
def secure_parse_logs(log_stream):
    for x in log_stream:
        temp = []
        try:
            temp = x.split(',')
            yield {'trxn': temp[0], 'name' : temp[1], 'amount' : int(temp[2])}
        except ValueError:
            print(f"WARNING: Corrupt amount data in log -> {x}")
        except IndexError:
            print(f'WARNING: Malformed log format -> {x}')


# 3. ERROR HANDLING: The Logic Tripwire
def process_withdrawal(amount, balance):
    if amount < 0:
        raise PermissionError ('Fraud: Withdrawing negative amount')
    elif amount > balance:
        raise ValueError (f'Overdraft: Withdrawing {amount} from {balance}')
    else:
        balance -= amount
        return balance


# ==========================================
# EXECUTION & DIAGNOSTICS
# ==========================================
# if __name__ == '__main__':
#     print("--- SYSTEM DIAGNOSTICS BOOTING ---")
    
#     transactions = [
#         (1000, 5000),   
#         (6000, 5000),   
#         (-500, 5000)    
#     ]

#     print("--- INITIATING TRANSFERS ---")
#     for amt, bal in transactions:
#         try:
#             new_bal = process_withdrawal(amt, bal)
#             print(f"SUCCESS: Transfer complete. New balance: {new_bal}")
#         except ValueError as ve:
#             print(f"DECLINED: {ve}")
#         except PermissionError as pe:
#             print(f"SECURITY ALERT: {pe}")

if __name__ == '__main__':
    print("--- SYSTEM DIAGNOSTICS BOOTING ---")
    print("1. Decorator loaded.")
    print("2. Generator pipeline ready.")
    print("3. Error tripwires armed.")
    print("--- ALL SYSTEMS GREEN ---")