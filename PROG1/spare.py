from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql
#def hello():
    
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database Management")
        self.root.geometry("1530x700+0+0")


        firstLabel= Label(self.root, bd=20, relief= RIDGE, text="EMPLOYEE MANAGEMENT DATABASE", fg="black", bg="cyan", font=("consolas",30,"bold"))
        firstLabel.pack(side=TOP, fill=X)

        self.labelnamefname = StringVar()
        self.labelnamelname = StringVar()
        self.labelphone = StringVar()
        self.labelempno = StringVar()
        self.labeldesig = StringVar()
        self.labelemail = StringVar()
        self.labeladdress = StringVar()
        self.labelsalary = StringVar()
        self.labelage = StringVar()
        self.labeldob = StringVar()
        self.labeljoindate = StringVar()
        self.labelqualifications = StringVar()
        self.labelschedule = StringVar()


#============================DATAFRAME===================================================================
        dataframe= Frame(self.root, bd=20, bg="yellow",relief=RIDGE)
        dataframe.place(x=0, y=90, width=1370, height=400)

        dataframeleft= LabelFrame(dataframe,bd=10, relief=RIDGE, padx=10,
                                  font=('consolas',13,'bold'), text="Employee Information")
        dataframeleft.place(x=0, y=5, width=980, height=350)
        dataframeright= LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=('consolas',13,'bold'), text="Prescription")
        dataframeright.place(x=984, y=5, width=345, height=350)

#========================buttomns=======================================================

        buttonframe= Frame(self.root, bd=13, bg="lime",relief=RIDGE)
        buttonframe.place(x=0, y=486, width=1368, height=75)
#fv=========================================================================================

#===========================detailframeleft===============================================

        labelnamefname= Label(dataframeleft, font=("consolas",13,"bold"), text="First Name",padx=2, pady=8)
        labelnamefname.grid(row=0, column=0, sticky=W)
        entrynamefname= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelnamefname, width=32, bd=2)
        entrynamefname.grid(row=0, column=1)
        fnameget= entrynamefname.get()

        labelnamelname= Label(dataframeleft, font=("consolas",13,"bold"), text="Last Name",padx=2, pady=8)
        labelnamelname.grid(row=1, column=0, sticky=W)
        entrynamelname= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelnamelname, width=32, bd=2)
        entrynamelname.grid(row=1, column=1)
        lnameget = entrynamelname.get()

        labelemail= Label(dataframeleft, font=("consolas",13,"bold"), text="Email-ID",padx=2, pady=8)
        labelemail.grid(row=2, column=0, sticky=W)
        entryemail= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelemail, width=32, bd=2)
        entryemail.grid(row=2, column=1)
        emailget= entryemail.get()

        labelphone= Label(dataframeleft, font=("consolas",13,"bold"), text="Phone",padx=2, pady=8)
        labelphone.grid(row=3, column=0, sticky=W)
        entryphone= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelphone, width=32, bd=2)
        entryphone.grid(row=3, column=1)
        getphone = entryphone.get()

        labelage= Label(dataframeleft, font=("consolas",13,"bold"), text="Age",padx=2, pady=8)
        labelage.grid(row=4, column=0, sticky=W)
        entryage= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelage, width=32, bd=2)
        entryage.grid(row=4, column=1)
        ageget = entryage.get()

        labelempno= Label(dataframeleft, font=("consolas",13,"bold"), text="Employee No.",padx=2, pady=8)
        labelempno.grid(row=5, column=0, sticky=W)
        entryempno= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelempno, width=32, bd=2)
        entryempno.grid(row=5, column=1)
        empnoget = entryempno.get()
        #buttonx= Button(dataframeleft, text="NEW",width=8, font=("consolas",10,"bold")).grid(row=5, column=3, sticky=W)

        labelsalary= Label(dataframeleft, font=("consolas",13,"bold"), text="Salary",padx=2, pady=8)
        labelsalary.grid(row=6, column=0, sticky=W)
        entrysalary= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelsalary, width=32, bd=2)
        entrysalary.grid(row=6, column=1)
        salaryget = entrysalary.get()
#==================================right==============================================


        labeldob = Label(dataframeleft, text="DOB", font=('consolas',13, "bold"), textvariable=self.labeldob,padx=15, pady=8)
        labeldob.grid(row=0, column=3, sticky=W)
        entrydob = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labeljoindate, width=32, bd=2)
        entrydob.grid(row=0, column=4)
        dobget = entrydob.get()
        
        labeljoindate = Label(dataframeleft, font=("consolas",13, "bold"), text="Joining Date", padx=15, pady=8)
        labeljoindate.grid(row=1, column=3, sticky=W)
        entryjoindate = Entry(dataframeleft, font=("consolas",13, "bold"), width=32, bd=2)
        entryjoindate.grid(row=1, column=4)
        joindateget= entryjoindate.get()

        labelqualifications = Label(dataframeleft, font=("consolas",13, "bold"), text="Qualification", padx=15, pady=8)
        labelqualifications.grid(row=2, column=3, sticky=W)
        entryqualifications = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labelqualifications, width=32, bd=2)
        entryqualifications.grid(row=2, column=4)
        qualificationsget = entryqualifications.get()

        labeldesig = Label(dataframeleft, font=("consolas",13, "bold"), text="Designation", padx=15, pady=8)
        labeldesig.grid(row=3, column=3, sticky=W)
        entrydesig = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labeldesig, width=32, bd=2)
        entrydesig.grid(row=3, column=4)
        desigget = entrydesig.get()

        labelschedule = Label(dataframeleft, font=("consolas",13, "bold"), text="Schedule", padx=15, pady=8)
        labelschedule.grid(row=4, column=3, sticky=W)
        entryschedule = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labelschedule, width=32, bd=2)
        entryschedule.grid(row=4, column=4)
        scheduleget = entryschedule.get()

        labeladdress = Label(dataframeleft, font=("consolas",13, "bold"), text="Address", padx=15, pady=8)
        labeladdress.grid(row=6, column=3, sticky=W)
        entryaddress = Text(dataframeleft, font=("consolas",13, "bold"), width=32, height=3, bd=3)
        entryaddress.grid(row=6, column=4)

#========================================Dataframeright======================================================================
        self.txtPrescripion= Text(dataframeright, font=("consolas",13,"bold"), width=34, height=15, padx=0, pady=2)
        self.txtPrescripion.grid(row=0, column=0)
#===========================================Defining=========================================================================
        def insert():
            import mysql.connector as sql
            mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
            cursor=mycon.cursor()
            sql = "INSERT INTO emp(fname,lname,email,phone,age,enpno,salary,dob,joindate,qual,desig,schedule) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (fnameget,lnameget,emailget, getphone, ageget, empnoget, salaryget, dobget, joindateget, qualificationsget,
                    desigget, scheduleget)
            cursor.execute(sql, val)
            mycon.commit()

        def exxit():
            self.root.destroy()

        def clear_text():
            entrynamefname.delete(0, END)
            entrynamelname.delete(0, END)
            entryemail.delete(0, END)
            entryphone.delete(0, END)
            entryage.delete(0, END)
            entryempno.delete(0, END)
            entrysalary.delete(0, END)
            entrydob.delete(0, END)
            entryjoindate.delete(0, END)
            entryqualifications.delete(0, END)
            entrydesig.delete(0, END)
            entryschedule.delete(0, END)
            entryaddress.delete("1.0","end")

#===============================================BUTTONS====================================================================
        button1= Button(buttonframe,text="Prescription", font=("consolas",15,"bold"),bg="lime", width=30, height=1, padx=2, pady=6)
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










