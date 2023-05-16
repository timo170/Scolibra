import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import date,timedelta

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

data_azi=date.today()
data_return=date.today() +timedelta(days=14)
print(type(data_azi))

# run the app
root.mainloop()