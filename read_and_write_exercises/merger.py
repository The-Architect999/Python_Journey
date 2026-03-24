from pathlib import Path
base_folder = Path('lab_data')
master_file = base_folder / 'master_incubation_report.txt'
with open (master_file, mode = 'a', encoding='utf-8') as myfile:
    for files in base_folder.glob('*.txt'):
        content = files.read_text(encoding='utf-8')
        myfile.write(content + '\n')
print("System Alert: Incubation logs successfully merged.")

    