from tkinter import *
import random
import mysql.connector
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror
import pyqrcode
import shutil
import os
import qrcode


#conectare la baza de date
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="BIBLIOTECA"
)
cursor=mydb.cursor()

#importare citate din baza de date in variabila citate
sql="Select Citate from CITATE where Numar=%s"
cursor.execute(sql,[random.randrange(0,10)])
citate=cursor.fetchall()    
citate = ','.join(map(str, citate[0]))





criteriu="some"


    
        


#functia care deschide FEREASTRA DE CAUTARE
def search():

    global criteriu
    

    window=Tk()
    window.resizable(1,1)
    window.iconbitmap('lista_carti.ico')
    window.title('Listă cărți')
    window.geometry('1500x1000')


    frame3=Frame(window)
    frame3.pack(side=TOP)

    label=Label(frame3,text="Caută după:",font=("Helvetica",15))
    label.pack(side=LEFT)

    genqr=Button(frame3,width=20,text="Generează cod QR",command=generareQR)
    genqr.pack(side=RIGHT)

    sterge=Button(frame3,width=10,text="Șterge carte",command=stergere)
    sterge.pack(side=RIGHT)

    adauga=Button(frame3,width=10,text="Adaugă carte",command=inserare)
    adauga.pack(side=RIGHT)

    


    

     
    filtru=ttk.Combobox(frame3,width=30,font=("Helvetica",16))
    filtru.pack(padx=5,side=RIGHT)


    valori=["Cod","Autor","Titlu","Editura","Anul_aparitiei","Pret","Stare"]
    filtru['values']=valori      
    filtru['state']='readonly'


    caseta=Entry(window,font=("Helvetica",20),width=100)
    caseta.pack(anchor=NW,padx=5)
    
    
    
    global tree
    coloane=(0,1,2,3,4,5,6)
    tree=ttk.Treeview(window,columns=coloane,show='headings')
    tree.pack()

    tree.heading(0,text='COD')
    tree.heading(1,text='AUTOR')
    tree.heading(2,text='TITLU')
    tree.heading(3,text='EDITURA')
    tree.heading(4,text='ANUL_APARITIEI')
    tree.heading(5,text='PRET')
    tree.heading(6,text='STARE')


    q="Select * from carti"
    cursor.execute(q)
    result=cursor.fetchall()
    date=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],
              x[5],
              x[6])
        date.append(list1)
    
    for rand in date:
        tree.insert('',END,values=rand)
    
    

    
    
    
    
    def schimbare(event):
        global criteriu
        criteriu=filtru.get()
        
    
    def stergere_elemente_arbore():
        x = tree.get_children()
        for item in x:
            tree.delete(item)

    #functia care face cautarea in baza de date
    def cauta(event):
        cuvant=caseta.get()
        
        
        
        cuv=("%"+cuvant +"%")
        
        test=(criteriu,cuv)
        print(criteriu)

        sql="SELECT * FROM carti WHERE {} LIKE '{}' ;".format(criteriu,cuv)
        cursor.execute(sql,)
        records = cursor.fetchall()
        
        recor=[]
        for x in records:
            list1=(x[0],x[1], x[2],
               x[3],
               x[4],
               x[5],
               x[6])
            recor.append(list1)
        mydb.commit()

        
        
        stergere_elemente_arbore()
        for record in records:
            tree.insert('', 0, values=record)
            


    
    
    caseta.bind( '<Return>',cauta)
    filtru.bind('<<ComboboxSelected>>',schimbare )
   

    

    window.mainloop()

def generareQR():
    ite=tree.item(tree.focus())
    carte=""
    carte=str(ite['values'][0])+'/'+str(ite['values'][1])+'/'+str(ite['values'][2])+'/'+str(ite['values'][3])+'/'+str(ite['values'][4])+'/'+str(ite['values'][5])+'/'+'Biblioteca LNI'
    carte=str(carte)
    nume=""
    nume='qr_'+str(ite['values'][0])
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(carte.encode('utf-8'))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("C://Users/PC/De/'f{nume}'.png") #aici vreau sa modific numele fisierului
    showinfo(title="Info",message="Fișierul qr.png conține codul QR și este pe Desktop.")

    

#functia care sterge o carte din baza de date
def stergere():
    
    ite=tree.item(tree.focus())
    cell=ite['values'][0]
    parametri=(cell,)
    sql="delete from carti where Cod=%s;"
    cursor.execute(sql,parametri)
    cell=str(cell)
    showinfo("info","Ati sters cartea cu codul "+cell )
    mydb.commit()

#functia de inserare in tabelul cartilor

def inserare():
    geam=Tk()
    geam.resizable(1,1)
    geam.geometry('800x600')
    geam.title("Adaugare")
    






    # fereastra adaugare carti 1234
    
    
    canvas=Canvas(geam,width=1920,height=1080)
    canvas.pack(expand=True,fill=BOTH)
    canvas.columnconfigure(0,weight=1)
    canvas.columnconfigure(1,weight=3)

    #functia de preluare a informatiilor despre o carte
    def preluare():
        Cod_entry.focus()
        def log(event):
            global cod
            cod=Cod_entry.get()
            Autor_entry.focus()
            def log1(event):
                global autor
                autor=Autor_entry.get()
                Titlu_entry.focus()
                def log2(event):
                    global titlu
                    titlu=Titlu_entry.get()
                    Editura_entry.focus()
                    def log3(event):
                        global editura
                        editura=Editura_entry.get()
                        An_entry.focus()
                        def log4(event):
                            global an
                            an=An_entry.get()
                            Pret_entry.focus()
                            def log5(event):
                                global pret
                                pret=Pret_entry.get()
                                        
                                

                            Pret_entry.bind('<Return>',log5)

                        An_entry.bind('<Return>',log4)

                    Editura_entry.bind('<Return>',log3)

                Titlu_entry.bind('<Return>',log2)

            Autor_entry.bind('<Return>',log1)
        
        Cod_entry.bind('<Return>',log)

    #functia de introducere si salvare a unei carti in baza de date
    def salvare():
        sql="INSERT INTO carti(Cod,Autor,Titlu,Editura,Anul_aparitiei,Pret,Stare) VALUES(%s,%s,%s,%s,%s,%s,'libera');"
        values=(Cod_entry.get(), Autor_entry.get(), Titlu_entry.get(), Editura_entry.get(), An_entry.get(), Pret_entry.get() )
        try:
    # afisarea erorii
            cursor.execute(sql,values)
            mydb.commit()
        except Exception:
            messagebox.showerror(title="Eroare",message = "Codul introdus este deja inregistrat in baza de date")
        
        '''Cod_entry.delete(0,END) 
        Autor_entry.delete(0,END)
        Titlu_entry.delete(0,END)
        Editura_entry.delete(0,END)
        An_entry.delete(0,END)
        Pret_entry.delete(0,END)'''
        Cod_entry.focus()



                                    

    #campurile ferestrei
    Cod=Label(canvas,text="Cod:")
    Cod.grid(column=0,row=0,sticky=EW)

    Cod_entry=Entry(canvas,)
    Cod_entry.grid(column=1,row=0,sticky=W)

    Autor=Label(canvas,text="Autor:")
    Autor.grid(column=0,row=1,sticky=EW)

    Autor_entry=Entry(canvas,)
    Autor_entry.grid(column=1,row=1,sticky=W)

    Titlu=Label(canvas,text="Titlu:")
    Titlu.grid(column=0,row=2,sticky=EW)

    Titlu_entry=Entry(canvas,)
    Titlu_entry.grid(column=1,row=2,sticky=W)

    Editura=Label(canvas,text="Editura:")
    Editura.grid(column=0,row=3,sticky=EW)

    Editura_entry=Entry(canvas,)
    Editura_entry.grid(column=1,row=3,sticky=W)

    An=Label(canvas,text="An:")
    An.grid(column=0,row=4,sticky=EW)

    An_entry=Entry(canvas,)
    An_entry.grid(column=1,row=4,sticky=W)

    Pret=Label(canvas,text="Pret:")
    Pret.grid(column=0,row=5,sticky=EW)

    Pret_entry=Entry(canvas,)
    Pret_entry.grid(column=1,row=5,sticky=W)

    salvare_btn=Button(canvas,text='Salvare',bg='red',fg='white',command=salvare)
    salvare_btn.grid(column=1,row=6,sticky=W)

    preluare()



    geam.mainloop()



#functia care deschide FEREASTRA IMPRUMUTURI
def imprumut():

    def stergere_elemente_tabel():
        x = tabel.get_children()
        for item in x:
            tabel.delete(item)

    #functia care sterge un imprumut adus la timp
    def returnata():
        ite=tabel.item(tabel.focus())
        cell=ite['values'][0]
        cod_carte=int(ite["values"][4])
        sql1="update carti set Stare='liberă' where Cod=%s;"
        para=(cod_carte,)
        cursor.execute(sql1,para)
        cell=str(cell)
        parametri=(cell,)
        sql="delete from imprumuturi where COD_IMPRUMUT=%s;"
        cursor.execute(sql,parametri)
        
        showinfo("info","Cartea a fost restituita.")
        window.destroy()
        mydb.commit()
        
        

    window=Tk()
    window.geometry("1500x600")
    root.resizable(0,0)
    window.iconbitmap('carti_i.ico')
    window.title('Cărți împrumutate')
   
    coloane=[0,1,2,3,4,5,6]
    tabel=ttk.Treeview(window,columns=coloane,show="headings")
    tabel.pack()

    adus=Button(window,text="Returnata",bg="green",fg="white",font=("Helvetica",12),command=returnata)
    adus.pack()

    tabel.heading(0,text='COD IMPRUMUT')
    tabel.heading(1,text='COD ABONAT')
    tabel.heading(2,text='NUME')
    tabel.heading(3,text='CLASA')
    tabel.heading(4,text='COD CARTE')
    tabel.heading(5,text='DATA IMPRUMUTULUI')
    tabel.heading(6,text='DATA RETURNARII')

    q="Select * from imprumuturi"
    cursor.execute(q)
    result=cursor.fetchall()

    date=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],
              x[5],x[6],)
        date.append(list1)
    
    stergere_elemente_tabel()
    for rand in date:
        tabel.insert('',END,values=rand)
    
    

    
    
#functia care deschide LISTA DE ELEVI ABONATI
def abonati():
    window=Tk()
    window.geometry("1500x1000")
    window.resizable(0,0)
    window.iconbitmap('lista_elevi.ico')
    window.title('Listă elevi')
    
    window.lift()
    

    coloane=[0,1,2,3,4,5]
    tabel=ttk.Treeview(window,columns=coloane,show="headings")
    tabel.pack()

    tabel.heading(0,text='COD ELEV')
    tabel.heading(1,text='NUME')
    tabel.heading(2,text='PRENUME')
    tabel.heading(3,text='CLASA')
    tabel.heading(4,text='DATA ABONARII')
    

    q="Select * from abonati"
    cursor.execute(q)
    result=cursor.fetchall()

    date=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],)
        date.append(list1)
    for rand in date:
        tabel.insert('',END,values=rand)

    

    def imprumut_nou():
        ite=tabel.item(tabel.focus())
        cod_abonat=ite['values'][0]
        nume=ite['values'][1]
        clasa=ite['values'][3]
        from datetime import date,timedelta
        win=Tk()
        
        Titlu=Label(win,text="Cod carte:")
        Titlu.pack()

        Titlu_entry=Entry(win,)
        Titlu_entry.pack()
        
        

        data_azi=str(date.today())
        data_return=str(date.today() +timedelta(days=14))
        
        
        def save_imprumut():
            cod_carte=int(Titlu_entry.get())
            
            sql2="Select * from carti where Cod=%s and Stare='liberă';"
            test2=(cod_carte,)
            cursor.execute(sql2,test2)
            re=cursor.fetchall()
            if len(re)== 1:
                cod_i=(cod_abonat+cod_carte)/2
                sql="insert into imprumuturi values( %s,%s,%s,%s,%s,%s,%s);"
            
                test=(cod_i,cod_abonat,nume,clasa,cod_carte,data_azi,data_return)
                cursor.execute(sql,test)

                sql1="update carti set Stare='împrumutată'  where Cod=%s;"
                test1=(cod_carte,)
                cursor.execute(sql1,test1)
                showinfo(title="Info",message="Împrumut adăugat.")
                mydb.commit()
                win.destroy()
            else:
                showerror(title='Eroare',message="Cartea este împrumutată!")
        

        


    
    

        salvare_btn=Button(win,text='Salvare',bg='red',fg='white',command=save_imprumut)
        salvare_btn.pack()

        win.mainloop()

    adauga=Button(window,text="Adaugă împrumut",width=10,height=5,command=imprumut_nou)
    adauga.pack()

    window.mainloop()

        


#FEREASTRA PRINCIPALA

root=Tk()

root.geometry('1920x1080')
root.title('Școlibra')
root.iconbitmap('iconbitmap_principal.ico')
root.resizable(0,0)



#imaginea pentru fundalul canvas_principala
photo=Image.open("background.jpg")
photo1=photo.resize((1920,1080))
img=ImageTk.PhotoImage(photo1)

canvas=Canvas(root,width=1920,height=1080)
canvas.pack(expand=True,fill=BOTH)
canvas.create_image(0,0,image=img,anchor=NW)



frame0=Frame(canvas,height=400,width=800,bg="yellow")
frame0.place(relx=0,rely=0,anchor=NW)

welcome=Label(frame0,text=" Biblioteca LNI \n \n \n Bine ați venit!",bg="yellow", font=("Helvetica",40))
welcome.place(relx=0.5,rely=0.5,anchor=CENTER)


frame=Frame(canvas,height=400,width=800,)
frame.place(rely=0,relx=1,anchor=NE)

citat=Label(frame,text=citate,height=400,width=800,font=("Helvetica",14) )               
citat.place(relx=0.5,rely=0.5,anchor=CENTER)


frame1=Frame(canvas,width=850,height=450)
frame1.place(relx=0.5,rely=0.7,anchor=CENTER)

imprumuturi=Button(frame1,text="Cărți împrumutate",width=80,height=6, bg="#F5EBE0",font=("Cambria_Math",15),command=imprumut)
imprumuturi.place(relx=0,rely=0,anchor=NW,)

carti=Button(frame1,text="Listă cărți",width=80,height=6,bg="#F5EBE0",font=("Cambria_Math",15),command=search)
carti.place(relx=0,rely=0.5,anchor=W,)

elevi=Button(frame1,text="Listă elevi",width=80,height=6,bg="#F5EBE0",font=("Cambria_Math",15),command=abonati)
elevi.place(relx=0,rely=1,anchor=SW)



#buton_cautare=Button(frame2,text="Cautare",command=search)
#buton_cautare.pack( ipadx=50, ipady=50)





root.mainloop()