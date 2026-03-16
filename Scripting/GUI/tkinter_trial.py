# import tkinter as tk
# #creates the main window
# root = tk.Tk()
# #sets the Title
# root.title("Prototype!")
# #window size
# root.geometry("500x300")

# label = tk.Label(root, text = "Hello!")
# label.place(x=110, y=50)
# button = tk.Button(root, text= "click me", command = lambda: label.config
#                    (text = "you just took instructions from a shitty GUI!"))
# button.place(x=110, y=100)


# #start the GUI event loop
# root.mainloop()

import tkinter as tk

def change_text():
    label.config(text="Status: Scout1 is active and monitoring Tesla.", fg="green")

root = tk.Tk()
root.title("Scout1: Terminal")
root.geometry("400x200")

# Adding padding (space) so it's not cramped
label = tk.Label(root, text="System Standby...", font=("Arial", 12))
label.pack(pady=20) 

# No lambda needed if the function is simple!
button = tk.Button(root, text="Initialize Scout", command=change_text)
button.pack(pady=10)

root.mainloop()