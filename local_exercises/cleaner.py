from pathlib import Path
base_file = Path('inventory.txt')
given = []
counter = 0
with open(base_file, mode = 'r', encoding='utf-8') as file:
    content = file.readlines()
    for data in content:
        if data.startswith('ERROR'):
            counter += 1
        else:
            given.append(data)

with open('resolved_inventory.txt', mode = 'a', encoding= 'utf-8') as file2:
    for points in given:
        file2.write(points)

print(f'excluded {counter} datapoints')