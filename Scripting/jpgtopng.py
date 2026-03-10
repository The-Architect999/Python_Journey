import sys
from pathlib import Path
from PIL import Image

first = sys.argv[1]
second = sys.argv[2]
base_folder = Path(first)
output_folder = Path(second)

output_folder.mkdir(parents= True, exist_ok = True)

for file in base_folder.iterdir():
    img = Image.open(file)
    clean_name = file.stem
    destination = output_folder / f"{clean_name}.png"
    img.save(destination, 'png')
    print(f"Successfully converted {clean_name}.png")
    
print("All tasks completed.")