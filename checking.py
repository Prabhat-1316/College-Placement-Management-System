def addstudent():
    def submitadd():
        usn = idval.get()
        name = nameval.get()
        phone_no = mobileval.get()
        placed_status = statusval.get()
        comp_name = compNameval.get()
        # addedtime = time.strftime("%H:%M:%S")
        # addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into STUDENT1 values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (usn, name, phone_no, placed_status, comp_name))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'id {} name {} Added successfully.. and want to clear the form'.format(usn, name), parent=addroot)

            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                statusval.set('')
                compNameval.set('')
        except:
            messagebox.showerror('Notifications','Id Already exits try another id...',parent=addroot)
        strr = 'select *from student1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4]]
            studenttable.insert('',END,values=vv)


    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+100')
    addroot.title('Adding Details')
    addroot.config(bg='blue')
    addroot.iconbitmap('ico image.ico')
    addroot.resizable(False,False)
    #--------add student label------------
    idlabel = Label(addroot,text='Enter USN: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    moblabel = Label(addroot,text='Enter Mobile: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel.place(x=10,y=130)

    statuslabel = Label(addroot,text='Placed Status: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    statuslabel.place(x=10,y=190)

    compNamelabel = Label(addroot,text='Company Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    compNamelabel.place(x=10,y=250)

    ##-----add student entry--------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    statusval = StringVar()
    compNameval = StringVar()

    identry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    statusentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=statusval)
    statusentry.place(x=250,y=190)

    compNameentry = Entry(addroot,font=('arial',15,'bold'),bd=5,textvariable=compNameval)
    compNameentry.place(x=250,y=250)

    ####--------add button----------
    submitbtn = Button(addroot,text='Submit',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue'
                       ,activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)
  

    addroot.mainloop()


def searchstudent():
    def search():
        usn = idval.get()
        name = nameval.get()
        phone_no = mobileval.get()
        placed_status = statusval.get()
        comp_name = compNameval.get()
        if(id != ''):
            strr = 'select *from student1 where usn = %s'
            mycursor.execute(strr,(usn))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4]]
                studenttable.insert('',END,values=vv)
        
        if(name != ''):
            strr = 'select *from student1 where name = %s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4]]
                studenttable.insert('',END,values=vv)

        if(phone_no != ''):
            strr = 'select *from student1 where phone_no = %s'
            mycursor.execute(strr,(phone_no))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4]]
                studenttable.insert('',END,values=vv)

        if(placed_status != ''):
            strr = 'select *from student1 where placed_status = %s'
            mycursor.execute(strr,(placed_status))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4]]
                studenttable.insert('',END,values=vv)

        if(comp_name != ''):
            strr = 'select *from student1 where comp_name = %s'
            mycursor.execute(strr,(comp_name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4]]
                studenttable.insert('',END,values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+100')
    searchroot.title('Searching Details')
    searchroot.config(bg='light blue')
    searchroot.iconbitmap('ico image.ico')
    searchroot.resizable(False,False)
    #--------add student label------------
    idlabel = Label(searchroot,text='Enter USN: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    moblabel = Label(searchroot,text='Enter Mobile: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel.place(x=10,y=130)

    statuslabel = Label(searchroot,text='Placed Status: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    statuslabel.place(x=10,y=190)

    compNamelabel = Label(searchroot,text='Company Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    compNamelabel.place(x=10,y=250)

    ##-----add student entry--------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    statusval = StringVar()
    compNameval = StringVar()

    identry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    statusentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=statusval)
    statusentry.place(x=250,y=190)

    compNameentry = Entry(searchroot,font=('arial',15,'bold'),bd=5,textvariable=compNameval)
    compNameentry.place(x=250,y=250)

    ####--------add button----------
    searchbtn = Button(searchroot,text='Search',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue'
                       ,activeforeground='white',bg='red',command=search)
    searchbtn.place(x=150,y=420)
  

    searchroot.mainloop()


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)  # where we have clicked in list of student
    pp = content['values'][0]  # to store primary key
    strr = 'delete from student1 where USN=%s '
    mycursor.execute(strr,(pp))
    con.commit  # update the list
    messagebox.showinfo('Notifications','Deleted successfully...')

    strr = 'select *from student1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4]]
        studenttable.insert('',END,values=vv)


def updatestudent():
    def update():
        usn = idval.get()
        name = nameval.get()
        phone_no = mobileval.get()
        placed_status = statusval.get()
        comp_name = compNameval.get()

        strr = 'update student1 set name=%s,phone_no=%s,placed_status=%s,comp_name=%s where usn=%s'
        mycursor.execute(strr,(name,phone_no,placed_status,comp_name,usn))
        con.commit()

        messagebox.showinfo('Notifications','Modified successfully')
        strr = 'select *from student1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4]]
            studenttable.insert('',END,values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x500+220+100')
    updateroot.title('Updating Details')
    updateroot.config(bg='light green')
    updateroot.iconbitmap('ico image.ico')
    updateroot.resizable(False,False)

    #--------add student label------------
    idlabel = Label(updateroot,text='Enter USN: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    moblabel = Label(updateroot,text='Enter Mobile: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    moblabel.place(x=10,y=130)

    statuslabel = Label(updateroot,text='Placed Status: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    statuslabel.place(x=10,y=190)

    compNamelabel = Label(updateroot,text='Company Name: ',bg='gold2',font=('arial',18,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    compNamelabel.place(x=10,y=250)

    ##-----add student entry--------
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    statusval = StringVar()
    compNameval = StringVar()

    identry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    statusentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=statusval)
    statusentry.place(x=250,y=190)

    compNameentry = Entry(updateroot,font=('arial',15,'bold'),bd=5,textvariable=compNameval)
    compNameentry.place(x=250,y=250)

    ####--------add button----------
    updatebtn = Button(updateroot,text='Update',font=('arial',15,'bold'),width=20,bd=5,activebackground='blue'
                       ,activeforeground='white',bg='red',command=update)
    updatebtn.place(x=150,y=420)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        statusval.set(pp[3])
        compNameval.set(pp[4])
  

    updateroot.mainloop()


def showstudent():
        strr = 'select *from student1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4]]
            studenttable.insert('',END,values=vv)


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if(res==True):
        root.destroy()

#### Connection of database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        # Display entered host, user, and password (for debugging purposes)
        print(host,user,password)

        # Try to establish a connection with the database
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            # If connection fails, show an error message and return
            messagebox.showerror('Notifications',
                                 'Data is incorrect please try again',parent=dbroot)
            return
        
        # If connection is successful, attempt to create the database and table
        try:
            strr = 'create database COLLEGE1'   # Create the database named 'COLLEGE1'
            mycursor.execute(strr)
            strr = 'use COLLEGE1'  # Use the 'COLLEGE1' database
            mycursor.execute(strr)
            # Create a table named 'STUDENT1' with specific columns
            strr = 'create table STUDENT1(usn varchar(10),name varchar(25),phone_no varchar(10),placed_status varchar(10),comp_name varchar(30))'
            mycursor.execute(strr)
            # Modify the 'usn' column to be not null
            strr = 'alter table STUDENT1 modify column usn varchar(10) not null'
            mycursor.execute(strr)
            # Set 'usn' column as the primary key
            strr = 'alter table STUDENT1 modify column usn varchar(10) primary key'
             # Show a success message indicating the database connection
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Connected Successfully...',parent=dbroot)

        except:
            # If the database and table creation fails, assume the database already exists
            # Use the existing 'COLLEGE1' database and show a success message
            strr = 'use COLLEGE1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to database...',parent=dbroot)
        dbroot.destroy() # Close the database connection window

        
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('ico image.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='YellowGreen')
    #### connectdb labels
    hostlabel = Label(dbroot,text="Enter Host :",bg='gold2',font=('Monaco',18,'bold'),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User :",bg='gold2',font=('Monaco',18,'bold'),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password :",bg='gold2',font=('Monaco',18,'bold'),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    passwordlabel.place(x=10,y=130)
    ##### Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    

    hostentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('arial',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    ### Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('arial',15,'bold'),width=20,bg='red',bd=5,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

##################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)

### intro slider
import random
colors = ['red']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel1.config(fg=fg)
    SliderLabel1.after(2,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count >= len(ss)):
        count = 0
        text = ''
        SliderLabel1.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel1.config(text=text)
        count += 1
    SliderLabel1.after(200,IntroLabelTick)


from tkinter import *
from tkinter import Toplevel,messagebox
import random 
from tkinter.ttk import Treeview
from tkinter import ttk
import time
import pymysql 
root = Tk()
root.title('College Placement')
root.config(bg='grey')
root.geometry('1174x600+100+40')
root.iconbitmap('logo.ico')
root.resizable(False,False)

### frames
#---- dataentry Frame 
DataEntryFrame = Frame(root,bg='LightGrey',relief=SOLID,borderwidth=2)
DataEntryFrame.place(x=10,y=80,width=400,height=500)
frontlabel = Label(DataEntryFrame,text='Copyright © P4',width=25,font=('Brush Script MT',22,'italic bold'),bg='LightGrey')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='Add Student',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='Search Student',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='Delete Student',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text= 'Update Student',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

displaybtn = Button(DataEntryFrame,text='Display Student',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=showstudent)
displaybtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='Exit',width=20,font=('Georgia',20,'bold'),bd=6,bg='LightSkyBlue',activebackground='LimeGreen',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

##------Show data frame
showDataFrame = Frame(root,bg='red',relief=GROOVE,borderwidth=2)
showDataFrame.place(x=450,y=80,width=720,height=500)

##-----------show dataframe-------------
style = ttk.Style()
style.configure('Treeview.Heading',front=('arial',20,'italic bold'),foreground='blue')
style.configure('Treeview',front=('times new roman',15,'italic bold'),foreground='black',background='BlanchedAlmond')

scroll_x = Scrollbar(showDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(showDataFrame,orient=VERTICAL)
studenttable = Treeview(showDataFrame,columns=('USN','NAME','PHONE NO.','PLACED STATUS','COMPANY NAME'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('USN',text='USN')
studenttable.heading('NAME',text='NAME')
studenttable.heading('PHONE NO.',text='PHONE NO.')
studenttable.heading('PLACED STATUS',text='PLACED STATUS')
studenttable.heading('COMPANY NAME',text='COMPANY NAME')
studenttable['show'] = 'headings'
studenttable.column('USN',width=150)
studenttable.column('NAME',width=300)
studenttable.column('PHONE NO.',width=200)
studenttable.column('PLACED STATUS',width=100)
studenttable.column('COMPANY NAME',width=400)

studenttable.pack(fill=BOTH,expand=1)


### slider -- blinking part
ss = 'Welcome To College Placement System\n Developed by P4-Innovators '
count =0
text = ''
####### 
SliderLabel1 = Label(root,text=ss,font=('Lucida Handwriting',18,'italic bold'),relief=RIDGE,borderwidth=5,bg='AntiqueWhite')
SliderLabel1.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()

#### clock
clock = Label(root,text=ss,font=('time',14,'bold'),relief=RIDGE,borderwidth=4,bg='Aqua')
clock.place(x=0,y=0)
tick()


### connect database button
connectbutton = Button(root,text='Connect To Database',width=20,font=('time new roman',15,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
                       activebackground='yellow',activeforeground='red',command=Connectdb)
connectbutton.place(x=920,y=0)
root.mainloop()













