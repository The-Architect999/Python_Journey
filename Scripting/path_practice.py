from pathlib import Path

current_location = Path.cwd() #returns current directory on disk
print(f"Absolute Path: {current_location}")
# name is an attribute of the object:
print(f"Folder Name: {current_location.name}")
# / inside the directory, automaticalls converts to C:\\Users\\..
fake_file = current_location / "ghost_file.txt"
print(f"Does ghost_file exist? {fake_file.exists()}") #returns bool


sandbox = current_location / "lab_sector_7"
sandbox.mkdir(exist_ok=True) # creates a new directory
print(f"Directory spawned: {sandbox.exists()}") #confirms new dir made
# If I run sandbox.mkdir() and the lab_sector_7 folder already exists:
# Python will instantly throw a FileExistsError
# By adding exist_ok=True - tells python - if it exists, move on
# parents=True gives Python the authority to build the 
# entire chain of folders from scratch.(x/y/paste_here)

# THE new text file inside that folder
data_file = sandbox / "secure_log.txt"

# 3. THE INJECTION: Write data directly into the file
data_file.write_text("I never existed HAHA! - the devil!.") #write
print(f"File created and injected: {data_file.exists()}") #check

# Read the data right back out to the terminal
extracted_data = data_file.read_text() #assign variable to data
print(f"Extracted payload says: '{extracted_data}'") #print data

# 5. THE CLEANUP: delete the file, then delete the folder
# in python you cant delete folders that include a file,
# so we delete the file/files first
data_file.unlink()  # .unlink() is the command to delete a file
sandbox.rmdir()     # .rmdir() is the command to delete an EMPTY directory

#confirming the file is deleted
print(f"Evidence destroyed. Sandbox exists? {sandbox.exists()}")