leet = {
    'a': 4, 'A': 4,
    'e': 3, 'E': 3,
    'o': 0, 'O': 0,
    't': 7, 'T': 7,
    'b': 8, 'B': 8
}
new_string = []
output_string = []
user_word = input("type something:")
for letters in user_word:
    new_string += letters
    
for letter in new_string:
    if letter in leet.keys():
        output_string.append(leet[letter])
    else:
        output_string.append(letter)
final_sentence = "".join(map(str, output_string))
print(final_sentence)
