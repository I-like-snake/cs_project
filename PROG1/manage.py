from tkinter import *
from PIL import ImageTk
from spare2 import hello
from delete import dele
from show_data import show
def man():
     menu = Toplevel()
     menu.title("Menu")
     menu.geometry("750x500+200+200")

     bgim= ImageTk.PhotoImage(file="download.jpg")
     back= Label(menu, image=bgim).place(x=0,y=0)
     p1 = ImageTk.PhotoImage(file = 'menu.png')
     menu.iconphoto(False, p1)                          
     #canvas = Canvas(menu, width=300, height=460, bg="lime")
     #canvas.place(x=70,y=30)
     #lab= Label(menu, text=" MAIN MENU " , font=("agency fb",35,"bold")).place(x=60, y=30)
     but1= Button(menu, text="Create",fg="black",command=hello ,bd=5,font=("agency fb" ,25,"bold"))
     but1.place(x=260, y=160,width=200)
     but1= Button(menu, text="Update", fg="Black",bd=5, font=("agency fb" ,25,"bold"))
     but1.place(x=260, y=240,width=200)
     but1= Button(menu, text="Delete",  fg="black",bd=5,command=dele, font=("agency fb" ,25,"bold"))
     but1.place(x=260, y=320,width=200)
     but1= Button(menu, text="Show Data", command=show,fg="black",bd=5, font=("agency fb" ,20,"bold"))
     but1.place(x=260, y=400,width=200)
     

     menu.mainloop()
