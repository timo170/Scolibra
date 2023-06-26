import requests
import json
import mysql.connector
#conectare la baza de date
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="BIBLIOTECA"
)
cursor=mydb.cursor()



q="Select * from cartile;"
cursor.execute(q)
result=cursor.fetchall()
   
date=[]
for rand in result: #conversia rezultatelor in dictionare
    id=rand[0]
    sql=f"Select Count(Cod) from carticod where Id={id} and Stare='liberă';"
    cursor.execute(sql)
    result=cursor.fetchone()
    nr=result[0]
    thisdict={'Id':rand[0], 'Autor':rand[1], 'Titlu':rand[2], 'Editura':rand[3], 'An':rand[4],'Nr':nr}
    date.append(thisdict)
#date este o lista de dictionare
    


res=requests.post(url='https://scolibra.000webhostapp.com/insertdata.php',json=date[44])
print(res)
