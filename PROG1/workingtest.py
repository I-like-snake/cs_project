from tkinter import *

root = Tk()
e1= Entry(root, width=10,bd=5)
e2= Entry(root, width=10,bd=5)
e3= Entry(root, width=10,bd=5)
e1.pack()
e2.pack()
e3.pack()

def ll():
     import mysql.connector as sql
     mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
     cursor=mycon.cursor()
     a=e1.get()
     b=e2.get()
     c=e3.get()
     sql = "INSERT INTO  new1(id,name,marks) VALUES (%s, %s, %s)"
     val = (a,b,c)
     cursor.execute(sql, val)
     mycon.commit()


but = Button(root, command=ll, text="Submit").pack()
root.mainloop()
