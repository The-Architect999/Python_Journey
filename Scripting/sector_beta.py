from pathlib import Path
from time import time

start = time()
base_dir = Path.cwd() / 'sector beta'
base_dir.mkdir(parents=True, exist_ok=True)

files_to_create = ["log1.txt", "log2.txt", "notes.txt", "config.py", "data.csv"]

print('initiating generation!')
for files in files_to_create:
    target_file = base_dir / files
    target_file.write_text(f"automated data for{files}")
    print(f"created: {target_file.name}")

print('filtering and returning text only')
for file in base_dir.iterdir():
    if file.is_file() and file.suffix == ".txt":
        print(f"found text file: {file.name}| contents: {file.read_text()}")


print('deleting evidence!')
for items in base_dir.iterdir():
    items.unlink()
    print(f"deleted: {items.name}")

base_dir.rmdir()

print(f"sector beta exists?: {base_dir.exists()}")
end = time()
print(f"took {end - start} s")








