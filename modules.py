import security_utils #can use everything from teh file
# Inside main_system.py
import security_utils
print("--- RUNNING EXTERNAL SYSTEM ---")
# Reaching into the utility belt:
final_balance = security_utils.process_withdrawal(500, 2000)
print(f"Transaction successful. Vault balance: {final_balance}")

from security_utils import *

print(__name__)

if __name__ == '__main__':
    #do this
    pass

import random
print(random.random())
print(random.randint(1,200))
print(random.choice([1,2,3,4,5]))
