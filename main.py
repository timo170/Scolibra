from ctypes.wintypes import tagSIZE
from tkinter import *
import random
import mysql.connector
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror
import qrcode
import cv2
import pywhatkit as kit
from pyzbar.pyzbar import decode 
from datetime import datetime,date,timedelta


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


#Functia care deschide LISTĂ CĂRȚI
def search():

    def schimbare(event):  #funcția care actualizează filtrul
        global criteriu
        criteriu=filtru.get()
        if criteriu=="QR":
            cauta_QR()
        
    
    def stergere_elemente_arbore():  #funcția care șterge toate rândurile din tabel
        x = tree.get_children()
        for item in x:
            tree.delete(item)

    
    def cauta(event):      #functia care face cautarea in baza de date în funcție de bara de căutare
        cuvant=caseta.get()

        cuv=("%"+cuvant +"%")
        sql="SELECT * FROM carti2 WHERE {} LIKE '{}' ;".format(criteriu,cuv)
        cursor.execute(sql,)
        records = cursor.fetchall()
    
        date=[]
        for x in records:
            list1=(x[1], x[2],
               x[3],
               x[4],
               x[5],
               x[0])
            date.append(list1)
        mydb.commit()

        stergere_elemente_arbore()
        for rand in date:

            carte=tree.insert('',END,text="",values=rand)
    
            com="Select Cod from carti where Autor=%s and Titlu=%s and Editura=%s and Anul_aparitiei=%s and Stare='liberă';"
            val=[rand[0],rand[1],rand[2],rand[3]]
            cursor.execute(com,val)
            result=cursor.fetchall()
            for cod in result:
                tree.insert(carte,END,values=("","","","","","",cod))
            

        
    def cauta_QR():    #funcția care face căutarea în funcție de codul stocat în codul QR
        var=""
        def reader_cam_qr(): #funcția care scanează codul QR prin intermediul camerei web
            cam =cv2.VideoCapture(0)
            cam.set(5, 640)
            cam.set(6, 480)

            camera = True
            while camera == True:
                suceess, frame= cam.read()
                for i in decode(frame):
                    return i.data.decode('utf-8')
        
            
        var=reader_cam_qr()
        Cod=int(var.split('/')[0])
        

        sql="SELECT * FROM carti WHERE Cod={} ;".format(Cod)
        cursor.execute(sql,)
        records = cursor.fetchall()
        
        date=[]
        for x in records:
            list1=(x[1], x[2],
               x[3],
               x[4],
               x[5],"",
               x[0])
            date.append(list1)
        mydb.commit()

        stergere_elemente_arbore()
        for rand in date:
            tree.insert("",END,values=rand)

    global criteriu
    
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
        window.lift()
    
    #inserare în tabel din baza de date
    # aici trebuie sa apara o functie

    
    





    window=Tk()
    window.resizable(1,1)
    window.iconbitmap('lista_carti.ico')
    window.title('Listă cărți')
    window.geometry('1500x1000') 
    
    window.configure(background="#c7d3d4")
    window.resizable(0,0)

    w = 1500 
    h = 1000

    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))



    #campurile ferestrei
    frame3=Frame(window)
    frame3.pack(side=TOP)

    label=Label(frame3,width=20,height=1,text="Caută după:",font=("Helvetica",21),bg="#c7d3d4",fg="black",anchor=E)
    label.pack(side=LEFT)

    genqr=Button(frame3,width=20,text="Generează cod QR",command=generareQR,font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru generare QR
    genqr.pack(side=RIGHT)

    sterge=Button(frame3,width=15,text="Șterge carte",command=stergere,font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru ștergere carte
    sterge.pack(side=RIGHT)

    adauga=Button(frame3,width=15,text="Adaugă carte",command=inserare,font=("Helvetica",14),bg="#A085C2",fg="black") #buton pentru inserare carte
    adauga.pack(side=RIGHT)


    filtru=ttk.Combobox(frame3,height=30,font=("Helvetica",16))  #filtru (caută după)
    filtru.pack(padx=5,side=RIGHT)


    valori=["Cod","Autor","Titlu","Editura","Anul_aparitiei","Pret","Stare","QR"]
    filtru['values']=valori      
    filtru['state']='readonly'


    caseta=Entry(window,font=("Helvetica",20),fg="black",width=93)  #bara de căutare
    caseta.pack(anchor=CENTER)
    
    
    
    global tree
    coloane=(1,2,3,4,5,6,7)
    tree=ttk.Treeview(window,columns=coloane,height=43) #tabelul cu afișări
    
    
    # configurare Scrollbar
    scrollbar = Scrollbar(window,orient='vertical',command=tree.yview,width=20)
    scrollbar.pack(side=RIGHT,fill='y')
    tree.pack(side=TOP,padx=30,anchor=N)
    
    tree['yscrollcommand'] = scrollbar.set
    
    
   
    tree.heading("#0",text='ID')
    tree.heading(1,text='AUTOR')
    tree.heading(2,text='TITLU')
    tree.heading(3,text='EDITURA')
    tree.heading(4,text='ANUL_APARIȚIEI')
    tree.heading(5,text='PREȚ')
    tree.heading(6,text='NR BUCĂȚI')
    tree.heading(7,text='COD CĂRȚI LIBERE')

    tree.column('#0',minwidth=40,width=40,anchor=CENTER)
    

    q="Select * from cartile;"
    cursor.execute(q)
    result=cursor.fetchall()
   
    date=[]
    for rand in result:
        list1=[rand[0],rand[1],rand[2],rand[3],rand[4],rand[5]]
        date.append(list1)

    for rand in date:
        id=int(rand[0])
        par=[id,]
        q="SELECT COUNT(Id) FROM carticod Where Id=%s;"
        cursor.execute(q,par)
        nr=cursor.fetchall()
        nr=nr[0]

        ID=tree.insert("",END,text=id,values=[rand[1],rand[2],rand[3],rand[4],rand[5],nr])
        q="Select Cod from carticod where Id=%s and Stare='liberă';"
        
        cursor.execute(q,par)
        result=cursor.fetchall()
        for cod in result:
            tree.insert(ID,END,values=["","","","","","",cod])

    
    
    caseta.bind( '<Return>',cauta)
    filtru.bind('<<ComboboxSelected>>',schimbare )
   
    window.mainloop()

    

    

#functia care sterge o carte din baza de date
def stergere():
    try:
        id_cod=tree.focus()
        cod=tree.item(id_cod)
        cod=cod["values"][6]
        parametri=(cod,)
        print(cod)
        sql="delete from carticod where Cod=%s;"
        cursor.execute(sql,parametri)
        cod=str(cod)
        showinfo("Info","Ați șters cartea cu codul "+cod )
        mydb.commit()
    except:
        showerror('Eroare',"Selectați un cod, nu un titlu general.")


#functia care inserează o carte in tabelul cartilor
def inserare():
    geam=Tk()   # fereastra adaugare carti
  
    geam.configure(background="#c7d3d4")
    geam.resizable(0,0)
    geam.title("Adaugă carte")

    w = 300 
    h = 200

    ws = geam.winfo_screenwidth() 
    hs = geam.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    geam.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
    
    canvas=Canvas(geam,width=1920,height=1080,background="#c7d3d4")
    canvas.pack(expand=True,fill=BOTH)
    canvas.columnconfigure(0,weight=1)
    canvas.columnconfigure(1,weight=3)

    
    def preluare():       #functia de preluare a informatiilor despre o carte
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

    
    def salvare():      #functia care salvează datele unei cărți in baza de date
        cod=Cod_entry.get()
        autor=Autor_entry.get()
        titlu= Titlu_entry.get()
        editura=Editura_entry.get()
        an=An_entry.get()
        pret=Pret_entry.get()
        sql='SELECT Id  FROM cartile where Autor=%s and Titlu=%s and Editura=%s and Anul_aparitiei=%s and Pret=%s;'
        par=[autor,titlu,editura,an,pret]
        cursor.execute(sql,par)
        iduri=cursor.fetchall()
        
        date=[]
        for rand in iduri:
            date.append(rand[0])

        print(date)


        
        
        
        if date==[]:
            sql="INSERT INTO cartile(Autor,Titlu,Editura,Anul_aparitiei,Pret) VALUES(%s,%s,%s,%s,%s);"
            values=(autor,titlu,editura,an,pret)
            sql1='SELECT Id  FROM cartile where Autor=%s and Titlu=%s and Editura=%s and Anul_aparitiei=%s and Pret=%s;'
            cursor.execute(sql,values)
            mydb.commit()
            cursor.execute(sql1,values)
            id=cursor.fetchall()
            ids=[]
            for rand in id:
                ids.append(rand[0])

            id=int(ids[0])
            sql2=f'Insert into carticod values({cod},"liberă",{id});'
            cursor.execute(sql2)
            mydb.commit()
            print('aici')
            showinfo("Info","Cartea a fost inregistrata in baza de date.")
            
        else:
            sql=f"Select Count(Cod) from carticod where Cod={cod};"
            cursor.execute(sql)
            result=cursor.fetchall()
            if result==():
                idr=int(date[0])
                sql='Insert into carticod values (%s,"liberă",%s)'
                values=[cod,idr]
                cursor.execute(sql,values)
                mydb.commit()
                print('sau aici')
                showinfo("Info","Cartea a fost inregistrata in baza de date.")
            else:
                showerror(title="Eroare",message="Codul introdus există deja în baza de date.")
        
        
        Cod_entry.focus()

    #campurile ferestrei
    Cod=Label(canvas,text="Cod:",bg="#c7d3d4")
    Cod.grid(column=0,row=0,sticky=EW)

    Cod_entry=Entry(canvas,)
    Cod_entry.grid(column=1,row=0,sticky=W)

    Autor=Label(canvas,text="Autor:",bg="#c7d3d4")
    Autor.grid(column=0,row=1,sticky=EW)

    Autor_entry=Entry(canvas,)
    Autor_entry.grid(column=1,row=1,sticky=W)

    Titlu=Label(canvas,text="Titlu:",bg="#c7d3d4")
    Titlu.grid(column=0,row=2,sticky=EW)

    Titlu_entry=Entry(canvas,)
    Titlu_entry.grid(column=1,row=2,sticky=W)

    Editura=Label(canvas,text="Editura:",bg="#c7d3d4")
    Editura.grid(column=0,row=3,sticky=EW)

    Editura_entry=Entry(canvas,)
    Editura_entry.grid(column=1,row=3,sticky=W)

    An=Label(canvas,text="An:",bg="#c7d3d4")
    An.grid(column=0,row=4,sticky=EW)

    An_entry=Entry(canvas,)
    An_entry.grid(column=1,row=4,sticky=W)

    Pret=Label(canvas,text="Pret:",bg="#c7d3d4")
    Pret.grid(column=0,row=5,sticky=EW)

    Pret_entry=Entry(canvas,)
    Pret_entry.grid(column=1,row=5,sticky=W)

    salvare_btn=Button(canvas,text='Salvare',font="Helveitica,20",bg='red',fg='white',command=salvare)
    salvare_btn.grid(column=1,row=6,sticky=W)

    preluare()



    geam.mainloop()




#functia care deschide FEREASTRA CĂRȚI ÎMPRUMUTATE
def imprumut():

    def stergere_elemente_tabel(): #funcția care șterge elementele din tabel
        x = tabel.get_children()
        for item in x:
            tabel.delete(item)

    
    def returnata():   #functia care șterge un împrumut adus la timp (atunci când cartea este returnată)
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
        
        showinfo("info","Cartea a fost restituită.")
        window.destroy()
        mydb.commit()
    
    def mesaj():
        now = datetime.now()
        minut = int(now.strftime("%M"))+1
        ora = now.strftime("%H")
        
        for i in range(len(numere0)):
            try:
                kit.sendwhatmsg(numere0[i][0],f"Împrumutul a depășit data limită {numere0[i][1]} . Vă rog să returnați cartea/țile la bibliotecă.",int(ora),int(minut),wait_time=14,tab_close=True,close_time=2)
                minut=int(minut)+1
                

            except:
                
                showerror(title='Eroare', message='A apărut o eroare la împrumuturile trecute de termen!')
        
        for i in range(len(numere1)):
            try:
                kit.sendwhatmsg(numere1[i][0],f"Data limită împrumutului este {numere1[i][1]}.",int(ora),int(minut),wait_time=14,tab_close=True,close_time=2)
                minut=int(minut)+1
                

            except:
                
                showerror(title='Eroare', message='A apărut o eroare la împrumuturile în perioadă!')
        
        showinfo(title="Info",message="Abonații au fost notificați.") 
        

    window=Tk()
    
    window.resizable(0,0)
    window.config(background="#ece5e0")
    window.iconbitmap('carti_i.ico')
    window.configure(background="#DBFFE2")
    window.title('Cărți împrumutate')
    
    w = 1600 
    h = 750

    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #câmpurile ferestrei
    coloane=[0,1,2,3,4,5,6,7]
    tabel=ttk.Treeview(window,columns=coloane,show="headings",height=30)
    tabel.pack()

    adus=Button(window,text="Returnată",bg="#547F5D",fg="white",font=("Helvetica",20),command=returnata)
    adus.pack()

    msj_elev=Button(window,text="Notifică elevii",bg="#547F5D",fg="white",font=("Helvetica",20),command=mesaj)
    msj_elev.pack()

    tabel.heading(0,text='COD IMPRUMUT')
    tabel.heading(1,text='COD ABONAT')
    tabel.heading(2,text='NUME')
    tabel.heading(3,text='CLASA')
    tabel.heading(4,text='COD CARTE')
    tabel.heading(5,text='DATA IMPRUMUTULUI')
    tabel.heading(6,text='DATA RETURNARII')
    tabel.heading(7,text='TELEFON')
    tabel.tag_configure('limita',background='yellow',foreground='green')
    tabel.tag_configure('trecut',background='#FF6A6A',foreground="white")
    
   
    stergere_elemente_tabel()

    q="Select * from imprumuturi"
    cursor.execute(q)
    result=cursor.fetchall()

    datele=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],
              x[5],x[6],x[7])
        datele.append(list1)

    global numere0,numere1
    numere0=[]
    numere1=[]
    for rand in datele:
        
        if date.today()>rand[6]:
            my_tag='trecut'
            numere0.append([rand[7],rand[6]])
            
        else: 
            if date.today()+timedelta(days=4)> rand[6]:
                my_tag='limita'
                numere1.append([rand[7],rand[6]])
            
            else:
                my_tag='normal'
                
            
        
        tabel.insert('',END,values=rand,tags=my_tag)
    
    

    
    
    

    
    
#functia care deschide LISTA DE ELEVI (ABONAȚI la bibliotecă)
def abonati():
    window=Tk()
    
    window.resizable(0,0)
    window.iconbitmap('lista_elevi.ico')
    window.title('Listă abonați')
    window.configure(background="#FFDFBA")
    window.lift()

    w = 1500 
    h = 1000

    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #funcția care generează un cod QR pentru elevul selectat
    def generareQR():
        ite=tabel.item(tabel.focus())
        elev=""
        elev=str(ite['values'][0])+'/'+str(ite['values'][1])+'/'+str(ite['values'][2])+'/'+str(ite['values'][3])+'/'+str(ite['values'][4])+'/'+str(ite['values'][5])+'/'+'Biblioteca LNI'+'/'+'Abonat'
        elev=str(elev)
        nume=""
        nume='qr_'+str(ite['values'][0])
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(elev.encode('utf-8'))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{nume}.png") 
        showinfo(title="Info",message="Fișierul a fost salvat.")
        window.lift()

    def stergere():     #functia care sterge o carte din baza de date
    
        ite=tabel.item(tabel.focus())
        cell=ite['values'][0]
        parametri=(cell,)
        sql="delete from abonati where Cod_abonat=%s;"
        cursor.execute(sql,parametri)
        cell=str(cell)
        showinfo("Info","Ați șters abonatul cu codul "+cell )
        mydb.commit()
        window.lift()



    def inserare():    #functia care inserează un abonat in tabelul abonatilor
        geam=Tk()   # fereastra adaugare abonati
        geam.configure(background="#FFDFBA")
        geam.resizable(0,0)
      
        geam.title("Inserare abonat nou")
        

        w = 300
        h = 200

        ws = window.winfo_screenwidth() 
        hs = window.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        geam.geometry('%dx%d+%d+%d' % (w, h, x, y))

        canvas=Canvas(geam,width=1920,height=1080)
        canvas.pack(expand=True,fill=BOTH)
        canvas.columnconfigure(0,weight=1)
        canvas.columnconfigure(1,weight=3)
        

        
        def preluare():       #functia de preluare a informatiilor despre un abonat
            
            
                Nume_entry.focus()
                def log1(event):
                    Prenume_entry.focus()
                    def log2(event):
                        Clasa_entry.focus()
                        def log3(event):
                            Telefon_entry.focus()
                        Clasa_entry.bind('<Return>',log3)    

                    Prenume_entry.bind('<Return>',log2)

                Nume_entry.bind('<Return>',log1)
        
            


        def salvare():      #functia care salvează datele unui abonat in baza de date

            data_azi=str(date.today())
            sql="INSERT INTO abonati(Nume,Prenume,Clasa,Data_abonarii,Telefon) VALUES(%s,%s,%s,%s,%s);"
            values=( Nume_entry.get(), Prenume_entry.get(), Clasa_entry.get(),data_azi,Telefon_entry.get() )
            try:
                cursor.execute(sql,values)
                mydb.commit()
                showinfo(title="Info",message="Datele au fost introduse in baza de date.")
            
                
                
    

            except Exception:   # afisarea erorii
                messagebox.showerror(title="Eroare",message = "Codul introdus este deja înregistrat in baza de date")
                
                
            window.lift()
            geam.lift()
            
            
             



                                  
        geam.lift() 
        #campurile ferestrei
        

        Nume=Label(canvas,text="Nume:")
        Nume.grid(column=0,row=1,sticky=EW)

        Nume_entry=Entry(canvas,)
        Nume_entry.grid(column=1,row=1,sticky=W)

        Prenume=Label(canvas,text="Prenume:")
        Prenume.grid(column=0,row=2,sticky=EW)

        Prenume_entry=Entry(canvas,)
        Prenume_entry.grid(column=1,row=2,sticky=W)

        Clasa=Label(canvas,text="Clasa:")
        Clasa.grid(column=0,row=3,sticky=EW)

        Clasa_entry=Entry(canvas,)
        Clasa_entry.grid(column=1,row=3,sticky=W)

        Telefon=Label(canvas,text="Telefon:")
        Telefon.grid(column=0,row=4,sticky=EW)

        Telefon_entry=Entry(canvas,)
        Telefon_entry.grid(column=1,row=4,sticky=W)

    

        salvare_btn=Button(canvas,text='Salvare',font="helvetica,20",bg='red',fg='white',command=salvare)
        salvare_btn.grid(column=1,row=6,sticky=W)

        
        preluare()


        geam.mainloop()

    def schimbare(event):  #funcția care actualizează filtrul
            global criteriu
            criteriu=filtru.get()
            if criteriu=="QR":
                cauta_QR()
        
    
    def stergere_elemente_arbore():  #funcția care șterge toate rândurile din tabel
            
            x = tabel.get_children()
            for item in x:
                tabel.delete(item)

    
    def cauta(event):      #functia care face cautarea in baza de date în funcție de bara de căutare
            cuvant=caseta.get()

            cuv=("%"+cuvant +"%")
            sql="SELECT * FROM abonati WHERE {} LIKE '{}' ;".format(criteriu,cuv)
            cursor.execute(sql,)
            records = cursor.fetchall()
        
            recor=[]
            for x in records:
                list1=(x[0],x[1], x[2],x[3],x[4])
                recor.append(list1)
            mydb.commit()

            stergere_elemente_arbore()
            for record in records:
                tabel.insert('', 0, values=record)


        
    def cauta_QR():    #funcția care face căutarea în funcție de codul stocat în codul QR
            var=""
            def reader_cam_qr(): #funcția care scanează codul QR prin intermediul camerei web
                cam =cv2.VideoCapture(0)
                cam.set(5, 640)
                cam.set(6, 480)

                camera = True
                while camera == True:
                    suceess, frame= cam.read()
                    for i in decode(frame):
                        return i.data.decode('utf-8')
        
            
            var=reader_cam_qr()
            Cod=int(var.split('/')[0])
        

            sql="SELECT * FROM abonati WHERE Cod_abonat={} ;".format(Cod)
            cursor.execute(sql,)
            records = cursor.fetchall()
        
            recor=[]
            for x in records:
                list1=(x[0],x[1], x[2],x[3],x[4])
                recor.append(list1)
            mydb.commit()

            stergere_elemente_arbore()
        
            for record in records:
                tabel.insert('', 0, values=record)

    

    global criteriu
    
    frame3=Frame(window)
    frame3.pack(side=TOP)

    label=Label(frame3,text="Caută după:",font=("Helvetica",18),bg="#FFDFBA",fg="#5E3205")
    label.pack(side=LEFT)

    filtru=ttk.Combobox(frame3,width=30,font=("Helvetica",16))  #filtru (caută după)
    filtru.pack(side=LEFT)

    

    valori=["Cod_abonat","Nume","Prenume","Clasa","QR"]
    filtru['values']=valori      
    filtru['state']='readonly'


    caseta=Entry(window,font=("Helvetica",20),fg="#323232",width=67)  #bara de căutare
    caseta.pack(side=TOP,padx=5,pady=5)

    global tabel
    coloane=[0,1,2,3,4,5]
    tabel=ttk.Treeview(window,columns=coloane,show="headings",height=43,)
    tabel.pack()

    tabel.heading(0,text='COD ABONAT')
    tabel.heading(1,text='NUME')
    tabel.heading(2,text='PRENUME')
    tabel.heading(3,text='CLASA')
    tabel.heading(4,text='DATA ABONARII')
    tabel.heading(5,text='TELEFON')
    
  

    q="Select * from abonati"
    cursor.execute(q)
    result=cursor.fetchall()
    datele=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],x[5])
        datele.append(list1)
    for rand in datele: 
        
        tabel.insert('',END,values=rand)

    
            
    caseta.bind( '<Return>',cauta)
    filtru.bind('<<ComboboxSelected>>',schimbare )

    

    def imprumut_nou(): #funcția care adaugă un împrumut nou
        ite=tabel.item(tabel.focus())
        cod_abonat=ite['values'][0]
        nume=ite['values'][1]
        clasa=ite['values'][3]
        telefon=ite['values'][5]

        

        data_azi=str(date.today())
        data_return=str(date.today() +timedelta(days=14))
        
        win=Tk()
        win.title("Adăugare împrumut")
        win.configure(background="#FFDFBA")
        win.resizable(0,0)

        w = 300
        h = 150

        ws = root.winfo_screenwidth() 
        hs = root.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win.geometry('%dx%d+%d+%d' % (w, h, x, y))

        global cod_carte
        
        def reader_cam_qr(): #funcția care scanează codul QR de pe o carte
            cam =cv2.VideoCapture(0)
            cam.set(5, 640)
            cam.set(6, 480)

            camera = True
            while camera == True:
                suceess, frame= cam.read()
                for i in decode(frame):
                    return i.data.decode('utf-8')
        
            
        

        def verif(): #funcția care preia codul cărți ori din câmpul de introducere ori din codul QR
            
            if Titlu_entry.get()=="":
                var=reader_cam_qr()
                cod_carte=int(var.split('/')[0])
                Titlu_entry.insert(END,str(cod_carte))
    
            
        

        def save_imprumut():   #funcția care salvează împrumutul în baza de date
            cod_carte=int(Titlu_entry.get())

            sql2="Select * from carti where Cod=%s and Stare='liberă';"
            test2=(cod_carte,)
            cursor.execute(sql2,test2)
            re=cursor.fetchall()
            if len(re)== 1:
                
                sql="insert into imprumuturi (COD_ABONAT,NUME,CLASA,COD_CARTE,DATA_IMPRUMUT,DATA_RETURNARII,TELEFON) values(%s,%s,%s,%s,%s,%s,%s);"
            
                test=(cod_abonat,nume,clasa,cod_carte,data_azi,data_return,telefon)
                cursor.execute(sql,test)

                sql1="update carti set Stare='împrumutată'  where Cod=%s;"
                test1=(cod_carte,)
                cursor.execute(sql1,test1)
                showinfo(title="Info",message="Împrumut adăugat.")
                mydb.commit()
                win.destroy()
                window.lift()
            else:
                showerror(title='Eroare',message="Cartea este împrumutată!")
                win.destroy()
                window.lift()
        

        
        #câmpurile ferestrei IMPRUMUT NOU

        Titlu=Label(win,text="Cod carte:", background="#FFDFBA",font="Helvetica,16")
        Titlu.pack()
        Titlu_entry=Entry(win,font="Helvetica,20")
        Titlu_entry.pack()

        codqr=Button(win,text="QR",font="Helvetica,16",bg="green",fg="white",command=verif)
        codqr.pack()

        salvare_btn=Button(win,text='Salvare',font="Helvetica,16",bg='red',fg='white',command=save_imprumut)
        salvare_btn.pack()

        win.mainloop()

    inser=Button(frame3,text="Inserare elevi",command=inserare,font=("Helvetica",13),bg="#F1BDB0",fg="#5E3205").pack(side=LEFT,)
    sterg=Button(frame3,text="Stergere elevi",command=stergere,font=("Helvetica",13),bg="#F1BDB0",fg="#5E3205").pack(side=LEFT,padx=3)
    generare=Button(frame3,text="Genereaza cod QR",command=generareQR,font=("Helvetica",13),bg="#F1BDB0",fg="#5E3205").pack(side=LEFT,)
    adauga=Button(frame3,text="Adaugă împrumut",font=("Helvetica",13),bg="#F1BDB0",fg="#5E3205",command=imprumut_nou).pack(side=LEFT,padx=3)
    
    window.mainloop()

        


#FEREASTRA PRINCIPALA

root = Tk()
root.geometry('1920x1080')
root.title('Școlibra')
root.iconbitmap('iconbitmap_principal.ico')
root.resizable(0,0)

w = 1920 
h = 1080

ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))



#imaginea pentru fundalul canvas_principala
photo=Image.open("biblioteca1.jpeg")
photo1=photo.resize((1920,1080))
img=ImageTk.PhotoImage(photo1)

canvas=Canvas(root,width=1920,height=1080)
canvas.pack(expand=True,fill=BOTH)
canvas.create_image(0,0,image=img,anchor=NW)

imglni=Image.open("lni.jpg")
imglni=imglni.resize((800,400))
imglni=ImageTk.PhotoImage(imglni)

#câmpurile ferestrei

frame0=Frame(canvas,height=390,width=780,bg="#F5EBE0")
frame0.place(relx=0,rely=0,anchor=NW)

welcome=Label(frame0,image=imglni)
welcome.place(relx=0.5,rely=0.5,anchor=CENTER)


frame=Frame(canvas,height=400,width=800,)
frame.place(rely=0,relx=1,anchor=NE)

citat=Label(frame,text=citate,height=400,width=800,font=("Comic Sans MS",16),bg="#F6E1B5",fg="#805E19", )               
citat.place(relx=0.5,rely=0.5,anchor=CENTER)


frame1=Frame(canvas,width=780,height=400)
frame1.place(relx=0.5,rely=0.79,anchor=CENTER)

imprumuturi=Button(frame1,text="Cărți împrumutate",width=70,height=6,bg="#F6E1B5" ,font=("Comic Sans",15),fg="#805E19",command=imprumut)
imprumuturi.place(relx=0,rely=0,anchor=NW,)

carti=Button(frame1,text="Listă cărți",width=70,height=6,bg="#F6E1B5",font=("Comic Sans",15),fg="#805E19",command=search)
carti.place(relx=0,rely=0.5,anchor=W,)

elevi=Button(frame1,text="Listă elevi",width=70,height=5,bg="#F6E1B5",font=("Comic Sans",15),fg="#805E19",command=abonati)
elevi.place(relx=0,rely=1,anchor=SW)

data_azi=str(date.today())
data_ora=Label(canvas,text=data_azi,width=10,height=3,font=("Helvetica",20),bg="#F6E1B5",fg="#805E19")
data_ora.place(relx=0.9,rely=0.99,anchor=SW,)



root.mainloop()