from tkinter import *
import tkinter.ttk as ttk
import mysql.connector as sql
#from updatepage import *
root= Tk()
root.title("Update")
root.geometry("400x500+300+20")
mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
cursor=mycon.cursor()
lab= Label(root, text="  UPDATING  ", font=("agency fb",40,"bold"), relief=RIDGE, bd=7,bg="purple",fg="white")
lab.place(x=90,y=10)
ent1= Entry(root, bd=5, width=14, font=("agency fb",29))
ent1.place(x=60,y=130)

#================================table=============================================================
canva = LabelFrame(root,bd=10, bg="lime",relief=RIDGE)
canva.place(x=25,y=220,height=200)
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
tree.pack()
#===============================================================================================        
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
    root.bind('<y>',lambda event:adios())
    root.bind('<n>',lambda event:na())

but2= Button(root, text="Edit",font=("agency fb",20,"bold"), bd=5)
but2.place(x=310,y=129, height=58,width=60)
btn3= Button(root, bd=5, fg="red",text="Exit",command=exitwin ,font=("agency fb",22,"bold"),padx=20, pady=1)
btn3.place(x=300,y=430,height=56)
root.bind('<Escape>',lambda event:exitwin())
#root.bind('<Return>',lambda event:on_button())
root.mainloop()
