from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror
import pywhatkit as kit
from datetime import datetime,date,timedelta


window= Tk()
window.geometry('1000x1000')
def mesaj():
    now = datetime.now()
    minut = int(now.strftime("%M"))+1
    ora = now.strftime("%H")
    numere = ["+40738231065","+40756528688"]
    for i in range(2):
        try:
            kit.sendwhatmsg(numere[i],"NU O DAI CU PGM",int(ora),int(minut),wait_time=14,tab_close=True,close_time=2)
            print(minut)
            minut=int(minut)+1
            print (minut)

        except:
            print("Teapa ca nu mere")
           
msj_elev=Button(window,text="Notifică elevii",bg="#547F5D",fg="white",font=("Helvetica",20),command=mesaj)
msj_elev.pack()
        