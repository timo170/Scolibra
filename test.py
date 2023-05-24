from tkinter import *
from PIL import Image,ImageTk
root = Tk() # create a Tk root window

w = 500 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
def start(event):
    print(ws)


img = ImageTk.PhotoImage(Image.open("books.png").resize((200,200),Image.ANTIALIAS))
image=Label(root,image=img).pack()
image.bind('<Button-1>', start)
root.mainloop()