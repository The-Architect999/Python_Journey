messy_names = ["  albert ", " bOB  ", "   cArlOs", "ALICE   ", " bOb "]
temp_list = []
for names in messy_names:
    names = names.strip().capitalize()
    if names not in temp_list:
        temp_list.append(names)
print(temp_list)

    
