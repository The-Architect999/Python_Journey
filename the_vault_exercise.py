datalibrarybalance = {'a': 20000, 'b': 50000, 'c': 10000}
datalibrarycredit = {'a': 0, 'b': 0, 'c': 50000}


class Accounts:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f'Account: {self.holder_name}, Balance: rs {self.balance:.2f}'


class Savings(Accounts):
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'[{self.holder_name}] Insufficient Funds!')
        else:
            self.balance -= amount


class Business(Accounts):
    def __init__(self, holder_name, balance, credit_limit):
        super().__init__(holder_name, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.credit_limit):
            print(f'[{self.holder_name}] Insufficient Credit Limit!')
        else:
            self.balance -= amount
            # If balance is negative, it shows the utilized credit
            if self.balance < 0:
                print(
                    f'[{self.holder_name}] Using Credit! Available limit: rs {self.credit_limit + self.balance:.2f}')


# Creating instances using your data libraries
account_a = Savings('User A', datalibrarybalance['a'])
account_b = Savings('User B', datalibrarybalance['b'])
account_c = Business('User C', datalibrarybalance['c'], datalibrarycredit['c'])

accounts_list = [account_a, account_b, account_c]

print("--- Processing Withdrawals of rs 10,000 ---")
for acc in accounts_list:
    acc.withdraw(100000)
    print(acc)
    print("-" * 30)
