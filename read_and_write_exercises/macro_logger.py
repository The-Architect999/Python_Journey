import sys
import datetime
with open('diet_log.txt' , mode = 'a') as my_file:
    text = my_file.write(f"[{datetime.datetime.now()}] Intake: {sys.argv[2]}g of {sys.argv[1]}\n")