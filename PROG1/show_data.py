import tkinter.ttk as ttk 
import mysql.connector as sql
from tkinter import *
def show():
    root = Tk()
    root.title("DataBase")
    root.geometry("1200x400")
    root['background']="grey"
    lab= Label(root, relief=RIDGE, bd=7,text="  Database Table  ", fg="black",bg="grey",font=("agency fb",40,"bold")).place(x=450,y=10)
    canva = LabelFrame(root,bd=10, bg="white",relief=RIDGE)
    canva.place(x=50,y=100)
    tree = ttk.Treeview(canva)
    tree["columns"] = ("fn", "ln", "mail","no","age","empno","sal","dob","doj","qua","des","sch")
    tree.column("fn", width=70)
    tree.column("ln", width=70)
    tree.column("mail", width=150)
    tree.column("no", width=70)
    tree.column("age", width=50)
    tree.column("empno", width=50)
    tree.column("sal", width=50)
    tree.column("dob", width=100)
    tree.column("doj", width=100)
    tree.column("qua", width=150)
    tree.column("des", width=100)
    tree.column("sch", width=70)

    tree.heading("#0", text='ID')
    tree.column("#0", width=30)
    tree.heading("fn", text="First Name")
    tree.heading("ln", text="Last Name")
    tree.heading("mail", text="E-mail")
    tree.heading("no", text="Phone")
    tree.heading("age", text="Age")
    tree.heading("empno", text="Emp NO.")
    tree.heading("sal", text="Salary")
    tree.heading("dob", text="DOB")
    tree.heading("doj", text="DOJ")
    tree.heading("qua", text="Qualification")
    tree.heading("des", text="Designation")
    tree.heading("sch", text="Schedule")

    con = sql.connect(host='localhost',user='root',passwd='tiger',database='test')
    cur = con.cursor()
    cur.execute("select * from emp;")
    l = cur.fetchall()
    cpt = 0
    for r in l:
        tree.insert('', 'end', text=str(cpt), values=(r[0],r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]))
        cpt += 1
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
              root.bind('<y>', lambda event: adios())
              root.bind('<n>', lambda event: na())
    #exitbut= Button(root, text="Exit",font=("",20,"bold"), bg="red",fg="black",command=exitwin).place(x=1050,y=350)
    root.bind('<Escape>', lambda event: exitwin())
    tree.pack()
    root.mainloop()