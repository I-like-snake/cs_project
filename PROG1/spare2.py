from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
def hello():
        
    class Employee:
        def __init__(self,root):
            self.root=root
            self.root.title("Employee Database Management")
            self.root.geometry("1370x750+100+20")
            root.resizable(False,False)

            firstLabel= Label(self.root, bd=20, relief= RIDGE, text="EMPLOYEE MANAGEMENT DATABASE", fg="black", bg="cyan", font=("consolas",30,"bold"))
            firstLabel.pack(side=TOP, fill=X)




    #============================DATAFRAME===================================================================
            dataframe= Frame(self.root, bd=20, bg="yellow",relief=RIDGE)
            dataframe.place(x=0, y=90, width=1370, height=400)

            dataframeleft= LabelFrame(dataframe,bd=10, relief=RIDGE, padx=10,
                                      font=('consolas',13,'bold'), text="Employee Information")
            dataframeleft.place(x=0, y=5, width=980, height=350)

            dataframeright= LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10,
                                      font=('consolas',13,'bold'), text="Prescription")
            dataframeright.place(x=984, y=5, width=345, height=350)

            l1= Label(dataframeright,text="Name :", font=("agency fb",17,"bold"), padx=10)
            l1.grid(row=0,column=0)
            l2= Label(dataframeright,text="Email :", font=("agency fb",17,"bold"), padx=10)
            l2.grid(row=2,column=0)
            l3= Label(dataframeright,text="Phone :", font=("agency fb",17,"bold"), padx=10)
            l3.grid(row=3,column=0)
            l4= Label(dataframeright,text="Age :", font=("agency fb",17,"bold"), padx=10)
            l4.grid(row=4,column=0)
            l5= Label(dataframeright,text="Employee No :", font=("agency fb",17,"bold"), padx=10)
            l5.grid(row=5,column=0)
            l6= Label(dataframeright,text="Salary :", font=("agency fb",17,"bold"), padx=10)
            l6.grid(row=6,column=0)
            l7= Label(dataframeright,text="DOB :", font=("agency fb",17,"bold"), padx=10)
            l7.grid(row=7,column=0)
            l8= Label(dataframeright,text="Qualification :", font=("agency fb",17,"bold"), padx=10)
            l8.grid(row=8,column=0)
            l9= Label(dataframeright,text="Designation :", font=("agency fb",17,"bold"), padx=10)
            l9.grid(row=9,column=0)

    #========================buttons=======================================================

            buttonframe= Frame(self.root, bd=13, bg="lime",relief=RIDGE)
            buttonframe.place(x=0, y=486, width=1368, height=75)
    #fv=========================================================================================

    #===========================detailframeleft===============================================

            labelnamefname= Label(dataframeleft, font=("consolas",13,"bold"), text="First Name",padx=2, pady=8)
            labelnamefname.grid(row=0, column=0, sticky=W)
            entrynamefname= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entrynamefname.grid(row=0, column=1)
            

            labelnamelname= Label(dataframeleft, font=("consolas",13,"bold"), text="Last Name",padx=2, pady=8)
            labelnamelname.grid(row=1, column=0, sticky=W)
            entrynamelname= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entrynamelname.grid(row=1, column=1)
            

            labelemail= Label(dataframeleft, font=("consolas",13,"bold"), text="Email-ID",padx=2, pady=8)
            labelemail.grid(row=2, column=0, sticky=W)
            entryemail= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entryemail.grid(row=2, column=1)
            

            labelphone= Label(dataframeleft, font=("consolas",13,"bold"), text="Phone",padx=2, pady=8)
            labelphone.grid(row=3, column=0, sticky=W)
            entryphone= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entryphone.grid(row=3, column=1)
            

            labelage= Label(dataframeleft, font=("consolas",13,"bold"), text="Age",padx=2, pady=8)
            labelage.grid(row=4, column=0, sticky=W)
            entryage= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entryage.grid(row=4, column=1)
            

            labelempno= Label(dataframeleft, font=("consolas",13,"bold"), text="Employee No.",padx=2, pady=8)
            labelempno.grid(row=5, column=0, sticky=W)
            entryempno= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entryempno.grid(row=5, column=1)
        

            labelsalary= Label(dataframeleft, font=("consolas",13,"bold"), text="Salary",padx=2, pady=8)
            labelsalary.grid(row=6, column=0, sticky=W)
            entrysalary= Entry(dataframeleft, font=("consolas",13,"bold"), width=32, bd=2)
            entrysalary.grid(row=6, column=1)
            
    #==================================right==============================================


            labeldob = Label(dataframeleft, text="DOB", font=('consolas',13, "bold"),padx=15, pady=8)
            labeldob.grid(row=0, column=3, sticky=W)
            box1= ttk.Combobox(dataframeleft,font=("consolas",13, "bold"), width=7)
            box1["values"]=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                            "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30", "31")
            box1.set("Date")
            box1.place(x=560,y=10)

            box2= ttk.Combobox(dataframeleft,font=("consolas",13, "bold"), width=7)
            box2["values"]=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
            box2.set("Month")
            box2.place(x=660,y=10)
                
            box3= ttk.Combobox(dataframeleft,font=("consolas",13, "bold"),width=7)
            l = []
            for i in range(1949,2004):
                 l.append(str(i+1))
            t = tuple(l)
            box3["values"]=t
            box3.set("Year")
            box3.place(x=770,y=10)
            
            
            labeljoindate = Label(dataframeleft, font=("consolas",13, "bold"), text="Joining Date", padx=15, pady=8)
            labeljoindate.grid(row=4, column=3, sticky=W)
            entryjoindate = Entry(dataframeleft, font=("consolas",13, "bold"), width=32, bd=2)
            entryjoindate.grid(row=4, column=4)
            

            labelqualifications = Label(dataframeleft, font=("consolas",13, "bold"), text="Qualification", padx=15, pady=8)
            labelqualifications.grid(row=1, column=3, sticky=W)
            entryqualifications = Entry(dataframeleft, font=("consolas",13, "bold"), width=32, bd=2)
            entryqualifications.grid(row=1, column=4)
            

            labeldesig = Label(dataframeleft, font=("consolas",13, "bold"), text="Designation", padx=15, pady=8)
            labeldesig.grid(row=2, column=3, sticky=W)
            entrydesig = Entry(dataframeleft, font=("consolas",13, "bold"), width=32, bd=2)
            entrydesig.grid(row=2, column=4)
            

            labelschedule = Label(dataframeleft, font=("consolas",13, "bold"), text="Schedule", padx=15, pady=8)
            labelschedule.grid(row=3, column=3, sticky=W)
            entryschedule = Entry(dataframeleft, font=("consolas",13, "bold"), width=32, bd=2)
            entryschedule.grid(row=3, column=4)
            

            labeladdress = Label(dataframeleft, font=("consolas",13, "bold"), text="Address", padx=15, pady=8)
            labeladdress.grid(row=5, column=3, sticky=W)
            entryaddress = Text(dataframeleft, state=DISABLED,font=("consolas",13, "bold"), width=32, height=4, bd=3)
            entryaddress.place(x=560,y=210)

    #========================================Dataframeright======================================================================
            '''self.txtPrescripion= Text(dataframeright, font=("consolas",13,"bold"), width=34, height=15, padx=0, pady=2)
            self.txtPrescripion.grid(row=0, column=0)'''
    #===========================================Defining=========================================================================
            def insert():
                import mysql.connector as sql
                mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
                cursor=mycon.cursor()

                fnameget= entrynamefname.get()
                lnameget = entrynamelname.get()
                emailget= entryemail.get()
                getphone = entryphone.get()
                ageget = entryage.get()
                empnoget = entryempno.get()
                salaryget = entrysalary.get()
                box1get = box1.get()
                box2get = box2.get()
                box3get = box3.get()
                dobget= box1get+"-"+box2get+"-"+box3get
                joindateget= entryjoindate.get()
                qualificationsget = entryqualifications.get()
                desigget = entrydesig.get()
                scheduleget = entryschedule.get()
                addressget=entryaddress.get("1.0","end-1c")

                sql = "INSERT INTO emp(fname,lname,email,phone,age,enpno,salary,dob,joindate,qual,desig,schedule) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (fnameget,lnameget,emailget, getphone, ageget, empnoget, salaryget, dobget, joindateget, qualificationsget,
                        desigget, scheduleget)
                cursor.execute(sql, val)
                mycon.commit()

            def exxit():

                win= Tk()
                win.geometry("250x90+540+320")
                win.title("Warning!")
                def adios():
                    self.root.destroy()
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

            root.bind('<Escape>', lambda event: exxit())

            def pres():
                
                fnameget= entrynamefname.get()
                lnameget = entrynamelname.get()
                name=fnameget+""+lnameget
                emailget= entryemail.get()
                getphone = entryphone.get()
                ageget = entryage.get()
                box1get = box1.get()
                box2get = box2.get()
                box3get = box3.get()
                dobget= box1get+"-"+box2get+"-"+box3get
                empnoget = entryempno.get()
                salaryget = entrysalary.get()
                joindateget= entryjoindate.get()
                qualificationsget = entryqualifications.get()
                desigget = entrydesig.get()
                scheduleget = entryschedule.get()

                l1= Label(dataframeright,text=name, font=("agency fb",17,"bold"), padx=10)
                l1.grid(row=0,column=1)
                l2= Label(dataframeright,text=emailget, font=("agency fb",17,"bold"), padx=10)
                l2.grid(row=2,column=1)
                l3= Label(dataframeright,text=getphone, font=("agency fb",17,"bold"), padx=10)
                l3.grid(row=3,column=1)
                l4= Label(dataframeright,text=ageget, font=("agency fb",17,"bold"), padx=10)
                l4.grid(row=4,column=1)
                l5= Label(dataframeright,text=empnoget, font=("agency fb",17,"bold"), padx=10)
                l5.grid(row=5,column=1)
                l6= Label(dataframeright,text=salaryget, font=("agency fb",17,"bold"), padx=10)
                l6.grid(row=6,column=1)
                l7= Label(dataframeright,text=dobget, font=("agency fb",17,"bold"), padx=10)
                l7.grid(row=7,column=1)
                l8= Label(dataframeright,text=qualificationsget, font=("agency fb",17,"bold"), padx=10)
                l8.grid(row=8,column=1)
                l9= Label(dataframeright,text=desigget, font=("agency fb",17,"bold"), padx=10)
                l9.grid(row=9,column=1)

            def clear_text():
                entrynamefname.delete(0, END)
                entrynamelname.delete(0, END)
                entryemail.delete(0, END)
                entryphone.delete(0, END)
                entryage.delete(0, END)
                entryempno.delete(0, END)
                entrysalary.delete(0, END)
                box1.delete(0, END)
                box2.delete(0, END)
                box3.delete(0, END)
                entryjoindate.delete(0, END)
                entryqualifications.delete(0, END)
                entrydesig.delete(0, END)
                entryschedule.delete(0, END)
                entryaddress.delete("1.0","end")
            def gettheno():
                mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
                cursor=mycon.cursor()
                a="select count(*) from emp"
                cursor.execute(a)
                x=cursor.fetchall()
                noofemp= len(x)+1
                print(noofemp)

            buttonx= Button(dataframeleft, text="NEW",width=8, font=("consolas",10,"bold"),command=gettheno).grid(row=5, column=3, sticky=W)    
    #===============================================BUTTONS====================================================================
            button1= Button(buttonframe,text="Prescription", command=pres,font=("consolas",15,"bold"),bg="lime", width=30, height=1, padx=2, pady=6)
            button1.grid(row=0, column=0)

            button1= Button(buttonframe, text="Insert Data", font=("consolas",15,"bold"),bg="lime", width=30, height=1,
                            command=insert,padx=2, pady=6)
            button1.grid(row=0, column=1)

            #button1= Button(buttonframe, text="Update", font=("consolas",13,"bold"),bg="lime", width=24, height=1, padx=2, pady=6)
            #button1.grid(row=0, column=2)

            #button1= Button(buttonframe, text="Delete", font=("consolas",13,"bold"),bg="lime", width=23, height=1, padx=2, pady=6)
            #button1.grid(row=0, column=3)

            button1= Button(buttonframe, text="Clear", command=clear_text,font=("consolas",15,"bold"),bg="lime", width=30, height=1, padx=2, pady=6)
            button1.grid(row=0, column=4)

            button1= Button(buttonframe, text="Exit",font=("consolas",15,"bold"),command=exxit,bg="lime", width=28, height=1, padx=2, pady=6)
            button1.grid(row=0, column=5)

    #=====================================scrollbar=====================================================================================
    


    root= Tk()
    ob= Employee(root)
    root.mainloop()











