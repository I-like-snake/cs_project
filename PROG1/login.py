from tkinter import *
from PIL import ImageTk
from manage import man

root= Tk()
root.geometry("800x550")
root.title("LOGIN")
bg= ImageTk.PhotoImage(file="download (1).png")
back= Label(root, image=bg).place(x=0,y=0)
p1 = ImageTk.PhotoImage(file = 'wallpaperflare-cropped.jpg')
root.iconphoto(False, p1)

def on_button():
     username=ent1.get()
     password=ent2.get()

     if username=='root' and password=='management':
          button1= Button(root, text="Login",font=("agency fb", 20), width=10, height=1,command=man)
          button1.place(x=650, y=450)
          #root.after(3000, lambda:root.destroy())
          root.bind('<Return>', lambda event: man())
     if username=="root":
          pass
     else:
          lab1= Label(root, text="Invalid Username",font=("agency fb", 20,"bold")).place(x=330,y=370)
          print("invalid")

     if password=="management":
          labe= Label(root, text=" WELCOME ! ", font=("agency fb",20,"bold")).place(x=330 ,y=420)

     else:
          lab2= Label(root, text="Invalid Password",font=("agency fb", 20,"bold")).place(x=330,y=370)
          print("invalid")
def exxit():
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

ent1= Entry(root, bd=5, font=("agency fb", 27),width=15)
ent2= Entry(root, bd=5, font=("agency fb", 27),width=15, show="*")
but= Button(root, text="Check Me!",font=("agency fb", 20), width=10, height=1,command=on_button)
but1= Button(root, text="EXIT", font=("agency fb",25,"bold"),command=exxit, fg="white",bg="red")
but1.place(x=50, y=450, height=60, width=75)
ent1.place(x=330,y=166)
ent2.place(x=330,y=285)
but.place(x=650, y=450)
root.bind('<Escape>',lambda event:exxit())
root.bind('<Return>',lambda event:on_button())
root.mainloop()
