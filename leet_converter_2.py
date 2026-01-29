leet = {
    'a': 4,
    'e': 3,
    'o': 0,
    't': 7,
    'b': 8,
}
output = []
mode = input("do you want to convert to leet or from leet[to/from]").lower()
while mode != 'to' and mode != 'from':
         print("Invalid mode!")
         mode = input("do you want to convert to leet or from leet[to/from]").lower()
name = input("type what you want to convert:").lower()
for letters in name:
        if mode == "to":
            if letters in leet.keys():
                output.append(leet[letters])
            else:
                output.append(letters)
        elif mode == "from":
             found = False
             for key,value in leet.items():
                  if str(letters) == str(value):
                       output.append(key)
                       found = True
                       break
             if not found:
                    output.append(letters)
print("".join(map(str, output)))
            
                

