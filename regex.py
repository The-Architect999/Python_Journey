import re
# pattern = re.compile('jerk|is')
# string = 'is this search inside of is this string'
# a = pattern.search(string) #search in the string
# b = pattern.findall(string)
# print(a)
# print(b)

# regex = re.compile(r"you|how")

# test_str = "how are you today"

# matches = regex.finditer(test_str)

# for match_num, match in enumerate(matches, start=1):
#     print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")
    
#     for group_num, group in enumerate(match.groups(), start=1):
#         print(f"Group {group_num} found at {match.start(group_num)}-{match.end(group_num)}: {group}")

# email validator:
# regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

#password validation exercise:
# can include: letters, numbers, $%#@
password_allowed = re.compile(r'^[a-zA-Z0-9$%#@]{8,}\d$')

while True:
    password = input('type your password')
    valid_password = password_allowed.match(password)
    if valid_password:
        print("success!")
        break
    else:
        print('try again, must include: can include: letters, numbers, $%#@')