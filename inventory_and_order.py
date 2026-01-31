inventory = {
    "laptop": {"price": 1200, "stock": 5},
    "mouse": {"price": 25, "stock": 10},
    "monitor": {"price": 300, "stock": 2}
}
customer_order = [
    {"item": "laptop", "quantity": 1},
    {"item": "mouse", "quantity": 12}, # Notice: This is more than we have!
    {"item": "tablet", "quantity": 1}  # Notice: This isn't in our inventory!
]
for sets in customer_order:
    item_name = sets["item"]
    needed_quantity = sets['quantity']
    if item_name in inventory:
        if needed_quantity >= inventory[item_name]["stock"]:
            print(f"sorry, we only have {inventory[item_name]["stock"]} {item_name} left")
        elif inventory[item_name]["stock"] >= needed_quantity:
            inventory[item_name]["stock"] -= needed_quantity
            print(f'''
thank's for your order, 
the total cost of your {item_name} order is: {needed_quantity * inventory[item_name]["price"]}''')
    else:
        print(f'we do not trade in the item you requested')
print(inventory)
              
        
           
