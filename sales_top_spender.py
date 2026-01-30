sales_data = [
    {"name": "victus", "purchases": [10.99, 5.50, 20.00]},
    {"name": "jay", "purchases": [5.00, 100.25]},
    {"name": "victus", "purchases": [25.00]},
    {"name": "anna", "purchases": [15.50, 15.50]},
    {"name": "jay", "purchases": [10.00]}
]
total_spent = {}
for sales in sales_data:
    name = sales["name"]
    amount = sum(sales["purchases"])
    if name in total_spent:
        total_spent[name] += amount
    else:
        total_spent[name] = amount
print(total_spent)
vip_name = ''
max_amount = 0
for k,v in total_spent.items():
    if v > max_amount:
        max_amount = v
        vip_name = k
print(f'the highest spender is: {vip_name}')
print(f'the highest spent is: {max_amount}')