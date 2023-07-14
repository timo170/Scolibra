
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
import requests
import webbrowser


#conectare la baza de date
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="biblioteca"
)
cursor=mydb.cursor()

#importare citate din baza de date in variabila citate
sql="Select Citate from citate where Numar=%s"
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
        if criteriu=='Cod':
            sql=f"Select Id from carticod where Cod={int(cuvant)};"
            cursor.execute(sql)
            records = cursor.fetchall()
    
            date=[]
            for x in records:
                date.append(x[0])
            id=date[0]
            sql=f"Select * from cartile where Id={id};"
        else:
            cuv=("%"+cuvant +"%")
            sql=f"SELECT * FROM cartile WHERE {criteriu} LIKE '{cuv}' ;"
        
        cursor.execute(sql)
        records = cursor.fetchall()
    
        date=[]
        for x in records:
            list1=(x[0],x[1], x[2],
               x[3],
               x[4],
               x[5],)
            date.append(list1)
        

        stergere_elemente_arbore()
        tag1='roz'
        tag2='normal'
        for rand in date:
            id=rand[0]
            q="SELECT COUNT(Cod) FROM carticod Where Id=%s;"
            para=[id]
            cursor.execute(q,para)
            nr=cursor.fetchall()
            nr=nr[0]
            if tag1=='roz':
                tag1='porto'
            else:
                tag1='roz'
            carte=tree.insert('',END,text=id,values=[rand[1],rand[2],rand[3],rand[4],rand[5],nr],tags=tag1)
    
            com=f"Select Cod from carticod where Id={id} and Stare='liberă';"
            cursor.execute(com)
            result=cursor.fetchall()
            for cod in result:
                if tag2=='normal':
                    tag2='gri'
                else:
                    tag2='normal'
                tree.insert(carte,END,values=("","","","","","",cod),tags=tag2)
            

        
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
        cod=int(var.split('/')[0])
        
        stergere_elemente_arbore()

        sql=f"SELECT Id FROM carticod WHERE Cod={cod};"
        cursor.execute(sql)
        records = cursor.fetchall()
        
        date=[]
        date.append(records[0])
        for co in date:
            id=co[0]

        
        sql1=f"Select * from cartile where Id={id};"
        cursor.execute(sql1)
        result=cursor.fetchall()
        
        
        q=f"SELECT COUNT(Id) FROM carticod Where Id={id};"
        cursor.execute(q)
        nr=cursor.fetchall()
        nr=nr[0]

        date=[]
        for rand in result:
            list1=[rand[1],rand[2],rand[3],rand[4],rand[5],nr]
            date.append(list1)

        
            ID=tree.insert("",END,text=id,values=rand)
        
        q=f"Select Cod from carticod where Id={id};"
        cursor.execute(q)
        result=cursor.fetchall()
        date=[]
        for rand in result:
            
            date.append(rand[0])
        

        for co in date:
            if co==cod:
                my_tag='cod_scanat'
            else:
                my_tag='normal'
                


            tree.insert(ID,END,values=["","","","","","",co],tags=my_tag)
        
        
        

        
        

    global criteriu
    
    #funcția care generează un cod QR pentru cartea selectată
    def generareQR():
        try:
            id_cod=tree.focus()
            id_carte=tree.parent(id_cod)
            carte=tree.item(id_carte)
            cod=tree.item(id_cod)["values"][6]
            id=carte["text"]
            titlu=carte["values"][1]
            autor=carte["values"][0]
            editura=carte["values"][2]
            an=carte["values"][3]
            pret=carte["values"][4]
            carte=str(cod)+'/'+str(autor)+'/'+str(titlu)+'/'+str(editura)+'/'+str(an)+'/'+str(pret)+'/'+str(id)+'/'+'Biblioteca LNI'
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
    
    

    
    





    window=Tk()
    window.resizable(1,1)
    window.iconbitmap('../Școlibra_program/lista_carti.ico')
    window.title('Listă cărți')
    
    window.configure(background="#c7d3d4")
    window.resizable(0,0)

    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    w = int(ws/1.24)
    h = int(hs/1.08)

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


    valori=["Cod","Autor","Titlu","Editura","Anul_aparitiei","Pret","QR"]
    filtru['values']=valori      
    filtru['state']='readonly'


    caseta=Entry(window,font=("Helvetica",20),fg="black",width=93)  #bara de căutare
    caseta.pack(anchor=CENTER)
    
    global tree
    coloane=(1,2,3,4,5,6,7)
    tree=ttk.Treeview(window,columns=coloane) #tabelul cu afișări
    
    
    # configurare Scrollbar
    scrollbar = Scrollbar(window,orient='vertical',command=tree.yview,width=20)
    scrollbar.pack(side=RIGHT,fill='y')
    tree.place(relx=0.01,rely=0.08,relheight=0.91,relwidth=0.97)
    
    tree['yscrollcommand'] = scrollbar.set
    
    
   
    tree.heading("#0",text='ID')
    tree.heading(1,text='AUTOR')
    tree.heading(2,text='TITLU')
    tree.heading(3,text='EDITURA')
    tree.heading(4,text='ANUL_APARIȚIEI')
    tree.heading(5,text='PREȚ')
    tree.heading(6,text='NR BUCĂȚI')
    tree.heading(7,text='COD CĂRȚI LIBERE')

    tree.tag_configure('cod_scanat',background='yellow')
    tree.tag_configure('gri',background='#EEE6DE')
    tree.tag_configure('roz',background="#FFE3E3")
    tree.tag_configure('porto',background="#FFC0A4",)

    tree.column('#0',minwidth=40,width=40,anchor=CENTER)
    

    q="Select * from cartile;"
    cursor.execute(q)
    result=cursor.fetchall()
   
    date=[]
    for rand in result:
        list1=[rand[0],rand[1],rand[2],rand[3],rand[4],rand[5]]
        date.append(list1)
    tag1='roz'
    tag2='normal'
    

    for rand in date:
        id=int(rand[0])
        par=[id,]
        q="SELECT COUNT(Id) FROM carticod Where Id=%s;"
        cursor.execute(q,par)
        nr=cursor.fetchall()
        nr=nr[0]

        ID=tree.insert("",END,text=id,values=[rand[1],rand[2],rand[3],rand[4],rand[5],nr],tags=tag1)
        if tag1=='roz':
            tag1='porto'
        else:
            tag1='roz'
        q="Select Cod from carticod where Id=%s and Stare='liberă';"
        
        cursor.execute(q,par)
        result=cursor.fetchall()
        
        for cod in result:
            tree.insert(ID,END,values=["","","","","","",cod],tags=tag2)
            if tag2=='normal':
                tag2='gri'
            else:
                tag2='normal'
            

    
    
    caseta.bind( '<Return>',cauta)
    filtru.bind('<<ComboboxSelected>>',schimbare )
   
    window.mainloop()

    

    

#functia care sterge o carte din baza de date
def stergere():
    try:
        id_cod=tree.focus()
        id_carte=tree.parent(id_cod)
        id=tree.item(id_carte)["text"]
        
        valori=tree.item(id_cod)
        cod=valori["values"][6]
        parametri=(cod,)
        print(cod)
        sql="delete from carticod where Cod=%s;"
        cursor.execute(sql,parametri)
        mydb.commit()
        
        dic={'Id':id}
        res=requests.post('https://scolibra.000webhostapp.com/stergbucata.php',json=dic)
        print(res)

        
        
        cod=str(cod)
        showinfo("Info","Ați șters cartea cu codul "+cod )
        
    except:
        id_carte=tree.focus()
        id=tree.item(id_carte)["text"]
        sql=f"Select Count(Cod) from carticod where Id={id};"
        cursor.execute(sql)
        nr=cursor.fetchall()
        nr=nr[0]
        nr=nr[0]
        if nr==0:
            sql=f"Delete from cartile where Id={id};"
            cursor.execute(sql)
            mydb.commit()
            dic={'Id':id}
            res=requests.post(url='https://scolibra.000webhostapp.com/stergcarte.php',json=dic)
            id=str(id)
            showinfo("Info","Ați șters cartea cu Id-ul "+id)
        



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
          
        if date==[]:
            #cazul in care nu exista cartea respectiva in baza de date
            sql="INSERT INTO cartile(Autor,Titlu,Editura,Anul_aparitiei,Pret) VALUES(%s,%s,%s,%s,%s);"
            values=(autor,titlu,editura,an,pret)
            sql1='SELECT Id  FROM cartile where Autor=%s and Titlu=%s and Editura=%s and Anul_aparitiei=%s and Pret=%s;'
            cursor.execute(sql,values)
            mydb.commit()
            cursor.execute(sql1,values)
            id=cursor.fetchall()
            id=list(id[0])
            id=int(id[0])
            sql2=f'Insert into carticod values({cod},"liberă",{id});'
            cursor.execute(sql2)
            mydb.commit()
            nr=1
            dic={'Id':id, 'Autor':autor, 'Titlu':titlu, 'Editura':editura, 'An':an,'Nr':nr}
            res=requests.post(url='https://scolibra.000webhostapp.com/inserare_date.php',json=dic)
            print(res)
            showinfo("Info","Cartea a fost inregistrata in baza de date.")
            
        else:#cazul in care cartea este inregistrata in baza de date, dar adaugam o noua bucata cu un cod nou
                idr=int(date[0])
                sql1=f"Select Count(Cod) from carticod where Cod={cod} and Id={idr};"
                cursor.execute(sql1)
                result=cursor.fetchall()
                result=list(result[0])
                count=int(result[0])
                if count==0:
                    sql='Insert into carticod values (%s,"liberă",%s)'
                    values=[cod,idr]
                    cursor.execute(sql,values)
                    mydb.commit()
                    stare="liber_"
                    sql=f"select Count(Cod) from carticod where Id={idr} and Stare like '{stare}';"
                    cursor.execute(sql)
                    result=cursor.fetchall()
                    result=list(result[0])
                    nr=int(result[0])
                    dic={'Id':idr,'Nr':nr}
                    res=requests.post(url='https://scolibra.000webhostapp.com/adaugbucata.php',json=dic)
                    print(res)
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

    def prelungire():
        ite=tabel.item(tabel.focus())
        cod_imprumut=int(ite['values'][0])
        data_returnarii=ite["values"][6]
        an=int(data_returnarii.split(sep='-')[0])
        luna=int(data_returnarii.split(sep='-')[1])
        zi=int(data_returnarii.split(sep='-')[2])
        data_returnarii=date(year=an,month=luna,day=zi)
        data_noua=str(data_returnarii +timedelta(days=14))
        try:
            query=f"Update imprumuturi set DATA_RETURNARII='{data_noua}' where COD_IMPRUMUT={cod_imprumut};"
            mydb.commit()
            showinfo(title="Info",message="Împrumutul a fost prelungit cu două săptămâni.")
        except:
            showerror(title="Eroare", message="Contactați creatorul aplicației !")
        


    
    def returnata():   #functia care șterge un împrumut adus la timp (atunci când cartea este returnată)
        ite=tabel.item(tabel.focus())
        cell=ite['values'][0]
        cod_carte=int(ite["values"][4])
        sql1="update carticod set Stare='liberă' where Cod=%s;"
        para=(cod_carte,)
        cursor.execute(sql1,para)
        mydb.commit()
        cell=str(cell)
        
        sql=f"delete from imprumuturi where COD_IMPRUMUT={cell};"
        cursor.execute(sql)
        mydb.commit()

        sql=f'Select Id from carticod where Cod={cod_carte};'
        cursor.execute(sql)
        id=cursor.fetchall()
        id=list(id[0])
        id=int(id[0])
        stare="liber_"
        sql1=f"select Count(Cod) from carticod where Id={id} and Stare like '{stare}';"
        cursor.execute(sql1)
        result=cursor.fetchall()
        result=list(result[0])
        nr=int(result[0])
        dic={'Id':id,'Nr':nr}
        res=requests.post(url='https://scolibra.000webhostapp.com/adaugbucata.php',json=dic)
        print(res)
        
        showinfo("info","Cartea a fost restituită.")
        window.destroy()
        mydb.commit()
    
    def mesaj():
        now = datetime.now()
        minut = int(now.strftime("%M"))+1
        ora = now.strftime("%H")
        
        
        print(numere0)
        print(numere1)

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
    window.iconbitmap('../Școlibra_program/carti_i.ico')
    window.configure(background="#DBFFE2")
    window.title('Cărți împrumutate')

    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    w = int(ws/1.16)
    h = int(hs/1.44)

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #câmpurile ferestrei
    coloane=[0,1,2,3,4,5,6,7]
    tabel=ttk.Treeview(window,columns=coloane,show="headings",height=30)
    tabel.pack()

    adus=Button(window,text="Returnată",bg="#547F5D",fg="white",font=("Helvetica",18),width=10,height=1,command=returnata)
    adus.pack()

    msj_elev=Button(window,text="Notifică elevii",bg="#547F5D",fg="white",font=("Helvetica",18),width=10,height=1,command=mesaj)
    msj_elev.pack()

    prelung=Button(window,text="Prelungire",bg="#547F5D",fg="white",font=("Helvetica",18),width=10,height=1,command=prelungire)
    prelung.pack()

    tabel.heading(0,text='COD IMPRUMUT')
    tabel.heading(1,text='COD ABONAT')
    tabel.heading(2,text='NUME')
    tabel.heading(3,text='CLASA')
    tabel.heading(4,text='COD CARTE')
    tabel.heading(5,text='DATA IMPRUMUTULUI')
    tabel.heading(6,text='DATA RETURNARII')
    tabel.heading(7,text='TELEFON')
    tabel.tag_configure('limita',background='yellow',)
    tabel.tag_configure('trecut',background='red',foreground="white")
    tabel.tag_configure('gri',background='#EEE6DE')
    
   
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
    my_tag='normal'
    for rand in datele:
        
        if date.today()>rand[6]:
            my_tag='trecut'
            numere0.append([rand[7],rand[6]])
            
        else: 
            if date.today()+timedelta(days=4)> rand[6]:
                my_tag='limita'
                numere1.append([rand[7],rand[6]])
            
            else:
                if my_tag=='normal':
                    my_tag='gri'
                else:
                    my_tag="normal"
                
            
        
        tabel.insert('',END,values=rand,tags=my_tag)
    
    

    
    
    

    
    
#functia care deschide LISTA DE ELEVI (ABONAȚI la bibliotecă)
def abonati():
    window=Tk()
    
    window.resizable(0,0)
    window.iconbitmap('../Școlibra_program/lista_elevi.ico')
    window.title('Listă abonați')
    window.configure(background="#FFDFBA")
    window.lift()


    ws = window.winfo_screenwidth() 
    hs = window.winfo_screenheight()

    w = int(ws/1.20)
    h = int(hs/1.08)

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

    def stergere():     #functia care sterge un abonat din baza de date
    
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
            tag="normal"
            for record in records:
                tabel.insert('', 0, values=record,tags=tag)
                if tag=="normal":
                    tag='gri'
                else:
                    tag='normal'


        
    def cauta_QR():    #funcția care face căutarea în funcție de codul stocat în codul QR
        var=""
        cam =cv2.VideoCapture(0)
        cam.set(5, 640)
        cam.set(6, 480)
            
        camera = True
        while camera == True:
            suceess, frame= cam.read()
            for i in decode(frame):
                var=i.data.decode('utf-8')
                camera=False
        
            
    
        Cod=int(var.split('/')[0])
        sql=f"SELECT * FROM abonati WHERE Cod_abonat={Cod};"
        cursor.execute(sql)
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
    tabel.column(0,anchor=W)
    tabel.column(1,anchor=W)
    tabel.column(2,anchor=W)
    tabel.column(3,anchor=W)
    tabel.column(4,anchor=W)
    tabel.column(5,anchor=W)

    tabel.tag_configure('gri',background="#EEE6DE")
    
  

    q="Select * from abonati"
    cursor.execute(q)
    result=cursor.fetchall()
    datele=[]
    for x in result:
        list1=(x[0],x[1], x[2],
              x[3],
              x[4],x[5])
        datele.append(list1)

    tag='normal'
    for rand in datele: 
        tabel.insert('',END,values=rand,tags=tag)
        if tag=="normal":
            tag='gri'
        else:
            tag='normal'

    
            
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

        ws = root.winfo_screenwidth() 
        hs = root.winfo_screenheight()

        w =300
        h = 150

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

            sql2="Select Cod from carticod where Cod=%s and Stare='liberă';"
            test2=(cod_carte,)
            cursor.execute(sql2,test2)
            re=cursor.fetchall()
            if len(re)== 1:
                
                sql="insert into imprumuturi (COD_ABONAT,NUME,CLASA,COD_CARTE,DATA_IMPRUMUT,DATA_RETURNARII,TELEFON) values(%s,%s,%s,%s,%s,%s,%s);"
            
                test=(cod_abonat,nume,clasa,cod_carte,data_azi,data_return,telefon)
                cursor.execute(sql,test)

                sql1=f"update carticod set Stare='împrumutată'  where Cod={cod_carte};"
                
                cursor.execute(sql1)
                mydb.commit()
                showinfo(title="Info",message="Împrumut adăugat.")
                
                sql=f"select Id from carticod where Cod={cod_carte};"
                cursor.execute(sql)
                id=cursor.fetchall()
                id=list(id[0])
                id=int(id[0])

                dic={'Id':id}
                res=requests.post('https://scolibra.000webhostapp.com/stergbucata.php',json=dic)
                print(res)

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

        
def link():
    return webbrowser.open("https://scolibra.000webhostapp.com/")

#FEREASTRA PRINCIPALA

root = Tk()

root.title('Școlibra')
root.iconbitmap('../Școlibra_program/iconbitmap_principal.ico')
root.resizable(0,0)

w = root.winfo_screenwidth() 
h = root.winfo_screenheight()

ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))



#imaginea pentru fundalul canvas_principala
photo=Image.open("../Școlibra_program/biblioteca1.jpeg")
photo1=photo.resize((ws,hs))
img=ImageTk.PhotoImage(photo1)

canvas=Canvas(root,)
canvas.place(relx=0,rely=0,relheight=1,relwidth=1)
canvas.create_image(0,0,image=img,anchor=NW)

imglni=Image.open("../Școlibra_program/lni.jpg")
imglni=imglni.resize((int(ws/2.5),int(hs/2.5)))
imglni=ImageTk.PhotoImage(imglni)

#câmpurile ferestrei

frame0=Frame(canvas,bg="#F5EBE0")  #height=390,width=780,
frame0.place(relx=0,rely=0,relheight=0.4,relwidth=0.4,anchor=NW)

welcome=Label(frame0,image=imglni)
welcome.place(relx=0.5,rely=0.5,anchor=CENTER)


frame=Frame(canvas,) #height=400,width=800,
frame.place(rely=0,relx=1,relheight=0.4,relwidth=0.4,anchor=NE)

citat=Label(frame,text=citate,font=("Comic Sans MS",16),bg="#F6E1B5",fg="#805E19", ) #height=400,width=800         
citat.place(relx=0.5,rely=0.5,relheight=1,relwidth=1,anchor=CENTER)


frame1=Frame(canvas,bg="#F6E1B5") #width=780,height=400
frame1.place(relx=0.5,rely=0.79,relheight=0.4,relwidth=0.5,anchor=CENTER)

imprumuturi=Button(frame1,text="Cărți împrumutate",bg="#F6E1B5" ,font=("Comic Sans",17),fg="#805E19",command=imprumut)
imprumuturi.place(relx=0,rely=0,relheight=0.33,relwidth=1, anchor=NW,)

carti=Button(frame1,text="Listă cărți",bg="#F6E1B5",font=("Comic Sans",17),fg="#805E19",command=search)
carti.place(relx=0,rely=0.5,relheight=0.33,relwidth=1,anchor=W,)

elevi=Button(frame1,text="Listă elevi",bg="#F6E1B5",font=("Comic Sans",17),fg="#805E19",command=abonati)
elevi.place(relx=0,rely=1,relheight=0.33,relwidth=1,anchor=SW)

data_azi=str(date.today())
data_ora=Label(canvas,text=data_azi,font=("Helvetica",20),bg="#F6E1B5",fg="#805E19") #width=10,height=3,
data_ora.place(relx=0.89,rely=0.92,relheight=0.1,relwidth=0.1,anchor=W,)

link_buton=Button(canvas,text="Școlibra website",font=("Helvetica",17),bg="#F6E1B5",fg="#805E19",command=link) #width=13,height=3,
link_buton.place(relx=0.13,rely=0.92,relheight=0.1,relwidth=0.12,anchor=E,)



root.mainloop()