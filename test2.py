from tkinter import *
import mysql.connector
from tkinter import ttk
#conectare la baza de date
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="BIBLIOTECA"
)
cursor=mydb.cursor()

window=Tk()
window.resizable(1,1)
window.iconbitmap('lista_carti.ico')
window.title('Listă cărți')
window.geometry('1500x1000') 
    
window.configure(background="#c7d3d4")
window.resizable(0,0)

w = 2000 
h = 1000

ws = window.winfo_screenwidth() 
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

#funcția care generează un cod QR pentru cartea selectată
def generareQR():
    try:
        id_cod=tree.focus()
        id_carte=tree.parent(id_cod)
        carte=tree.item(id_carte)
        cod=tree.item(id_cod)["values"][6]
        titlu=carte["values"][1]
        autor=carte["values"][0]
        editura=carte["values"][2]
        an=carte["values"][3]
        pret=carte["values"][4]
        carte=str(cod)+'/'+str(autor)+'/'+str(titlu)+'/'+str(editura)+'/'+str(an)+'/'+str(pret)+'/'+'Biblioteca LNI'
        carte=str(carte)
        nume=""
        nume='qr_'+str(cod)
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(carte.encode('utf-8'))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{nume}.png") 
        showinfo(title="Info",message="Fișierul a fost salvat.")
    except:
        showerror(title="Eroare",message="Selectați codul unei cărți, nu un titlu comun.")

#campurile ferestrei
frame3=Frame(window)
frame3.pack(side=TOP)

label=Label(frame3,width=20,height=1,text="Caută după:",font=("Helvetica",21),bg="#c7d3d4",fg="black",anchor=E)
label.pack(side=LEFT)

genqr=Button(frame3,width=20,text="Generează cod QR",command=generareQR,font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru generare QR
genqr.pack(side=RIGHT)

sterge=Button(frame3,width=15,text="Șterge carte",font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru ștergere carte
sterge.pack(side=RIGHT)

adauga=Button(frame3,width=15,text="Adaugă carte",font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru inserare carte
adauga.pack(side=RIGHT)


filtru=ttk.Combobox(frame3,height=30,font=("Helvetica",16))  #filtru (caută după)
filtru.pack(padx=5,side=RIGHT)


valori=["Cod","Autor","Titlu","Editura","Anul_aparitiei","Pret","Stare","QR"]
filtru['values']=valori      
filtru['state']='readonly'

from tkinter.messagebox import showinfo,showerror
import qrcode

caseta=Entry(window,font=("Helvetica",20),fg="black",width=93)  #bara de căutare
caseta.pack(anchor=CENTER)
    
    
    
global tree
coloane=(1,2,3,4,5,6,7)
tree=ttk.Treeview(window,columns=coloane,height=43,selectmode='browse') #tabelul cu afișări

    
# configurare Scrollbar
scrollbar = Scrollbar(window,orient='vertical',command=tree.yview,width=20)
scrollbar.pack(side=RIGHT,fill='y')
tree.pack(side=TOP,padx=30,anchor=N)
    
tree['yscrollcommand'] = scrollbar.set
    
    
   
tree.heading("#0",text='')
tree.heading(1,text='AUTOR')
tree.heading(2,text='TITLU')
tree.heading(3,text='EDITURA')
tree.heading(4,text='ANUL_APARIȚIEI')
tree.heading(5,text='PREȚ')
tree.heading(6,text='NR BUCĂȚI')
tree.heading(7,text='COD CĂRȚI LIBERE')

tree.column('#0',minwidth=20,width=20)
    
#inserare în tabel din baza de date

com="Drop table carti2;"

cursor.execute(com)
mydb.commit()
com="create table carti2 (SELECT COUNT(Cod),Autor,Titlu,Editura,Anul_aparitiei,Pret FROM carti GROUP BY Titlu,Autor,Editura,Anul_aparitiei,Pret);" 
cursor.execute(com)
mydb.commit()
com="Select * from carti2;"
cursor.execute(com)

result=cursor.fetchall()


coduri=[]
date=[]
for x in result:
    list1=(x[1], x[2],x[3],x[4],x[5],x[0])
    date.append(list1)


for rand in date:

    carte=tree.insert('',END,text="",values=rand)
    
    com="Select Cod from carti where Autor=%s and Titlu=%s and Editura=%s and Anul_aparitiei=%s and Stare='liberă';"
    val=[rand[0],rand[1],rand[2],rand[3]]
    cursor.execute(com,val)
    result=cursor.fetchall()
    for cod in result:
        tree.insert(carte,END,values=("","","","","","",cod))

def selected(event):
    idd=tree.focus()
    ite=tree.item(tree.focus())
    print(ite)
    print(idd)
    copii=tree.get_children(idd)
    idd=tree.focus()
    parinte=tree.parent(idd)
    item=tree.item(parinte)
    print(copii)
    print(parinte)
    print(item)

tree.bind('<Double-1>',selected)
    



    

   
window.mainloop()