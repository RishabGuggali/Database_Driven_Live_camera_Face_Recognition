import psycopg2

#connect to the db
con = psycopg2.connect(
            #host = " ",
            database="Sample",
            user = "postgres",
            password = "rishab")

#cursor
cur = con.cursor()



#execute query
cur.execute("insert into Users values('Bill Gates','Bill Gates.jpg') ")
cur.execute("insert into Users values('Elon musk','Elon musk.jpg') ")
cur.execute("insert into Users values('Mark zukerberg','mark zukerberg.jpg') ")
cur.execute("insert into Users values('Sunder pichai','Sunder pichai.jpg') ")

#cur.execute("delete from Users where name ='Narendra Modi' ")
cur.execute("select * from Users")
rows = cur.fetchall()
print("Name         |      Image")
for r in rows:

    print("_"*30)
    print (r[0]+"       |      "+r[1])

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()