messy_names = ["  albert ", " bOB  ", "   cArlOs", "ALICE   ", " bOb "]
temp_list = []
role_dict = {}
for names in messy_names:
    names = names.strip().capitalize()
    if names not in temp_list:
        temp_list.append(names)
for name in temp_list:
    initials = name[0]
    role_dict[initials] = name
print(role_dict)

    
