from tkinter import *
import random
import mysql.connector
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.messagebox import showinfo

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
cursor.execute(sql,[random.randrange(0,11)])
citate=cursor.fetchall()    
citate = ','.join(map(str, citate[0]))

#aici incerc ceva special o modificare



#functia care deschide FEREASTRA DE CAUTARE
def search():
    window=Tk()
    window.resizable(1,1)
    window.geometry('1000x600')


    frame3=Frame(window)
    frame3.pack(side=TOP)

    label=Label(frame3,text="Caută după:",font=("Helvetica",15))
    label.pack(side=LEFT)

    sterge=Button(frame3,width=10,text="Șterge carte")
    sterge.pack(side=RIGHT)

    adauga=Button(frame3,width=10,text="Adaugă carte",command=inserare)
    adauga.pack(side=RIGHT)


    select=StringVar()
    filtru=ttk.Combobox(frame3,width=30,font=("Helvetica",16))
    filtru.pack(padx=5,side=RIGHT)


    valori=["Cod","Autor","Titlu","Editura","An","Pret","Stare"]
    filtru['values']=valori      
    filtru['state']='readonly'



    
    
    

    
    caseta=Entry(window,font=("Helvetica",20),width=100)
    caseta.pack(anchor=NW,padx=5)

    lista=Listbox(window, width=190,height=100,font=("Helvetica",18),selectmode=EXTENDED)
    lista.pack()

    

    def schimbare(event):
        global criteriu
        criteriu=filtru.get()
        if criteriu=="Cod":
            criteriu=0
        else:
            if criteriu=="Autor":
                criteriu=1
            else:
                if criteriu=="Titlu":
                    criteriu=2
                else:
                    if criteriu=="Editura":
                        criteriu=3
                    else:
                        if criteriu=="An":
                            criteriu=4
                        else:
                            if criteriu=="Pret":
                                criteriu=5
                            else:
                                if criteriu=="Stare":
                                    criteriu=6
    
    
    
    filtru.bind('<<ComboboxSelected>>',schimbare )

    def actualizare(data):
        #golim lista
        lista.delete(0,END)

        for item in data:
            lista.insert(END,item)
    
    #actualizare caseta de intrare cu lista selectata
    def golire(e):
        #Golire caseta de intrare
        caseta.delete(0,END)

        #Adaugare
        caseta.insert(0,lista.get(ANCHOR))

    #verificare caseta cu lista

    def verificare(e):
        introdus=caseta.get()
        if introdus == '':
            data = date
        else:
            data=[]
            for item in date:
                if criteriu in (1,2,3,6):
                    if introdus.lower() in item[criteriu].lower():
                        data.append(item)
                else:
                    
                    if int(introdus)==item[criteriu]:
                        
                        data.append(item)
        
        actualizare(data)

    

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
    
    


    actualizare(date)
    lista.bind("<Return>",golire)

    caseta.bind("<Return>",verificare)
    result=StringVar()
    def preluare_element(event):
        selectat = event.widget.curselection()
        index = selectat[0]
        value = event.widget.get(index)
  
        result.set(value)
        print(value)


    lista.bind('<<ListboxSelect>>', preluare_element)

    window.mainloop()


def inserare():
    geam=Tk()
    geam.resizable(1,1)
    geam.geometry('800x600')
    geam.title("Adaugare")






    # fereastra adaugare carti
    
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



#FEREASTRA PRINCIPALA

root=Tk()
root.geometry('1920x1080')

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

imprumut=Button(frame1,text="Carti imprumutate",width=80,height=6, bg="#F5EBE0",font=("Cambria_Math",15))
imprumut.place(relx=0,rely=0,anchor=NW,)

carti=Button(frame1,text="Lista carti",width=80,height=6,bg="#F5EBE0",font=("Cambria_Math",15),command=search)
carti.place(relx=0,rely=0.5,anchor=W,)

elevi=Button(frame1,text="Lista elevi",width=80,height=6,bg="#F5EBE0",font=("Cambria_Math",15))
elevi.place(relx=0,rely=1,anchor=SW)



#buton_cautare=Button(frame2,text="Cautare",command=search)
#buton_cautare.pack( ipadx=50, ipady=50)





root.mainloop()