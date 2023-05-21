import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import date,timedelta
import pyqrcode
root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

data_azi=date.today()
data_return=date.today() +timedelta(days=14)
print(type(data_azi))



import qrcode

text = "ță.â.î.ș"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(text.encode('utf-8'))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()


# run the app
root.mainloop()