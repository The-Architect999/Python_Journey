# Input: "hello world"
# Required Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
the_keys = []
the_values = []
the_dict = {}
password = input("type your password here:")
#mehod 1
for characters in password:
    if characters in the_keys:
        the_values.append(password.count(characters))        
    else:
        the_keys.append(characters)
the_dict.update(zip(the_keys,the_values))
print(the_dict)
# #alternate way to do this:
# for characters in password:
#     if characters in the_dict:
#         the_dict[characters] += 1
#     else:
#         the_dict[characters] = 1
# print(the_dict)


    
    











