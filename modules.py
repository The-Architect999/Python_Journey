# import security_utils #can use everything from the file
# # Inside main_system.py
# import security_utils
# print("--- RUNNING EXTERNAL SYSTEM ---")
# # Reaching into the utility belt:
# final_balance = security_utils.process_withdrawal(500, 2000)
# print(f"Transaction successful. Vault balance: {final_balance}")
#
# from security_utils import *
#
# print(__name__)
#
# if __name__ == '__main__':
#     #do this
#     pass
#
# import random
# print(random.random())
# print(random.randint(1,200))
# my_list = [1,2,3,4,5]
# print(random.choice(my_list))
# random.shuffle(my_list)
#
# import pyjokes
# joke = pyjokes.get_joke('en', 'all')
# print(joke)


from collections import Counter, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah'
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})  # default callable
print(Counter(li))
print(Counter(sentence))
print(dictionary['c'])

import datetime

print(datetime.time(4, 30))
print(datetime.date.today())

import pdb


def add(n1, n2):
    pdb.set_trace()
    return n1 + n2

add (4, 5)