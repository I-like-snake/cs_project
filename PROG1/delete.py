import tkinter.ttk as ttk 
from tkinter import *
import mysql.connector as sql
def dele():
     root= Tk()
     root.geometry("450x600+300+20")
     root.title("Deleting Details")
     mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
     cursor=mycon.cursor()
     cursor.execute("select * from emp")
     ent1= Entry(root, bd=5, width=14, font=("agency fb",29))
     cursor.fetchall()

     def delete1():
          import mysql.connector as sql
          mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
          cursor=mycon.cursor()
          item=ent1.get()
          s= "delete from emp where enpno='{}';".format(item)
          cursor.execute(s)
          mycon.commit()
          mycon.close()

     label= Label(root, text="    DELETING SECTION    ",bg="white",relief=RIDGE,bd=11,font=("agency fb", 35,"bold"))
     btn1= Button(root, bd=5, text="DEL",command=delete1,font=("consolas",19,"bold"),padx=1, pady=1)
     #=================================table========================================================
     canva = LabelFrame(root,bd=10, bg="lime",relief=RIDGE)
     canva.place(x=50,y=240)
     style  = ttk.Style()
     style.configure("Treeview.Heading", font=("agency fb",16,"bold"))
     tree = ttk.Treeview(canva)
     tree["columns"] = ("fn", "ln","empno")
     tree.column("fn", width=120)
     tree.column("ln", width=120)
     tree.column("empno", width=60)
     tree.heading("#0", text='ID')
     tree.column("#0", width=30)
     tree.heading("fn", text="First Name")
     tree.heading("ln", text="Last Name")
     tree.heading("empno", text="Emp.No")
     cursor.execute("select * from emp;")
     l = cursor.fetchall()
     cpt = 0
     for r in l:
         tree.insert('', 'end', text=str(cpt), values=(r[0],r[1], r[5]))
         cpt += 1
     #===============================================================================================        
     tree.pack()
     label.place(x=35,y=30)
     btn1.place(x=342,y=130)
     ent1.place(x=90,y=130)

     def refresh():
          import mysql.connector as sql
          
          mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
          cursor=mycon.cursor()
          #=================================table========================================================
          canva = LabelFrame(root,bd=10, bg="lime",relief=RIDGE)
          canva.place(x=50,y=240)
          style  = ttk.Style()
          style.configure("Treeview.Heading", font=("agency fb",16,"bold"))
          tree = ttk.Treeview(canva)
          tree["columns"] = ("fn", "ln","empno")
          tree.column("fn", width=120)
          tree.column("ln", width=120)
          tree.column("empno", width=60)
          tree.heading("#0", text='ID')
          tree.column("#0", width=30)
          tree.heading("fn", text="First Name")
          tree.heading("ln", text="Last Name")
          tree.heading("empno", text="Emp.No")
          cursor.execute("select * from emp;")
          l = cursor.fetchall()
          cpt = 0
          for r in l:
              tree.insert('', 'end', text=str(cpt), values=(r[0],r[1], r[5]))
              cpt += 1
          #===============================================================================================        
          tree.pack()
     def exitwin():
          win= Tk()
          win.geometry("250x90+540+320")
          win.title("Warning!")
          def adios():
              root.destroy()
              win.destroy()
          def na():
              win.destroy()
          lab= Label(win, text="Do you want", font=("consolas",12,"bold")).pack()
          lab= Label(win, text="to Exit the Table", font=("consolas",12,"bold")).pack()
          but1= Button(win, text="Yes", fg="white",command=adios,bg="sky blue",font=("agency fb",14,"bold"),padx=47)
          but1.pack(side=LEFT)
          but2= Button(win, text="No", fg="white", bg="Red",command=na,font=("agency fb",14,"bold"),padx=50)
          but2.pack(side=LEFT)
     btn2= Button(root, bd=5, text="↻",command=refresh,font=("consolas",19,"bold"),padx=2, pady=1)
     btn2.place(x=10,y=510)
     btn3= Button(root, bd=5, fg="red",text="Exit",command=exitwin ,font=("agency fb",22,"bold"),padx=20, pady=1)
     btn3.place(x=350,y=510)
     mycon.close()


     root.mainloop()
