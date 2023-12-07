
#======================================================IMPORTING MODULES/LIBRARY

from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date,datetime
import sqlite3

#======================================================DATE & TIME SETTING

today = date.today()
y=today.year
m=today.month
d=today.day
wox=f"{d}/{m}/{y}"
time=datetime.now().strftime("%H:%M:%S")

#======================================================CONNECTION OF SQLITE3 DATABASE

deb=sqlite3.connect('cms.db')
cursor=deb.cursor()



#======================================================MAIN CODES OF CONTACT MANAGEMENT SYSTEM



#=====================================================TEACHER PANEL

def teacher():

#=====================================================TEACHER CMS

    #======================================================MAIN CODES OF CONTACT MANAGEMENT SYSTEM

    def teacher_cms_page():
        global tc_special2
        tc_special2=(tpcolumn1_value.split()[0])

        #=================================================TEACHER DELETE

        def teacher_delete_page():
            def back():
                det.destroy()
                teacher_main()
            def deletemain():
                c=entry_s.get().title()
                ch=entry_type.get()
                if ch=="Contact name":
                    if c=="Search..." or c=="":
                        label3=Label(det,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name !")
                        label3.place(x=170,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif c.isdigit():
                        label3=Label(det,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name in alphabet !")
                        label3.place(x=130,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    else:
                        query1="select name from contacts"
                        cursor.execute(query1)
                        data1=cursor.fetchall()
                        for i in data1:
                            if c in i:
                                w=True
                                break
                            else:
                                w=False
                        if w==True:       
                            query_name="delete from contacts where name='{}'".format(c)
                            cursor.execute(query_name)
                            deb.commit()
                            back()       
                        else:
                            label4=Label(det,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Contact name not matched !")
                            label4.place(x=143,y=190)
                            label4.after(2000,lambda:label4.destroy())
                    

                elif ch=="Contact phone number":
                    p="+91"+c
                    if c=="Search..." or c=="":
                        label2=Label(det,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone number !")
                        label2.place(x=135,y=190)
                        label2.after(2000,lambda:label2.destroy())
                    elif c.isalpha():
                        label2=Label(det,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in integer !")
                        label2.place(x=135,y=190)
                        label2.after(2000,lambda:label2.destroy())
                    elif len(c) != 10:
                        label2=Label(det,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in 10 digit !")
                        label2.place(x=130,y=190)
                        label2.after(2000,lambda:label2.destroy())
                    else:
                        query2="select phone from contacts"
                        cursor.execute(query2)
                        data2=cursor.fetchall()
                        for i in data2:
                            if p in i:
                                w=True
                                break
                            else:
                                w=False
                        if w==True:
                            query_phone="delete from contacts where phone='{}'".format(p)
                            cursor.execute(query_phone)
                            deb.commit()
                            back()
                        else:
                            label5=Label(det,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Contact phone not matched !")
                            label5.place(x=140,y=190)
                            label5.after(2000,lambda:label5.destroy())
                else:
                    label1=Label(det,bg="black",fg="red",pady=2,font=("Microsoft YeHei UI Light",12,"bold")
                                ,text="Select which type of data to search ?")
                    label1.place(x=115,y=190)
                    label1.after(2000,lambda:label1.destroy())

            det=Tk()
            det.title('DELETE PAGE')
            width =500
            height =300
            screen_width = det.winfo_screenwidth()
            screen_height = det.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            det.geometry("%dx%d+%d+%d" % (width, height, x, y))
            det.config(bg='black')
            det.resizable(0,0)
            #====================================title
            labeld=Label(det,text='Delete contact',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="red")
            labeld.place(x=140,y=15)
            #====================================request
            labeld=Label(det,text='Please enter contact Name or Phone number !',font=("Century Schoolbook L",15,"bold"),
                        bg="black",fg="white")
            labeld.place(x=30,y=80)
            #====================================type
            def on_entryt(rock):
                if entry_type.get()=='Select type!':
                    entry_type.delete(0,END)

            def on_leavet(pock):
                if entry_type.get()=='':
                    entry_type.insert(0,'Select type!')
            #====================================search
            def on_entryse(rock1):
                if entry_s.get()=='Search...':
                    entry_s.delete(0,END)

            def on_leavese(pock1):
                if entry_s.get()=='':
                    entry_s.insert(0,'Search...')
            #====================================search
            entry_s=Entry(det,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_s.place(x=30,y=140)
            entry_s.insert(0,"Search...")
            entry_s.bind('<FocusIn>',on_entryse)
            entry_s.bind('<FocusOut>',on_leavese)
            #====================================type of data
            w = StringVar()
            entry_type=ttk.Combobox(det, width = 15,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = w)
            #====================================Adding combobox drop down list
            entry_type['values'] = ('Contact name',
                                    'Contact phone number')
            entry_type.current()
            entry_type.place(x=280,y=140)
            entry_type.insert(0,"Select type!")
            entry_type.bind('<FocusIn>',on_entryt)
            entry_type.bind('<FocusOut>',on_leavet)
            #==================================back to cms page
            button_back=Button(det,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for delete data in database
            button_done=Button(det,text='Delete it!',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=deletemain,
                        cursor="hand2",bg="red",fg="black",border=0)
            button_done.place(x=150,y=230)
            #=================================mainloop
            det.mainloop()
        
        #=================================================TEACHER ADD

        def teacher_add_page():
            def back():
                add.destroy()
                teacher_main()
            #==================================================add data to database
            def addmain():
                n=entry_name.get().title()
                sn=entry_sname.get().title()
                p=entry_pn.get()
                d=entry_dob.get()
                l=entry_label.get()
                e=entry_e.get()
                s=entry_sex.get()
                a=entry_address.get().title()
                if n=='Name' and sn=='Surname' and p=='Phone number' and d=='Date of birth' and l=='Label' and e=='Email' and s=='Gender'and a=='Address':
                    lable_up=Label(add,text="All field's are required !'",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=165,y=645)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif n=="Name" or n=="":
                    lable_name=Label(add,text='Enter your Name !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_name.place(x=180,y=645)   
                    lable_name.after(2000,lambda:lable_name.destroy())
                elif sn=="Surname":
                    lable_sname=Label(add,text='Enter your Surname !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_sname.place(x=170,y=645)   
                    lable_sname.after(2000,lambda:lable_sname.destroy())
                elif p=="Phone number" or p=="":
                    lable_phone=Label(add,text='Enter your Phone number !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_phone.place(x=147,y=645)   
                    lable_phone.after(2000,lambda:lable_phone.destroy())
                elif d=="Date of birth" or d=="":
                    lable_d=Label(add,text='Enter your Date of birth !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_d.place(x=155,y=645)   
                    lable_d.after(2000,lambda:lable_d.destroy())
                elif l=="Label" or l=="":
                    lable_l=Label(add,text='Enter your Label !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_l.place(x=180,y=645)   
                    lable_l.after(2000,lambda:lable_l.destroy())
                elif e=="Email" or e=="":
                    lable_email=Label(add,text='Enter your Email !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_email.place(x=180,y=645)   
                    lable_email.after(2000,lambda:lable_email.destroy())
                elif s=="Gender" or s=="":
                    lable_sex=Label(add,text='Enter your Gender !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_sex.place(x=175,y=645)   
                    lable_sex.after(2000,lambda:lable_sex.destroy())
                elif a=="Address" or d=="":
                    lable_a=Label(add,text='Enter your Address !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_a.place(x=175,y=645)   
                    lable_a.after(2000,lambda:lable_a.destroy())
                else:
                    if n.replace(" ", "").isalpha():
                        if sn.replace(" ", "").isalpha() or sn=="":
                            if s.isalpha():
                                j=d.split('/')
                                if int(today.year) - int(j[2]) >= 16:
                                    if "@gmail.com" in e or "@yahoo.com" in e or "@outlook.com" in e:
                                        if p.isdigit():
                                            if len(p) == 10:
                                                pn="+91"+p
                                                query="Insert into contacts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(n,sn,pn,d,l,e,s,a)
                                                cursor.execute(query)
                                                deb.commit()
                                                back()
                                            else:
                                                lable_na=Label(add,text="Please enter phone number in 10 digit !",
                                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                                lable_na.place(x=105,y=645)
                                                lable_na.after(2000,lambda:lable_na.destroy())
                                        else:
                                            lable_no=Label(add,text="Enter phone number in integer !",
                                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                            lable_no.place(x=130,y=645)
                                            lable_no.after(2000,lambda:lable_no.destroy()) 
                                    else:
                                        lable_no=Label(add,text="Enter valid in email !",
                                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                        lable_no.place(x=165,y=645)
                                        lable_no.after(2000,lambda:lable_no.destroy()) 
                                else:
                                    lable_na=Label(add,text="You are not eligible to be a teacher or a student for class 12 !",
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                    lable_na.place(x=20,y=645)
                                    lable_na.after(2000,lambda:lable_na.destroy())
                            else:
                                lable_no=Label(add,text="Enter gender in alphabet!",
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_no.place(x=153,y=645)
                                lable_no.after(2000,lambda:lable_no.destroy())
                        else:
                            lable_no=Label(add,text="Enter surname in alphabet !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_no.place(x=150,y=645)
                            lable_no.after(2000,lambda:lable_no.destroy())
                    else:
                        lable_no=Label(add,text="Enter name in alphabet !",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_no.place(x=155,y=645)
                        lable_no.after(2000,lambda:lable_no.destroy()) 

            #====================================creating ADD page
            add=Tk()
            add.title('ADD CONTACT PAGE')
            width =500
            height =750
            screen_width = add.winfo_screenwidth()
            screen_height = add.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            add.geometry("%dx%d+%d+%d" % (width, height, x, y))
            add.configure(bg='black')
            add.resizable(0,0)
            #====================================photo import
            sop=PhotoImage(file='contact logo.png')
            lableb=Label(add,image=sop,bd=0,bg="black")
            lableb.place(x=177,y=20)
            #====================================title
            label1=Label(add,text='Add contact',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="dodger blue")
            label1.place(x=150,y=180)
            #====================================name
            def on_entryname(rock):
                if entry_name.get()=='Name':
                    entry_name.delete(0,END)

            def on_leavename(pock):
                if entry_name.get()=='':
                    entry_name.insert(0,'Name')
            #====================================surname
            def on_entrysname(rock):
                if entry_sname.get()=='Surname':
                    entry_sname.delete(0,END)

            def on_leavesname(pock):
                if entry_sname.get()=='':
                    entry_sname.insert(0,'Surname')
            #====================================phone no
            def on_entryspn(rock):
                if entry_pn.get()=='Phone number':
                    entry_pn.delete(0,END)

            def on_leavespn(pock):
                if entry_pn.get()=='':
                    entry_pn.insert(0,'Phone number')
            #====================================calender
            def call():
                def soup():
                    c = cal.get_date()
                    pd = datetime.strptime(c, "%m/%d/%y")
                    fd = pd.strftime("%d/%m/%Y")
                    entry_dob.delete(0, END)
                    entry_dob.insert(0, fd)
                    cal.destroy()
                cal = Calendar(add, selectmode='day', year=today.year, month=today.month, day=today.day)
                cal.place(x=130,y=430)
                cal.bind("<<CalendarSelected>>", lambda event: soup())
            #====================================dob
            def on_entrydb(rock):
                if entry_dob.get()=='Date of birth':
                    entry_dob.delete(0,END)

            def on_leavedb(pock):
                if entry_dob.get()=='':
                    entry_dob.insert(0,'Date of birth')
            #====================================label
            def on_entryl(rock):
                if entry_label.get()=='Label':
                    entry_label.delete(0,END)

            def on_leavel(pock):
                if entry_label.get()=='':
                    entry_label.insert(0,'Label')
            #====================================email
            def on_entrye(rock):
                if entry_e.get()=='Email':
                    entry_e.delete(0,END)

            def on_leavee(pock):
                if entry_e.get()=='':
                    entry_e.insert(0,'Email')
            #====================================sex
            def on_entrys(rock):
                if entry_sex.get()=='Gender':
                    entry_sex.delete(0,END)

            def on_leaves(pock):
                if entry_sex.get()=='':
                    entry_sex.insert(0,'Gender')
            #====================================address
            def on_entryaddress(rock):
                if entry_address.get()=='Address':
                    entry_address.delete(0,END)

            def on_leaveaddress(pock):
                if entry_address.get()=='':
                    entry_address.insert(0,'Address')
            #====================================name entry
            entry_name=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_name.place(x=130,y=250)
            entry_name.insert(0,"Name")
            entry_name.bind('<FocusIn>',on_entryname)
            entry_name.bind('<FocusOut>',on_leavename)
            #====================================surname entry
            entry_sname=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_sname.place(x=130,y=300)
            entry_sname.insert(0,"Surname")
            entry_sname.bind('<FocusIn>',on_entrysname)
            entry_sname.bind('<FocusOut>',on_leavesname)
            #====================================phone no entry
            entry_pn=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_pn.place(x=130,y=350)
            entry_pn.insert(0,"Phone number")
            entry_pn.bind('<FocusIn>',on_entryspn)
            entry_pn.bind('<FocusOut>',on_leavespn)
            label4=Label(add,text='+91',font=("Microsoft YeHei UI Light",15,"bold"),bg="black",fg="white")
            label4.place(x=90,y=350)
            #====================================dob entry
            entry_dob=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_dob.place(x=130,y=400)
            entry_dob.insert(0,"Date of birth")
            entry_dob.bind('<FocusIn>',on_entrydb)
            entry_dob.bind('<FocusOut>',on_leavedb)
            #====================================photo import
            so=PhotoImage(file='calendar.png')
            cal=Button(add,image=so,bd=0,bg='black',activebackground='black'
                            ,cursor='hand2',command=call)
            cal.place(x=380,y=397)
            #====================================label entry
            w = StringVar()
            entry_label=ttk.Combobox(add, width = 20,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = w)
            #====================================Adding combobox drop down list
            entry_label['values'] = ('Teacher',
                                    'Student 12A',
                                    'Student 12B')
            entry_label.current()
            entry_label.place(x=130,y=450)
            entry_label.insert(0,"Label")
            entry_label.bind('<FocusIn>',on_entryl)
            entry_label.bind('<FocusOut>',on_leavel)
            #====================================email entry
            entry_e=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_e.place(x=130,y=500)
            entry_e.insert(0,"Email")
            entry_e.bind('<FocusIn>',on_entrye)
            entry_e.bind('<FocusOut>',on_leavee)
            #====================================sex entry
            n = StringVar()
            entry_sex=ttk.Combobox(add, width = 20,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = n)
            #====================================Adding combobox drop down list
            entry_sex['values'] = ('Male',
                                    'Female',
                                    'Others')
            entry_sex.current()
            entry_sex.place(x=130,y=550)
            entry_sex.insert(0,"Gender")
            entry_sex.bind('<FocusIn>',on_entrys)
            entry_sex.bind('<FocusOut>',on_leaves)
            #====================================address entry
            entry_address=Entry(add,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_address.place(x=130,y=600)
            entry_address.insert(0,"Address")
            entry_address.bind('<FocusIn>',on_entryaddress)
            entry_address.bind('<FocusOut>',on_leaveaddress)
            #==================================back to cms page
            button_back=Button(add,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for save data in database
            button_done=Button(add,text='Save it!',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=addmain,
                        cursor="hand2",bg="dodger blue",fg="black",border=0)
            button_done.place(x=150,y=680)
            #===================================running code
            add.mainloop()
        
        #=================================================TEACHER SEARCH

        def teacher_search_page():
            def popo():
                def s2cms():
                    search2.destroy()
                    popo()
                def searchmain():
                    c=entry_s.get().title()
                    global search2
                    ch=entry_type.get()
                    if ch=='Contact name':
                        if c=="Search..." or c=="":
                            label3=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name !")
                            label3.place(x=170,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        elif c.isdigit():
                            label3=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name in alphabet !")
                            label3.place(x=130,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        else:
                            query1="select name from contacts"
                            cursor.execute(query1)
                            data1=cursor.fetchall()
                            for i in data1:
                                if c in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                src.destroy()
                                search2=Tk()
                                width =925
                                height =520
                                screen_width = search2.winfo_screenwidth()
                                screen_height = search2.winfo_screenheight()
                                x = (screen_width/2) - (width/2)
                                y = (screen_height/2) - (height/2)
                                search2.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                search2.title('SEARCH CONTACT PAGE')
                                search2.configure(bg='black')
                                search2.resizable(False,False)
                                button_not=Button(search2,text='←Back',
                                                font=("Algeria",13,"bold"),
                                                cursor="hand2",
                                                activebackground="black",
                                                command=s2cms,
                                                bg="black",fg="white",bd=0)
                                button_not.place(x=0,y=0)
                                o=c.upper()
                                label4=Label(search2,bg="black",fg="peach puff",
                                            text="DATA OF "+o+" CONTACT IS.....",font=("Microsoft YeHei UI Light",25,"bold"))
                                label4.place(x=150,y=10)
                                def o(p):
                                    l=["Firstname","Surname","Phone number","Date of birth","Label","Email","Gender","Address"]
                                    for j in p:
                                        h=0
                                        o=90
                                        for i in j:
                                            Label(search2,text=l[h]+" : "+i,bg="black",
                                                fg="white",font=("Microsoft YeHei UI Light",18,"bold")).place(x=30,y=o)
                                            o+=45
                                            h+=1
                                cursor.execute(("select * from contacts where name='{}'").format(c))
                                data_name=cursor.fetchall()
                                o(data_name)
                                search2.mainloop()
                            else:
                                label=Label(src,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact name does not exist !")
                                label.place(x=105,y=190)
                                label.after(2000,lambda:label.destroy())
                                                        

                    elif ch=='Contact phone number':
                        phone="+91"+c
                        if c=="Search..." or c=="":
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone number !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif c.isalpha():
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in integer !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif len(c) != 10:
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in 10 digit !")
                            label2.place(x=130,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        else:
                            query2="select phone from contacts"
                            cursor.execute(query2)
                            data2=cursor.fetchall()
                            for i in data2:
                                if phone in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                    src.destroy()
                                    search2=Tk()
                                    width =925
                                    height =520
                                    screen_width = search2.winfo_screenwidth()
                                    screen_height = search2.winfo_screenheight()
                                    x = (screen_width/2) - (width/2)
                                    y = (screen_height/2) - (height/2)
                                    search2.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                    search2.title('SEARCH CONTACT PAGE')
                                    search2.configure(bg='black')
                                    search2.resizable(False,False)
                                    button_not=Button(search2,text='←Back',
                                                    font=("Algeria",13,"bold"),
                                                    cursor="hand2",
                                                    activebackground="black",
                                                    command=s2cms,
                                                    bg="black",fg="white",bd=0)
                                    button_not.place(x=0,y=0)
                                    label4=Label(search2,bg="black",fg="peach puff",
                                                text="DATA OF "+phone+" CONTACT IS.....",font=("Microsoft YeHei UI Light",25,"bold"))
                                    label4.place(x=150,y=10)
                                    def d(p):
                                        l=["Firstname","Surname","Phone number","Date of birth","Label","Email","Gender","Address"]
                                        for j in p:
                                            h=0
                                            o=90
                                            for i in j:
                                                Label(search2,bg="black",fg="white",
                                                    font=("Microsoft YeHei UI Light",18,"bold"),text=l[h]+" : "+i).place(x=30,y=o)
                                                o+=45
                                                h+=1
                                    cursor.execute(("select * from contacts where phone='{}'").format(phone))
                                    data_phone=cursor.fetchall()
                                    d(data_phone) 
                                    search2.mainloop()
                            else:
                                label=Label(src,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact phone number does not exist!")
                                label.place(x=80,y=190)
                                label.after(2000,lambda:label.destroy())
            
                    else:
                        label1=Label(src,bg="black",fg="red",font=("Microsoft YeHei UI Light",12,"bold")
                                    ,text="Select which type of data to search ?")
                        label1.place(x=115,y=190)
                        label1.after(2000,lambda:label1.destroy())

                def back():
                    src.destroy()
                    teacher_main()

                src=Tk()
                src.title('SEARCH PAGE')
                #ver.geometry('500x300+500+250')
                width =500
                height =300
                screen_width = src.winfo_screenwidth()
                screen_height = src.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                src.geometry("%dx%d+%d+%d" % (width, height, x, y))
                src.config(bg='black')
                src.resizable(0,0)
                #====================================title
                labeld=Label(src,text='Search contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="peach puff")
                labeld.place(x=135,y=15)
                #====================================request
                labeld=Label(src,text='Please enter contact Name or Phone number !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=30,y=80)
                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select type!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select type!')
                #====================================search
                def on_entryse(rock1):
                    if entry_s.get()=='Search...':
                        entry_s.delete(0,END)

                def on_leavese(pock1):
                    if entry_s.get()=='':
                        entry_s.insert(0,'Search...')
                #====================================search
                entry_s=Entry(src,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_s.place(x=30,y=140)
                entry_s.insert(0,"Search...")
                entry_s.bind('<FocusIn>',on_entryse)
                entry_s.bind('<FocusOut>',on_leavese)
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(src, width = 15,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('Contact name',
                                        'Contact phone number')
                entry_type.current()
                entry_type.place(x=280,y=140)
                entry_type.insert(0,"Select type!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(src,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for delete data in database
                button_done=Button(src,text='Search it!',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=searchmain,
                            cursor="hand2",bg="peach puff",fg="black",border=0)
                button_done.place(x=150,y=230)
                #====================================mainloop 
                src.mainloop()
            popo()
        
        #=================================================TEACHER SORT

        def teacher_sort_page():
            def ret():
                sortmain()
            def sortmain():
                def Ascending():
                    dj=entry_type.get()
                    if dj=="Please select your choice !" or dj=="":
                        label3=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label3.place(x=150,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif dj=="name" or dj=="surname" or dj=="phone" or dj=="dob" or dj=="label" or dj=="email" or dj=="sex" or dj=="address":
                        def bye():
                            ase.destroy()
                            ret()
                        def p():
                            sot.destroy()
                            query_za=("select * from contacts order by {} ").format(dj)
                            cursor.execute(query_za)
                            data_za=cursor.fetchall()
                            global c
                            c = 0
                            for record in data_za:
                                if c % 2 == 0:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                                else:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                                c += 1
                        ase=Tk()
                        width =1355
                        height =570
                        screen_width = ase.winfo_screenwidth()
                        screen_height = ase.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        ase.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        ase.config(bg='dodger blue')
                        ase.resizable(0,0)

                        label_text = "Sorting contacts in order by {} format".format(dj)
                        label1 = Label(ase, text=label_text, font=("Century Schoolbook L", 20, "bold"), bg="dodger blue", fg="black")
                        label1.place(x=350)


                        t=Frame(ase)
                        t.place(x=5,y=40)

                        #==================================back to cms page
                        button_back=Button(ase,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="dodger blue",
                                    command=bye,
                                    cursor="hand2",bg="dodger blue",fg="black",border=0)
                        button_back.place(x=0,y=0)

                        yscroll=Scrollbar(t,orient=VERTICAL)
                        yscroll.pack(side=LEFT,fill=Y)
                        
                        columns = ("firstname", "surname", "phoneNo", "DOB", "label",  "email", "sex", "address")
                        my_tree = ttk.Treeview(t,height=25, show="headings",selectmode="browse",
                                                columns=columns,yscrollcommand=yscroll.set)
                                                
                        my_tree.pack()

                        yscroll.config(command=my_tree.yview)

                        my_tree.column("firstname", anchor=CENTER, width=85, minwidth=85)
                        my_tree.column("surname", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("phoneNo", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("DOB", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("label", anchor=CENTER, width=150, minwidth=150)
                        my_tree.column("sex", anchor=CENTER, width=50, minwidth=50)
                        my_tree.column("email", anchor=CENTER, width=250, minwidth=250)
                        my_tree.column("address", anchor=CENTER, width=490, minwidth=490)

                        my_tree.heading("firstname", text="Firstname", anchor=CENTER)
                        my_tree.heading("surname", text="Surname", anchor=CENTER)
                        my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
                        my_tree.heading("DOB", text="DOB", anchor=CENTER)
                        my_tree.heading("label", text="Label", anchor=CENTER)
                        my_tree.heading("sex", text="Sex", anchor=CENTER)
                        my_tree.heading("email", text="Email", anchor=CENTER)
                        my_tree.heading("address", text="Address", anchor=CENTER)

                        # Define styles for treeview table
                        style = ttk.Style()
                        style.theme_use("clam")  # Choose a theme ('clam' is just an example)

                        # Configure the header style
                        style.configure("Treeview.Heading",
                                        font=("Century Gothic", 12, "bold"),bg="black",
                                        foreground="white")

                        # Configure the row style
                        style.configure("Treeview",
                                        font=("Century Gothic", 11),
                                        background="white",
                                        foreground="black")
                        
                        style.map('Treeview', background=[('selected', 'dodger blue')])

                        my_tree.tag_configure('oddrow', background='white')
                        my_tree.tag_configure('evenrow', background='dodger blue')
                    
                        p()
                        ase.mainloop()
                    else:
                        label2=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label2.place(x=150,y=190)
                        label2.after(2000,lambda:label2.destroy())

                def Descending():
                    dj=entry_type.get()
                    if dj=="Please select your choice !" or dj=="":
                        label3=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label3.place(x=150,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif dj=="name" or dj=="surname" or dj=="phone" or dj=="dob" or dj=="label" or dj=="email" or dj=="sex" or dj=="address":
                        def bye():
                            des.destroy()
                            sortmain()
                        def p():
                            sot.destroy()
                            query_za=("select * from contacts order by {} desc").format(dj)
                            cursor.execute(query_za)
                            data_za=cursor.fetchall()
                            global c
                            c = 0
                            for record in data_za:
                                if c % 2 == 0:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                                else:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                                c += 1
                        des=Tk()
                        width =1355
                        height =570
                        screen_width = des.winfo_screenwidth()
                        screen_height = des.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        des.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        des.config(bg='lime green')
                        des.resizable(0,0)

                        label_text = "Sorting contacts in descending order by {} format".format(dj)
                        label1 = Label(des, text=label_text, font=("Century Schoolbook L", 20, "bold"), bg="lime green", fg="black")
                        label1.place(x=350)


                        t=Frame(des)
                        t.place(x=5,y=40)

                        #==================================back to cms page
                        button_back=Button(des,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="lime green",
                                    command=bye,
                                    cursor="hand2",bg="lime green",fg="black",border=0)
                        button_back.place(x=0,y=0)

                        yscroll=Scrollbar(t,orient=VERTICAL)
                        yscroll.pack(side=LEFT,fill=Y)
                        
                        columns = ("firstname", "surname", "phoneNo", "DOB", "label",  "email", "sex", "address")
                        my_tree = ttk.Treeview(t,height=25, show="headings",selectmode="browse",
                                                columns=columns,yscrollcommand=yscroll.set)
                                                
                        my_tree.pack()

                        yscroll.config(command=my_tree.yview)

                        my_tree.column("firstname", anchor=CENTER, width=85, minwidth=85)
                        my_tree.column("surname", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("phoneNo", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("DOB", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("label", anchor=CENTER, width=150, minwidth=150)
                        my_tree.column("sex", anchor=CENTER, width=50, minwidth=50)
                        my_tree.column("email", anchor=CENTER, width=250, minwidth=250)
                        my_tree.column("address", anchor=CENTER, width=490, minwidth=490)

                        my_tree.heading("firstname", text="Firstname", anchor=CENTER)
                        my_tree.heading("surname", text="Surname", anchor=CENTER)
                        my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
                        my_tree.heading("DOB", text="DOB", anchor=CENTER)
                        my_tree.heading("label", text="Label", anchor=CENTER)
                        my_tree.heading("sex", text="Sex", anchor=CENTER)
                        my_tree.heading("email", text="Email", anchor=CENTER)
                        my_tree.heading("address", text="Address", anchor=CENTER)

                        # Define styles for treeview table
                        style = ttk.Style()
                        style.theme_use("clam")  # Choose a theme ('clam' is just an example)

                        # Configure the header style
                        style.configure("Treeview.Heading",
                                        font=("Century Gothic", 12, "bold"),bg="black",
                                        foreground="white")

                        # Configure the row style
                        style.configure("Treeview",
                                        font=("Century Gothic", 11),
                                        background="white",
                                        foreground="black")
                        
                        style.map('Treeview', background=[('selected', 'lime green')])

                        my_tree.tag_configure('oddrow', background='white')
                        my_tree.tag_configure('evenrow', background='lime green')
                    
                        p()
                        des.mainloop()
                    else:
                        label2=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label2.place(x=150,y=190)
                        label2.after(2000,lambda:label2.destroy())

                def back():
                    sot.destroy()
                    teacher_main()

                sot=Tk()
                sot.title('SORTING PAGE')
                width =500
                height =300
                screen_width = sot.winfo_screenwidth()
                screen_height = sot.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                sot.geometry("%dx%d+%d+%d" % (width, height, x, y))
                sot.config(bg='black')
                sot.resizable(0,0)
                #====================================title
                labeld=Label(sot,text='Sort contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="gold")
                labeld.place(x=150,y=15)
                #====================================request
                labeld=Label(sot,text='Please select your choice !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=120,y=80)
                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select your choice!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select your choice!')
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(sot, width = 30,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('name',
                                        'surname',
                                        'phone',
                                        'dob',
                                        'label',
                                        'email',
                                        'sex',
                                        'address')
                entry_type.current()
                entry_type.place(x=75,y=140)
                entry_type.insert(0,"Select your choice!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(sot,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for decending
                button_done=Button(sot,text='Descending',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=Descending,
                            cursor="hand2",bg="lime green",fg="black",border=0)
                button_done.place(x=265,y=230)
                #==================================button for accending
                button_done=Button(sot,text='Ascending',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=Ascending,
                            cursor="hand2",bg="dodger blue",fg="black",border=0)
                button_done.place(x=35,y=230)
                #====================================mainloop 
                sot.mainloop()
            sortmain()
        
        #=================================================TEACHER EDIT

        def teacher_edit_page():
            def ret():
                main()
            def main():
                def editmain():
                    def display():
                        def purana():
                            dude.destroy()
                            ret()
                        def update():
                            n=entry_name.get().title()
                            sn=entry_sname.get().title()
                            p=entry_pn.get()
                            d=entry_dob.get()
                            l=entry_label.get()
                            e=entry_e.get()
                            s=entry_sex.get()
                            a=entry_address.get().title()
                            if n=='' and sn=='' and p=='' and d=='' and l=='' and e=='' and s==''and a=='':
                                lable_up=Label(dude,text="All field's are required !'",
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_up.place(x=165,y=515)   
                                lable_up.after(2000,lambda:lable_up.destroy())
                            elif n=="":
                                lable_name=Label(dude,text='Enter your Name !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_name.place(x=180,y=515)   
                                lable_name.after(2000,lambda:lable_name.destroy())
                            elif p=="":
                                lable_phone=Label(dude,text='Enter your Phone number !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_phone.place(x=147,y=515)   
                                lable_phone.after(2000,lambda:lable_phone.destroy())
                            elif d=="":
                                lable_d=Label(dude,text='Enter your Date of birth !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_d.place(x=155,y=515)   
                                lable_d.after(2000,lambda:lable_d.destroy())
                            elif l=="":
                                lable_l=Label(dude,text='Enter your Label !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_l.place(x=180,y=515)   
                                lable_l.after(2000,lambda:lable_l.destroy())
                            elif e=="":
                                lable_email=Label(dude,text='Enter your Email !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_email.place(x=180,y=515)   
                                lable_email.after(2000,lambda:lable_email.destroy())
                            elif s=="":
                                lable_sex=Label(dude,text='Enter your Gender !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_sex.place(x=175,y=515)   
                                lable_sex.after(2000,lambda:lable_sex.destroy())
                            elif d=="":
                                lable_a=Label(dude,text='Enter your Address !',
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_a.place(x=175,y=515)   
                                lable_a.after(2000,lambda:lable_a.destroy())
                            else:
                                if n.replace(" ", "").isalpha():
                                    if sn.replace(" ", "").isalpha() or sn=="":
                                        if s.isalpha():
                                            j=d.split('/')
                                            if int(today.year) - int(j[2]) >= 16:
                                                if "@gmail.com" in e or "@yahoo.com" in e or "@outlook.com" in e:
                                                    if p.isdigit():
                                                        if len(p) == 10:
                                                            pn="+91"+p
                                                            query='update contacts set name="{}",surname="{}",phone="{}",dob="{}",label="{}",email="{}",sex="{}",address="{}" where {}="{}"'.format(n,sn,pn,d,l,e,s,a,column_name,dv)
                                                            cursor.execute(query)
                                                            deb.commit()
                                                            dude.destroy()
                                                            teacher_main()
                                                        else:
                                                            lable_na=Label(dude,text="Please enter phone number in 10 digit !",
                                                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                                            lable_na.place(x=105,y=515)
                                                            lable_na.after(2000,lambda:lable_na.destroy())
                                                    else:
                                                        lable_no=Label(dude,text="Enter phone number in integer !",
                                                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                                        lable_no.place(x=130,y=515)
                                                        lable_no.after(2000,lambda:lable_no.destroy()) 
                                                else:
                                                    lable_no=Label(dude,text="Enter valid in email !",
                                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                                    lable_no.place(x=170,y=515)
                                                    lable_no.after(2000,lambda:lable_no.destroy())
                                            else:
                                                lable_na=Label(dude,text="You are not eligible to be a teacher or a student for class 12 !",
                                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                                lable_na.place(x=20,y=515)
                                                lable_na.after(2000,lambda:lable_na.destroy())
                                        else:
                                            lable_no=Label(dude,text="Enter gender in alphabet!",
                                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                            lable_no.place(x=153,y=515)
                                            lable_no.after(2000,lambda:lable_no.destroy())
                                    else:
                                        lable_no=Label(dude,text="Enter surname in alphabet !",
                                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                        lable_no.place(x=150,y=515)
                                        lable_no.after(2000,lambda:lable_no.destroy())
                                else:
                                    lable_no=Label(dude,text="Enter name in alphabet !",
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                    lable_no.place(x=155,y=515)
                                    lable_no.after(2000,lambda:lable_no.destroy()) 


                        global dv
                        if special_c.isdigit():
                            dv="+91"+special_c
                        else:
                            dv=special_c
                        query = "SELECT * FROM contacts WHERE {} = ?".format(column_name)
                        cursor.execute(query, (dv,))
                        data_name = cursor.fetchall()
                        n=data_name[0][0]
                        s=data_name[0][1]
                        p = data_name[0][2].replace("+91", "")  # Remove +91 prefix
                        d=data_name[0][3]
                        l=data_name[0][4]
                        e=data_name[0][5]
                        sx=data_name[0][6]
                        a=data_name[0][7]
                        edi.destroy()

                        #==================================creating window
                        dude=Tk()
                        dude.title('EDIT CONTACT PAGE')
                        width =500
                        height =620
                        screen_width = dude.winfo_screenwidth()
                        screen_height = dude.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        dude.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        dude.configure(bg='black')
                        dude.resizable(0,0)
                        #====================================title
                        label1=Label(dude,text='Edit contact',font=("Century Schoolbook L",25,"bold"),
                                    bg="black",fg="purple1")
                        label1.place(x=150,y=20)
                        #====================================name entry
                        label_name=Label(dude,text="Name :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_name.place(x=15,y=120)
                        entry_name=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_name.place(x=210,y=120)
                        entry_name.insert(0,n)
                        #====================================sname entry
                        label_sname=Label(dude,text="Surname :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_sname.place(x=15,y=170)
                        entry_sname=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_sname.place(x=210,y=170)
                        entry_sname.insert(0,s)
                        #====================================phone entry
                        label_pn=Label(dude,text="Phone number : +91",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_pn.place(x=15,y=220)
                        entry_pn=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_pn.place(x=210,y=220)
                        entry_pn.insert(0,p)
                        #===================================dob entry
                        #====================================calender
                        def call():
                            def soup():
                                c = cal.get_date()
                                pd = datetime.strptime(c, "%m/%d/%y")
                                fd = pd.strftime("%d/%m/%Y")
                                entry_dob.delete(0, END)
                                entry_dob.insert(0, fd)
                                cal.destroy()
                            cal = Calendar(dude, selectmode='day', year=today.year, month=today.month, day=today.day)
                            cal.place(x=210,y=300)
                            cal.bind("<<CalendarSelected>>", lambda event: soup())

                        label_dob=Label(dude,text="Date of birth :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_dob.place(x=15,y=270)
                        entry_dob=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_dob.place(x=210,y=270)
                        entry_dob.insert(0,d)
                        #====================================photo import
                        so=PhotoImage(file='calendar.png')
                        cal=Button(dude,image=so,bd=0,bg='black',activebackground='black'
                                        ,cursor='hand2',command=call)
                        cal.place(x=460,y=267)
                        #====================================label entry
                        label_l=Label(dude,text="Label :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_l.place(x=15,y=320)
                        w = StringVar()
                        entry_label=ttk.Combobox(dude, width = 20,font=("Microsoft YeHei UI Light",15),
                                                    textvariable = w)
                        #====================================Adding combobox drop down list
                        entry_label['values'] = ('Teacher',
                                                'Student 12A',
                                                'Student 12B')
                        entry_label.current()
                        entry_label.place(x=210,y=320)
                        entry_label.insert(0,l)
                        #====================================email entry
                        label_e=Label(dude,text="Email :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_e.place(x=15,y=370)
                        entry_e=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_e.place(x=210,y=370)
                        entry_e.insert(0,e)
                        #====================================sex entry
                        label_sx=Label(dude,text="Sex :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_sx.place(x=15,y=420)
                        n = StringVar()
                        entry_sex=ttk.Combobox(dude, width = 20,font=("Microsoft YeHei UI Light",15),
                                                    textvariable = n)
                        #====================================Adding combobox drop down list
                        entry_sex['values'] = ('Male',
                                                'Female',
                                                'Others')
                        entry_sex.current()
                        entry_sex.place(x=210,y=420)
                        entry_sex.insert(0,sx)
                        #====================================address entry
                        label_sx=Label(dude,text="Address :",font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        label_sx.place(x=15,y=470)
                        entry_address=Entry(dude,width=22,font=("Microsoft YeHei UI Light",15),bd=2)
                        entry_address.place(x=210,y=470)
                        entry_address.insert(0,a)
                        #==================================back to cms page
                        button_back=Button(dude,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="black",
                                    command=purana,
                                    cursor="hand2",bg="black",fg="white",border=0)
                        button_back.place(x=0,y=0)
                        #==================================button for save data in database
                        button_done=Button(dude,text='Save it!',font=("Algeria",13,"bold"),
                                    width=20,pady=5,activebackground="black",
                                    command=update,
                                    cursor="hand2",bg="Purple1",fg="black",border=0)
                        button_done.place(x=150,y=550)
                        #==================================mainloop
                        dude.mainloop()


                    global special_c 
                    special_c=entry_s.get().title()
                    ch=entry_type.get()
                    if ch=='Contact name':
                        name=special_c
                        if name=="Search..." or name=="":
                            label3=Label(edi,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name !")
                            label3.place(x=170,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        elif name.isdigit():
                            label3=Label(edi,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name in alphabet !")
                            label3.place(x=130,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        else:
                            query1="select name from contacts"
                            cursor.execute(query1)
                            data1=cursor.fetchall()
                            for i in data1:
                                if name in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                column_name= "name"
                                display()
                            else:
                                label=Label(edi,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact name does not exist !")
                                label.place(x=105,y=190)
                                label.after(2000,lambda:label.destroy())
                    elif ch=='Contact phone number':
                        phone="+91"+special_c
                        if special_c=="Search..." or special_c=="":
                            label2=Label(edi,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone number !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif special_c.isalpha():
                            label2=Label(edi,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in integer !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif len(special_c) != 10:
                            label2=Label(edi,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in 10 digit !")
                            label2.place(x=130,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        else:
                            query2="select phone from contacts"
                            cursor.execute(query2)
                            data2=cursor.fetchall()
                            for i in data2:
                                if phone in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                column_name= "phone"
                                display()
                            else:
                                label=Label(edi,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact phone number does not exist!")
                                label.place(x=80,y=190)
                                label.after(2000,lambda:label.destroy())
                    else:
                        label1=Label(edi,bg="black",fg="red",font=("Microsoft YeHei UI Light",12,"bold")
                                    ,text="Select which type of data to search ?")
                        label1.place(x=115,y=190)
                        label1.after(2000,lambda:label1.destroy())
                def back():
                        edi.destroy()
                        teacher_main()

                edi=Tk()
                edi.title('SEARCH PAGE')
                width =500
                height =300
                screen_width = edi.winfo_screenwidth()
                screen_height = edi.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                edi.geometry("%dx%d+%d+%d" % (width, height, x, y))
                edi.config(bg='black')
                edi.resizable(0,0)
                #====================================title
                labeld=Label(edi,text='Edit contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="purple1")
                labeld.place(x=155,y=15)
                #====================================request
                labeld=Label(edi,text='Please enter contact Name or Phone number !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=30,y=80)
                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select type!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select type!')
                #====================================search
                def on_entryse(rock1):
                    if entry_s.get()=='Search...':
                        entry_s.delete(0,END)

                def on_leavese(pock1):
                    if entry_s.get()=='':
                        entry_s.insert(0,'Search...')
                #====================================search
                entry_s=Entry(edi,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_s.place(x=30,y=140)
                entry_s.insert(0,"Search...")
                entry_s.bind('<FocusIn>',on_entryse)
                entry_s.bind('<FocusOut>',on_leavese)
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(edi, width = 15,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('Contact name',
                                        'Contact phone number')
                entry_type.current()
                entry_type.place(x=280,y=140)
                entry_type.insert(0,"Select type!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(edi,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for delete data in database
                button_done=Button(edi,text='Search it!',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=editmain,
                            cursor="hand2",bg="purple1",fg="black",border=0)
                button_done.place(x=150,y=230)
                #====================================mainloop 
                edi.mainloop()
            main()
        
        #=================================================TEACHER PRINT

        def teacher_print_page():
            def pmain():
                def printmain():
                    dk=entry_type.get()
                    def prj():
                        def tata():
                            ganga.destroy()
                            pmain()
                        def aim():
                            fj=entry_s.get().title()
                            if fj=='' or fj=='File Name':
                                label6=Label(ganga,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Please enter your file name !")
                                label6.place(x=135,y=190)
                                label6.after(2000,lambda:label6.destroy())
                            else:
                                # Execute a query to fetch data from the 'contacts' table
                                query = "SELECT * FROM contacts WHERE label = '{}'".format(dk)
                                cursor.execute(query)
                                data = cursor.fetchall()

                                # Ask the user for a file name
                                output_file = fj + '.txt'

                                # Define the widths for each column
                                column_widths = [25, 15, 15, 15, 30, 10, 30]

                                # Create a format string for each row based on column widths
                                format_string = ' | '.join('{{:<{}}}'.format(width) for width in column_widths)

                                # Write data to the text file with headings and formatted rows
                                with open(output_file, 'w') as file:
                                    headings = ["Name", "Phone Number", "Date of Birth", "Label", "Email", "Sex", "Address"]
                                    separator_line = '-+-'.join('-' * width for width in column_widths)
                                    file.write(format_string.format(*headings) + '\n')
                                    file.write(separator_line + '\n')
                                    for row in data:
                                        name = f"{row[0]} {row[1]}".ljust(column_widths[0])
                                        formatted_row = [name] + list(str(item).ljust(width) for item, width in zip(row[2:], column_widths[1:]))
                                        file.write(format_string.format(*formatted_row) + '\n')

                                # Close the database connection
                                ganga.destroy()
                                teacher_main()
                                    

                        pari.destroy()
                        ganga=Tk()
                        ganga.title('PRINT PAGE')
                        width =500
                        height =300
                        screen_width = ganga.winfo_screenwidth()
                        screen_height = ganga.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        ganga.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        ganga.config(bg='black')
                        ganga.resizable(0,0)
                        #====================================title
                        labeld=Label(ganga,text='Print contact',font=("Century Schoolbook L",25,"bold"),
                                    bg="black",fg="cyan")
                        labeld.place(x=140,y=15)
                        #====================================request
                        labeld=Label(ganga,text='Please enter your file name to save data !',font=("Century Schoolbook L",15,"bold"),
                                    bg="black",fg="white")
                        labeld.place(x=50,y=80)
                        #====================================file name
                        def on_entryse(rock1):
                            if entry_s.get()=='File Name':
                                entry_s.delete(0,END)

                        def on_leavese(pock1):
                            if entry_s.get()=='':
                                entry_s.insert(0,'File Name')
                        #====================================file name
                        entry_s=Entry(ganga,width=30,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                        entry_s.place(x=75,y=140)
                        entry_s.insert(0,"File Name")
                        entry_s.bind('<FocusIn>',on_entryse)
                        entry_s.bind('<FocusOut>',on_leavese)
                        #==================================back to cms page
                        button_back=Button(ganga,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="black",
                                    command=tata,
                                    cursor="hand2",bg="black",fg="white",border=0)
                        button_back.place(x=0,y=0)
                        #==================================button for delete data in database
                        button_done=Button(ganga,text='Print it!',font=("Algeria",13,"bold"),
                                    width=20,pady=5,activebackground="black",
                                    command=aim,
                                    cursor="hand2",bg="cyan",fg="black",border=0)
                        button_done.place(x=140,y=230)
                        ganga.mainloop()

                    if dk == '' or dk == 'Select type!':
                        label3=Label(pari,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label3.place(x=150,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif dk not in ['Teacher', 'Student 12A', 'Student 12B']:
                        label2=Label(pari,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice from given option !")
                        label2.place(x=75,y=190)
                        label2.after(2000,lambda:label2.destroy())
                    else:
                        prj()
                        
                def back():
                    pari.destroy()
                    teacher_main()
                pari=Tk()
                pari.title('PRINT PAGE')
                width =500
                height =300
                screen_width = pari.winfo_screenwidth()
                screen_height = pari.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                pari.geometry("%dx%d+%d+%d" % (width, height, x, y))
                pari.config(bg='black')
                pari.resizable(0,0)
                #====================================title
                labeld=Label(pari,text='Print contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="cyan")
                labeld.place(x=140,y=15)
                #====================================request
                labeld=Label(pari,text='Please enter your choice for data print format !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=25,y=80)

                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select type!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select type!')
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(pari, width = 30,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('Teacher',
                                        'Student 12A',
                                        'Student 12B')
                entry_type.current()
                entry_type.place(x=75,y=140)
                entry_type.insert(0,"Select type!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(pari,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for delete data in database
                button_done=Button(pari,text='Print it!',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=printmain,
                            cursor="hand2",bg="cyan",fg="black",border=0)
                button_done.place(x=150,y=230)
                pari.mainloop()
            pmain()
        
        #=================================================MAIN CMS
        
        def teacher_main():
            def search():
                main.destroy()
                teacher_search_page()
            def sort():
                main.destroy()
                teacher_sort_page()
            def delete():
                main.destroy()
                teacher_delete_page()
            def add():
                main.destroy()
                teacher_add_page()
            def edit():
                main.destroy()
                teacher_edit_page()
            def prin():
                main.destroy()
                teacher_print_page()
            def back():
                main.destroy()
                panel()
            #=================================================main window 
            main=Tk()
            main.title('TEACHER MAIN PAGE OF CONTACT MANAGEMENT SYSTEM')
            width =1475
            height =705
            screen_width = main.winfo_screenwidth()
            screen_height = main.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            main.geometry("%dx%d+%d+%d" % (width, height, x, y))
            main.configure(bg='black')
            main.resizable(0,0)
            #=================================================upper frame
            frameu=Frame(main,width=1465,height=60,bg="grey93",bd=0)
            frameu.place(x=5,y=5)
            #====================================photo import
            h=PhotoImage(file='healding.png')
            lableb=Label(frameu,image=h,bd=0,bg="grey93")
            lableb.place(x=0,y=0)
            #====================================photo import
            sm=PhotoImage(file='tmain.png')
            lableb=Label(frameu,image=sm,bd=0,bg="grey93")
            lableb.place(x=1400,y=2)
            #===================================hi label
            labelh=Label(frameu,text=("Hi! "+tc_special2),font=("Century Schoolbook L",20,"bold"),
                            bg="grey93",fg="black")
            labelh.place(x=1100,y=10)
            #===================================menu
            menubutton = Menubutton(frameu, text='▼')  # Unicode for downward arrow
            menu = Menu(menubutton, tearoff=0,activebackground="black")
            menu.add_command(label='Logout',command=back)
            menubutton.config(menu=menu)
            menubutton.place(x=1375,y=15)
            #=================================================left side frame
            framel=Frame(main,width=200,height=630,bg="grey93",bd=0)
            framel.place(x=5,y=70)
            #=================================================features label
            label1=Label(framel,text='Features !',font=("Century Schoolbook L",20,"bold"),
                            bg="grey93",fg="black")
            label1.place(x=35,y=100)
            #==================================button to add contact
            button_done=Button(framel,text='Add contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=add,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=170)
            #==================================button to delete contact
            button_done=Button(framel,text='Delete contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=delete,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=230)
            #==================================button to edit contact
            button_done=Button(framel,text='Edit contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=edit,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=290)
            #==================================button to sort contact
            button_done=Button(framel,text='sort contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=sort,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=350)
            #==================================button to search contact
            button_done=Button(framel,text='Search contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=search,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=410)
            #==================================button to print contact
            button_done=Button(framel,text='Print contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=prin,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=470)
            #=================================================date
            lable_d=Label(framel,text=f"Date:- {wox}",
                            font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            lable_d.place(x=6,y=5)
            #=================================================time
            def update_clock():
                current_time = datetime.now().strftime("%H:%M:%S")
                clock_label.config(text=current_time)
                clock_label.after(1000, update_clock)# Update every 1 second (1000 milliseconds)

            lable_t=Label(framel,text="Time:- ",
                            font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            lable_t.place(x=4,y=40)

            clock_label = Label(framel,font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            clock_label.place(x=80,y=40)

            update_clock()
            #=================================================main frame
            t=Frame(main,width=1065,height=615,bg="white",bd=0)
            t.place(x=210,y=70)
            #=================================================tree view diaplay
            def tree():
                cursor.execute("SELECT * FROM contacts order by label")
                data = cursor.fetchall()

                global c
                c = 0
                for record in data:
                    if c % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                    c += 1

            yscroll=Scrollbar(t,orient=VERTICAL)
            yscroll.pack(side=RIGHT,fill=Y)
            xscroll=Scrollbar(t,orient=HORIZONTAL)
            xscroll.pack(side=BOTTOM,fill=X)

            columns = ("firstname", "surname", "phoneNo", "DOB", "label", "email", "sex", "address")
            my_tree = ttk.Treeview(t,height=23, show="headings",selectmode="browse",
                                    columns=columns,yscrollcommand=yscroll.set,
                                    xscrollcommand=xscroll.set)
            my_tree.pack()

            yscroll.config(command=my_tree.yview)
            xscroll.config(command=my_tree.xview)

            my_tree.column("firstname", anchor=CENTER, width=100, minwidth=110)
            my_tree.column("surname", anchor=CENTER, width=110, minwidth=150)
            my_tree.column("phoneNo", anchor=CENTER, width=145, minwidth=165)
            my_tree.column("DOB", anchor=CENTER, width=100, minwidth=150)
            my_tree.column("label", anchor=CENTER, width=150, minwidth=200)
            my_tree.column("email", anchor=CENTER, width=250, minwidth=300)
            my_tree.column("sex", anchor=CENTER, width=100, minwidth=110)
            my_tree.column("address", anchor=CENTER, width=285, minwidth=345)

            my_tree.heading("firstname", text="Firstname", anchor=CENTER)
            my_tree.heading("surname", text="Surname", anchor=CENTER)
            my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
            my_tree.heading("DOB", text="DOB", anchor=CENTER)
            my_tree.heading("label", text="Label", anchor=CENTER)
            my_tree.heading("email", text="Email", anchor=CENTER)
            my_tree.heading("sex", text="Sex", anchor=CENTER)
            my_tree.heading("address", text="Address", anchor=CENTER)

            # Define styles for treeview table
            style = ttk.Style()
            style.theme_use("clam")  # Choose a theme ('clam' is just an example)

            # Configure the header style
            style.configure("Treeview.Heading",
                            font=("Century Gothic", 16, "bold"),
                            foreground="black")

            # Configure the row style
            style.configure("Treeview",
                            font=("Century Gothic", 16),
                            background="white",
                            foreground="black",rowheight=25)

            style.map('Treeview', background=[('selected', 'dodger blue')])


            my_tree.tag_configure('oddrow', background='white')
            my_tree.tag_configure('evenrow', background='lightblue')

            tree()  # Call the main function to populate the treeview

            #==================================================mainloop
            main.mainloop()
        teacher_main()

#=====================================================TEACHER LOGIN PAGE

    def teacher_login_page():

#======================================================TEACHER FORGET PASSWORD

        def teacher_forget_password():
            def forget_update():
                den.destroy()
                def back2():
                    wet.destroy()
                    teacher_sign_in()
                def power():
                    use=user
                    p=entry_npas.get()
                    o=entry_cpas.get()
                    if p=="New password" and o=="Confirm password":
                        lable_nc=Label(wet,text="All field's are required !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nc.place(x=165,y=395)
                        lable_nc.after(2000,lambda:lable_nc.destroy())
                    elif p=="" or p=="New password":
                        lable_n=Label(wet,text="Enter new password !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_n.place(x=165,y=395)
                        lable_n.after(2000,lambda:lable_n.destroy())
                    elif o=="" or o=="Confirm password":
                        lable_c=Label(wet,text="Enter confirm password !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_c.place(x=157,y=395)
                        lable_c.after(2000,lambda:lable_c.destroy())
                    else:
                        if p==o:
                            query="update register set password='{}' where username='{}'".format(p,use)
                            cursor.execute(query)
                            deb.commit()
                            back2()
                        else:
                            lable_mo=Label(wet,text='New password and confirm password not matched !',
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_mo.place(x=60,y=395)
                            lable_mo.after(2000,lambda:lable_mo.destroy())

                #====================================new password
                def on_entrynpas(rock):
                    if entry_npas.get()=='New password':
                        entry_npas.delete(0,END)
                        entry_npas.config(show=('*'))
                def on_leavenpas(pock):
                    if entry_npas.get()=='':
                        entry_npas.config(show=(''))
                        entry_npas.insert(0,'New password')

                #==================================== new eye
                def hide1():
                    openneye.config(file="eye2.png")
                    entry_npas.config(show=('*'))
                    eyenButton.config(command=show1)

                def show1():
                    openneye.config(file="eye1.png")
                    entry_npas.config(show=(''))
                    eyenButton.config(command=hide1)
                #====================================password
                def on_entrycpas(rock):
                    if entry_cpas.get()=='Confirm password':
                        entry_cpas.delete(0,END)
                        entry_cpas.config(show=('*'))
                def on_leavecpas(pock):
                    if entry_cpas.get()=='':
                        entry_cpas.config(show=(''))
                        entry_cpas.insert(0,'Confirm password')

                #====================================eye
                def hide2():
                    openceye.config(file="eye2.png")
                    entry_cpas.config(show=('*'))
                    eyecButton.config(command=show2)

                def show2():
                    openceye.config(file="eye1.png")
                    entry_cpas.config(show=(''))
                    eyecButton.config(command=hide2)
                #====================================new password entry
                #===============================creating window
                wet=Tk()
                wet.title('FORGET PAGE')
                #wet.geometry('500x500+500+150')
                width =500
                height =500
                screen_width = wet.winfo_screenwidth()
                screen_height = wet.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                wet.geometry("%dx%d+%d+%d" % (width, height, x, y))
                wet.configure(bg='black')
                wet.resizable(0,0)
                #====================================photo import
                sop=PhotoImage(file='teacher.png')
                lableb=Label(wet,image=sop,bd=0,bg="black")
                lableb.place(x=177,y=20)
                #====================================requesting
                label2=Label(wet,text='Please enter your new password !',font=("Century Schoolbook L",15),
                            bg="black",fg="white")
                label2.place(x=105,y=250)
                #==================================back to sign in page
                button_back=Button(wet,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back2,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for save data in database
                button_done=Button(wet,text='Reset password',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=power,
                            cursor="hand2",bg="dodger blue",fg="black",border=0)
                button_done.place(x=150,y=430)
                #====================================title
                label1=Label(wet,text='Teacher Forget password',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="dodger blue")
                label1.place(x=50,y=180)
                #====================================new password entry
                entry_npas=Entry(wet,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_npas.place(x=130,y=300)
                entry_npas.insert(0,"New password")
                entry_npas.bind('<FocusIn>',on_entrynpas)
                entry_npas.bind('<FocusOut>',on_leavenpas)
                #==================================eye button
                openneye=PhotoImage(file="eye2.png")
                eyenButton=Button(wet,image=openneye,bd=0,bg='black',activebackground='black'
                                ,cursor='hand2',command=show1)
                eyenButton.place(x=380,y=300)
                #====================================confirm password entry
                entry_cpas=Entry(wet,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_cpas.place(x=130,y=350)
                entry_cpas.insert(0,"Confirm password")
                entry_cpas.bind('<FocusIn>',on_entrycpas)
                entry_cpas.bind('<FocusOut>',on_leavecpas)
                #==================================eye button
                openceye=PhotoImage(file="eye2.png")
                eyecButton=Button(wet,image=openceye,bd=0,bg='black',activebackground='black'
                                ,cursor='hand2',command=show2)
                eyecButton.place(x=380,y=350)
                #===============================mainloop
                wet.mainloop()

            def back1():
                den.destroy()
                teacher_sign_in()
            def search():
                global user
                name=entry_name.get().title()
                email=entry_email.get()
                user=entry_user.get()
                if name=="Name" and email=="Email" and user=="Username":
                    lable_up=Label(den,text="All field's are required !'",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=160,y=445)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif name=="" or name=="Name":
                    lable_name=Label(den,text='Enter your Name !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_name.place(x=180,y=445)   
                    lable_name.after(2000,lambda:lable_name.destroy())
                elif email=="" or email=="Email":
                    lable_email=Label(den,text='Enter your Email !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_email.place(x=180,y=445)   
                    lable_email.after(2000,lambda:lable_email.destroy())
                elif user=="" or user=="Username":
                    lable_user=Label(den,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=170,y=445)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                else:
                    query="select name,email,username from register where username='{}'".format(user)
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if name in i and user in i and email in i:
                            w=True
                        else:
                            w=False
                    if w==False:
                        lable_nok=Label(den,text='Enter correct data !'
                                        ,font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=180,y=445)
                        lable_nok.after(3000,lambda:lable_nok.destroy())
                    else:
                        forget_update()
            #====================================name
            def on_entryname(rock):
                if entry_name.get()=='Name':
                    entry_name.delete(0,END)

            def on_leavename(pock):
                if entry_name.get()=='':
                    entry_name.insert(0,'Name')
            #====================================email
            def on_entryemail(rock2):
                if entry_email.get()=='Email':
                    entry_email.delete(0,END)

            def on_leaveemail(pock2):
                if entry_email.get()=='':
                    entry_email.insert(0,'Email')
            #====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #====================================creating sign up page
            den=Tk()
            den.title('FORGET PAGE')
            #den.geometry('500x600+500+70')
            width =500
            height =600
            screen_width = den.winfo_screenwidth()
            screen_height = den.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            den.geometry("%dx%d+%d+%d" % (width, height, x, y))
            den.configure(bg='black')
            den.resizable(0,0)
            #====================================photo import
            sop=PhotoImage(file='teacher.png')
            lableb=Label(den,image=sop,bd=0,bg="black")
            lableb.place(x=177,y=20)
            #====================================title
            label1=Label(den,text='teacher Forget password',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="dodger blue")
            label1.place(x=50,y=180)
            #====================================requesting
            label2=Label(den,text='Please enter data for verification !',font=("Century Schoolbook L",15),
                        bg="black",fg="white")
            label2.place(x=105,y=250)
            #====================================name entry
            entry_name=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_name.place(x=130,y=300)
            entry_name.insert(0,"Name")
            entry_name.bind('<FocusIn>',on_entryname)
            entry_name.bind('<FocusOut>',on_leavename)
            #====================================email entry
            entry_email=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_email.place(x=130,y=350)
            entry_email.insert(0,"Email")
            entry_email.bind('<FocusIn>',on_entryemail)
            entry_email.bind('<FocusOut>',on_leaveemail)
            #====================================username entry
            entry_user=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=400)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #====================================back to sign in
            button_create=Button(den,text='Back to sign in',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=back1,
                                bg="black",fg="dodger blue",border=0)
            button_create.place(x=200,y=520)
            #==================================back to sign in page
            button_back=Button(den,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back1,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for search data from database
            button_done=Button(den,text='Enter',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="dodger blue",fg="black",border=0)
            button_done.place(x=150,y=480)
            #====================================mainloop
            den.mainloop()

#======================================================TEACHER SIGN UP

        def teacher_sign_up():
            def back():
                cher.destroy()
                teacher_sign_in()
            def search():
                name=entry_name.get().title()
                phone=entry_phone.get()
                email=entry_email.get()
                sex=entry_sex.get()
                user=entry_user.get()
                pas=entry_pas.get()
                date=wox
                tame=time
                tepy="Teacher"
                if name=="Name" and phone=="Phone number" and email=="Email" and sex=="Gender" and user=="Username" and pas=="Password":
                    lable_up=Label(cher,text="All field's are required !'",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=160,y=580)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif name=="Name" or name=="":
                    lable_name=Label(cher,text='Enter your Name !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_name.place(x=180,y=580)   
                    lable_name.after(2000,lambda:lable_name.destroy())
                elif phone=="Phone number" or phone=="":
                    lable_phone=Label(cher,text='Enter your Phone number !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_phone.place(x=147,y=580)   
                    lable_phone.after(2000,lambda:lable_phone.destroy())
                elif email=="Email" or email=="":
                    lable_email=Label(cher,text='Enter your Email !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_email.place(x=180,y=580)   
                    lable_email.after(2000,lambda:lable_email.destroy())
                elif sex=="Gender" or sex=="":
                    lable_sex=Label(cher,text='Enter your Gender !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_sex.place(x=180,y=580)   
                    lable_sex.after(2000,lambda:lable_sex.destroy())
                elif user=="Username" or user=="":
                    lable_user=Label(cher,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=170,y=580)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                elif pas=="Password" or pas=="":
                    lable_pas=Label(cher,text='Enter your password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_pas.place(x=170,y=580)   
                    lable_pas.after(2000,lambda:lable_pas.destroy())
                else:
                    query="select username from register"
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if user in i:
                            w=True
                            break
                        else:
                            w=False
                    if w==True:
                        lable_nok=Label(cher,text='Username alredy exist !',
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=160,y=580)   
                        lable_nok.after(2000,lambda:lable_nok.destroy())   
                    else:
                        if name.replace(" ", "").isalpha():
                            if sex.isalpha():
                                if phone.isdigit():
                                    if "@gmail.com" in email or "@yahoo.com" in email or "@outlook.com" in email:
                                        if len(phone) == 10:
                                            phoneno="+91"+phone
                                            query="Insert into register values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,phoneno,email,sex,user,pas,date,tame,tepy)
                                            cursor.execute(query)
                                            deb.commit()
                                            back()
                                        else:
                                            lable_na=Label(cher,text="Please enter number in 10 digit !",
                                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                            lable_na.place(x=125,y=585)
                                            lable_na.after(2000,lambda:lable_na.destroy())
                                    else:
                                        lable_no=Label(cher,text="Enter valid in email !",
                                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                        lable_no.place(x=165,y=585)
                                        lable_no.after(2000,lambda:lable_no.destroy())
                                else:
                                    lable_no=Label(cher,text="Enter number in integer !",
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                    lable_no.place(x=153,y=585)
                                    lable_no.after(2000,lambda:lable_no.destroy()) 
                            else:
                                lable_no=Label(cher,text="Enter gender in alphabet!",
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_no.place(x=153,y=585)
                                lable_no.after(2000,lambda:lable_no.destroy()) 
                        else:
                            lable_no=Label(cher,text="Enter name in alphabet !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_no.place(x=155,y=585)
                            lable_no.after(2000,lambda:lable_no.destroy())  
            #====================================name
            def on_entryname(rock):
                if entry_name.get()=='Name':
                    entry_name.delete(0,END)

            def on_leavename(pock):
                if entry_name.get()=='':
                    entry_name.insert(0,'Name')
            #====================================phone
            def on_entryphone(rock1):
                if entry_phone.get()=='Phone number':
                    entry_phone.delete(0,END)

            def on_leavephone(pock1):
                if entry_phone.get()=='':
                    entry_phone.insert(0,'Phone number')
            #====================================email
            def on_entryemail(rock2):
                if entry_email.get()=='Email':
                    entry_email.delete(0,END)

            def on_leaveemail(pock2):
                if entry_email.get()=='':
                    entry_email.insert(0,'Email')
            #====================================gender
            def on_entrysex(rock3):
                if entry_sex.get()=='Gender':
                    entry_sex.delete(0,END)

            def on_leavesex(pock3):
                if entry_sex.get()=='':
                    entry_sex.insert(0,'Gender')
            #====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #====================================password
            def on_entrypas(rock):
                if entry_pas.get()=='Password':
                    entry_pas.delete(0,END)
                    entry_pas.config(show=('*'))
            def on_leavepas(pock):
                if entry_pas.get()=='':
                    entry_pas.config(show=(''))
                    entry_pas.insert(0,'Password')

            #====================================eye
            def hide():
                openeye.config(file="eye2.png")
                entry_pas.config(show=('*'))
                eyeButton.config(command=show)

            def show():
                openeye.config(file="eye1.png")
                entry_pas.config(show=(''))
                eyeButton.config(command=hide)
            #====================================creating sign up page
            cher=Tk()
            cher.title('SIGN IN PAGE')
            #cher.geometry('500x700+500+70')
            width =500
            height =700
            screen_width = cher.winfo_screenwidth()
            screen_height = cher.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            cher.geometry("%dx%d+%d+%d" % (width, height, x, y))
            cher.configure(bg='black')
            cher.resizable(0,0)
            #====================================photo import
            sop=PhotoImage(file='teacher.png')
            lableb=Label(cher,image=sop,bd=0,bg="black")
            lableb.place(x=177,y=20)
            #====================================title
            label1=Label(cher,text='Teacher Sign up',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="dodger blue")
            label1.place(x=127,y=180)
            #====================================requesting
            label2=Label(cher,text='Please enter your data to Sign up',font=("Century Schoolbook L",14),
                        bg="black",fg="white")
            label2.place(x=110,y=240)
            #====================================name entry
            entry_name=Entry(cher,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_name.place(x=130,y=290)
            entry_name.insert(0,"Name")
            entry_name.bind('<FocusIn>',on_entryname)
            entry_name.bind('<FocusOut>',on_leavename)
            #====================================phone no entry
            entry_phone=Entry(cher,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_phone.place(x=130,y=340)
            entry_phone.insert(0,"Phone number")
            entry_phone.bind('<FocusIn>',on_entryphone)
            entry_phone.bind('<FocusOut>',on_leavephone)
            label4=Label(cher,text='+91',font=("Microsoft YeHei UI Light",15,"bold"),bg="black",fg="white")
            label4.place(x=85,y=340)
            #====================================email entry
            entry_email=Entry(cher,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_email.place(x=130,y=390)
            entry_email.insert(0,"Email")
            entry_email.bind('<FocusIn>',on_entryemail)
            entry_email.bind('<FocusOut>',on_leaveemail)
            #====================================gender entry
            #====================================Combobox creation
            n = StringVar()
            entry_sex=ttk.Combobox(cher, width = 20,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = n)
            #====================================Adding combobox drop down list
            entry_sex['values'] = ('Male',
                                    'Female',
                                    'Others')
            entry_sex.current()
            entry_sex.place(x=130,y=440)
            entry_sex.insert(0,"Gender")
            entry_sex.bind('<FocusIn>',on_entrysex)
            entry_sex.bind('<FocusOut>',on_leavesex)
            #====================================username entry
            entry_user=Entry(cher,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=490)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #====================================password entry
            entry_pas=Entry(cher,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_pas.place(x=130,y=540)
            entry_pas.insert(0,"Password")
            entry_pas.bind('<FocusIn>',on_entrypas)
            entry_pas.bind('<FocusOut>',on_leavepas)
            #==================================eye button
            openeye=PhotoImage(file="eye2.png")
            eyeButton=Button(cher,image=openeye,bd=0,bg='black',activebackground='black'
                            ,cursor='hand2',command=show)
            eyeButton.place(x=380,y=540)
            #==================================back to selection page
            button_back=Button(cher,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for save data in database
            button_done=Button(cher,text='Sign up',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="dodger blue",fg="black",border=0)
            button_done.place(x=150,y=615)
            #==================================create account
            labed=Label(cher,text="I have account?",font=("Microsoft YeHei UI Light",11)
                        ,bg="black",fg="white")
            labed.place(x=170,y=660)
            button_create=Button(cher,text='Sign in',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=back,
                                bg="black",fg="dodger blue",border=0)
            button_create.place(x=280,y=660)
            #===================================mainloop
            cher.mainloop()

#======================================================TEACHER SIGN IN

        def teacher_sign_in():
            def call_sign_up():
                tea.destroy()
                teacher_sign_up()
            def call_forget():
                tea.destroy()
                teacher_forget_password()
            def back():
                tea.destroy()
                panel()
            #=====================================checking data from table
            def search():
                user=entry_user.get()
                pas=entry_passw.get()
                tepy="Teacher"
                if user=="Username" and pas=="Password":
                    lable_up=Label(tea,text='Enter your username & password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=120,y=510)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif user=="Username":
                    lable_user=Label(tea,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=165,y=510)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                elif pas=="Password":
                    lable_pas=Label(tea,text='Enter your password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_pas.place(x=165,y=510)   
                    lable_pas.after(2000,lambda:lable_pas.destroy())
                else:
                    query= "SELECT type FROM register WHERE username = '{}'".format(user)
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if tepy in i:
                            w=True
                            break
                        else:
                            w=False
                    if w==False:
                        lable_nok=Label(tea,text='You are not teacher !',
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=170,y=510)   
                        lable_nok.after(2000,lambda:lable_nok.destroy())   
                    else:
                        query="select username,password from register"
                        cursor.execute(query)
                        data=cursor.fetchall()
                        w=()
                        for i in data:
                            if user in i and pas in i:
                                w=True
                                break
                            else:
                                w=False
                        if w==True:
                            global tpcolumn1_value #, tpcolumn2_value
                            name=user
                            cursor.execute("SELECT name FROM register WHERE username = '{}'".format(name))
                            row = cursor.fetchone()
                            tpcolumn1_value = row[0]
                            #tpcolumn2_value = row[1]
                            tea.destroy()
                            #============================creating welcome page
                            wel = Tk()
                            wel.title("WELCOME PAGE")
                            wel.geometry('600x305+450+230')
                            wel.configure(bg="black")
                            #=============================importing photo
                            do=PhotoImage(file='welcome.png')
                            lable=Label(wel,image=do,bd=0,bg="black")
                            lable.place(x=0,y=0)
                            #=============================destroy windlow after 2 second
                            wel.after(2000,lambda:wel.destroy())
                            wel.mainloop()
                            teacher_cms_page()

            #===============================================================================================================================    
                        else:
                            lable_nok=Label(tea,text='Enter correct username or password !',
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_nok.place(x=110,y=510)   
                            lable_nok.after(2000,lambda:lable_nok.destroy())
            #=====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #=====================================password
            def on_entrypassw(rock2):
                if entry_passw.get()=='Password':
                    entry_passw.delete(0,END)
                    entry_passw.config(show=('*'))

            def on_leavepassw(pock):
                if entry_passw.get()=='':
                    entry_passw.config(show=(''))
                    entry_passw.insert(0,'Password')
            #====================================eye
            def hide():
                openeye.config(file="eye2.png")
                entry_passw.config(show=('*'))
                eyeButton.config(command=show)

            def show():
                openeye.config(file="eye1.png")
                entry_passw.config(show=(''))
                eyeButton.config(command=hide)

            tea=Tk()
            tea.title('SIGN IN PAGE')
            #tea.geometry('500x700+500+70')
            width =500
            height =700
            screen_width = tea.winfo_screenwidth()
            screen_height = tea.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            tea.geometry("%dx%d+%d+%d" % (width, height, x, y))
            tea.config(bg='black')
            tea.resizable(0,0)
            #====================================photo import
            df=PhotoImage(file='teacher.png')
            labler=Label(tea,image=df,bd=0,bg="black")
            labler.place(x=177,y=70)
            #====================================title
            label1=Label(tea,text='Teacher Sign in',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="dodger blue")
            label1.place(x=127,y=260)
            #====================================requesting
            label2=Label(tea,text='Please enter your Username & Password',font=("Century Schoolbook L",13),
                        bg="black",fg="white")
            label2.place(x=100,y=325)
            #====================================username entry
            entry_user=Entry(tea,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=380)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #===================================password entry
            entry_passw=Entry(tea,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_passw.place(x=130,y=440)
            entry_passw.insert(0,"Password")
            entry_passw.bind('<FocusIn>',on_entrypassw)
            entry_passw.bind('<FocusOut>',on_leavepassw)
            #==================================eye button
            openeye=PhotoImage(file="eye2.png")
            eyeButton=Button(tea,image=openeye,bd=0,bg='black',activebackground='black'
                            ,cursor='hand2',command=show)
            eyeButton.place(x=380,y=441)
            #==================================button for search data from database
            button_done=Button(tea,text='Sign in',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="dodger blue",fg="black",border=0)
            button_done.place(x=150,y=550)
            #==================================forget password button
            button_forget=Button(tea,text="Forget password ?",font=("Algeria",11),
                                width=16,pady=3,
                                cursor="hand2",
                                activebackground="black",
                                command=call_forget,
                                bg="black",fg="dodger blue",
                                border=0)
            button_forget.place(x=240,y=470)
            #==================================create account
            labed=Label(tea,text="Don't have an account?",font=("Microsoft YeHei UI Light",11)
                        ,bg="black",fg="white")
            labed.place(x=145,y=595)
            button_create=Button(tea,text='Sign up',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=call_sign_up,
                                bg="black",fg="dodger blue",border=0)
            button_create.place(x=305,y=595)
            #==================================back to selection page
            button_back=Button(tea,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #====================================mainloop
            tea.mainloop()

#======================================================TEACHER VERIFICATION CODE

        def verify():
            #=========================================checking
            def call():
                ver.destroy()
                teacher_sign_in()
            def back1():
                ver.destroy()
                panel()
            def trys():
                ch=entry_vamu.get()
                if ch=="admin123":
                    labev=Label(ver,text="Verification successful!",font=("Microsoft YeHei UI Light",13)
                                ,bg="black",fg="green2")
                    labev.place(x=165,y=170)
                    call()
                elif ch=="Verification code" or ch=="":
                    labee=Label(ver,text="Enter your verification code!",font=("Microsoft YeHei UI Light",13)
                                ,bg="black",fg="red")
                    labee.place(x=145,y=170)
                    labee.after(3000,lambda:labee.destroy())
                else:
                    labex=Label(ver,text="Verification code is wrong!",font=("Microsoft YeHei UI Light",13)
                                ,bg="black",fg="red")
                    labex.place(x=155,y=170)
                    labex.after(3000,lambda:labex.destroy())
            #=====================================verification
            def on_entryvamu(rock):
                entry_vamu.config(show=('*'))
            #=====================================creating checking window
            ver=Tk()
            ver.title('CHECKING PAGE')
            #ver.geometry('500x300+500+250')
            width =500
            height =300
            screen_width = ver.winfo_screenwidth()
            screen_height = ver.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            ver.geometry("%dx%d+%d+%d" % (width, height, x, y))
            ver.config(bg='black')
            ver.resizable(0,0)
            #=====================================photo import
            te=PhotoImage(file="check.png")
            lablet=Label(ver,image=te,bd=0,bg="black")
            lablet.place(x=0,y=0)
            #=====================================verify entry
            entry_vamu=Entry(ver,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_vamu.place(x=130,y=200)
            entry_vamu.bind('<FocusIn>',on_entryvamu)
            #==================================button for search data from database
            button_done=Button(ver,text='Verify!',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=trys,
                        cursor="hand2",bg="dodger blue",fg="black",border=0)
            button_done.place(x=152,y=250)
            #==================================back to selection page
            button_back=Button(ver,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back1,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================mainloop
            ver.mainloop()
        verify()

#=====================================================CALLING FUNCTION TO START TEACHER LOGIN PAGE

    teacher_login_page()

#======================================================STUDENT PANEL 

def student():


    def student_cms_page():
        global st_special2,st_special1
        st_special1=tpcolumn2_value
        st_special2=(tpcolumn1_value.split()[0])
        #=================================================STUDENT SORT

        def student_sort_page():
            def ret():
                sortmain()
            def sortmain():
                def Ascending():
                    dj=entry_type.get()
                    if dj=="Please select your choice !" or dj=="":
                        label3=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label3.place(x=150,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif dj=="name" or dj=="surname" or dj=="phone" or dj=="dob" or dj=="label" or dj=="email" or dj=="sex" or dj=="address":
                        def bye():
                            ase.destroy()
                            ret()
                        def p():
                            sot.destroy()
                            query_za = "SELECT * FROM contacts WHERE label = '{}' ORDER BY {}".format(st_special1, dj)
                            cursor.execute(query_za)

                            data_za=cursor.fetchall()
                            global c
                            c = 0
                            for record in data_za:
                                if c % 2 == 0:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                                else:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                                c += 1
                        ase=Tk()
                        width =1355
                        height =570
                        screen_width = ase.winfo_screenwidth()
                        screen_height = ase.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        ase.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        ase.config(bg='dodger blue')
                        ase.resizable(0,0)

                        label_text = "Sorting contacts in order by {} format".format(dj)
                        label1 = Label(ase, text=label_text, font=("Century Schoolbook L", 20, "bold"), bg="dodger blue", fg="black")
                        label1.place(x=350)


                        t=Frame(ase)
                        t.place(x=5,y=40)

                        #==================================back to cms page
                        button_back=Button(ase,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="dodger blue",
                                    command=bye,
                                    cursor="hand2",bg="dodger blue",fg="black",border=0)
                        button_back.place(x=0,y=0)

                        yscroll=Scrollbar(t,orient=VERTICAL)
                        yscroll.pack(side=LEFT,fill=Y)
                        
                        columns = ("firstname", "surname", "phoneNo", "DOB", "label",  "email", "sex", "address")
                        my_tree = ttk.Treeview(t,height=25, show="headings",selectmode="browse",
                                                columns=columns,yscrollcommand=yscroll.set)
                                                
                        my_tree.pack()

                        yscroll.config(command=my_tree.yview)

                        my_tree.column("firstname", anchor=CENTER, width=85, minwidth=85)
                        my_tree.column("surname", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("phoneNo", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("DOB", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("label", anchor=CENTER, width=150, minwidth=150)
                        my_tree.column("sex", anchor=CENTER, width=50, minwidth=50)
                        my_tree.column("email", anchor=CENTER, width=250, minwidth=250)
                        my_tree.column("address", anchor=CENTER, width=490, minwidth=490)

                        my_tree.heading("firstname", text="Firstname", anchor=CENTER)
                        my_tree.heading("surname", text="Surname", anchor=CENTER)
                        my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
                        my_tree.heading("DOB", text="DOB", anchor=CENTER)
                        my_tree.heading("label", text="Label", anchor=CENTER)
                        my_tree.heading("sex", text="Sex", anchor=CENTER)
                        my_tree.heading("email", text="Email", anchor=CENTER)
                        my_tree.heading("address", text="Address", anchor=CENTER)

                        # Define styles for treeview table
                        style = ttk.Style()
                        style.theme_use("clam")  # Choose a theme ('clam' is just an example)

                        # Configure the header style
                        style.configure("Treeview.Heading",
                                        font=("Century Gothic", 12, "bold"),bg="black",
                                        foreground="white")

                        # Configure the row style
                        style.configure("Treeview",
                                        font=("Century Gothic", 11),
                                        background="white",
                                        foreground="black")
                        
                        style.map('Treeview', background=[('selected', 'dodger blue')])

                        my_tree.tag_configure('oddrow', background='white')
                        my_tree.tag_configure('evenrow', background='dodger blue')
                    
                        p()
                        ase.mainloop()
                    else:
                        label2=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label2.place(x=150,y=190)
                        label2.after(2000,lambda:label2.destroy())

                def Descending():
                    dj=entry_type.get()
                    if dj=="Please select your choice !" or dj=="":
                        label3=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label3.place(x=150,y=190)
                        label3.after(2000,lambda:label3.destroy())
                    elif dj=="name" or dj=="surname" or dj=="phone" or dj=="dob" or dj=="label" or dj=="email" or dj=="sex" or dj=="address":
                        def bye():
                            des.destroy()
                            sortmain()
                        def p():
                            sot.destroy()
                            query_za = "SELECT * FROM contacts WHERE label = '{}' ORDER BY {} DESC".format(st_special1, dj)
                            cursor.execute(query_za)

                            data_za=cursor.fetchall()
                            global c
                            c = 0
                            for record in data_za:
                                if c % 2 == 0:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                                else:
                                    my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                                c += 1
                        des=Tk()
                        width =1355
                        height =570
                        screen_width = des.winfo_screenwidth()
                        screen_height = des.winfo_screenheight()
                        x = (screen_width/2) - (width/2)
                        y = (screen_height/2) - (height/2)
                        des.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        des.config(bg='lime green')
                        des.resizable(0,0)

                        label_text = "Sorting contacts in descending order by {} format".format(dj)
                        label1 = Label(des, text=label_text, font=("Century Schoolbook L", 20, "bold"), bg="lime green", fg="black")
                        label1.place(x=350)


                        t=Frame(des)
                        t.place(x=5,y=40)

                        #==================================back to cms page
                        button_back=Button(des,text='←Back',font=("Algeria",13,"bold"),
                                    width=7,pady=3,activebackground="lime green",
                                    command=bye,
                                    cursor="hand2",bg="lime green",fg="black",border=0)
                        button_back.place(x=0,y=0)

                        yscroll=Scrollbar(t,orient=VERTICAL)
                        yscroll.pack(side=LEFT,fill=Y)
                        
                        columns = ("firstname", "surname", "phoneNo", "DOB", "label",  "email", "sex", "address")
                        my_tree = ttk.Treeview(t,height=25, show="headings",selectmode="browse",
                                                columns=columns,yscrollcommand=yscroll.set)
                                                
                        my_tree.pack()

                        yscroll.config(command=my_tree.yview)

                        my_tree.column("firstname", anchor=CENTER, width=85, minwidth=85)
                        my_tree.column("surname", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("phoneNo", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("DOB", anchor=CENTER, width=100, minwidth=100)
                        my_tree.column("label", anchor=CENTER, width=150, minwidth=150)
                        my_tree.column("sex", anchor=CENTER, width=50, minwidth=50)
                        my_tree.column("email", anchor=CENTER, width=250, minwidth=250)
                        my_tree.column("address", anchor=CENTER, width=490, minwidth=490)

                        my_tree.heading("firstname", text="Firstname", anchor=CENTER)
                        my_tree.heading("surname", text="Surname", anchor=CENTER)
                        my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
                        my_tree.heading("DOB", text="DOB", anchor=CENTER)
                        my_tree.heading("label", text="Label", anchor=CENTER)
                        my_tree.heading("sex", text="Sex", anchor=CENTER)
                        my_tree.heading("email", text="Email", anchor=CENTER)
                        my_tree.heading("address", text="Address", anchor=CENTER)

                        # Define styles for treeview table
                        style = ttk.Style()
                        style.theme_use("clam")  # Choose a theme ('clam' is just an example)

                        # Configure the header style
                        style.configure("Treeview.Heading",
                                        font=("Century Gothic", 12, "bold"),bg="black",
                                        foreground="white")

                        # Configure the row style
                        style.configure("Treeview",
                                        font=("Century Gothic", 11),
                                        background="white",
                                        foreground="black")
                        
                        style.map('Treeview', background=[('selected', 'lime green')])

                        my_tree.tag_configure('oddrow', background='white')
                        my_tree.tag_configure('evenrow', background='lime green')
                    
                        p()
                        des.mainloop()
                    else:
                        label2=Label(sot,bg="black",fg="red",
                                    font=("Microsoft YeHei UI Light",12,"bold"),text="Please select your choice !")
                        label2.place(x=150,y=190)
                        label2.after(2000,lambda:label2.destroy())

                def back():
                    sot.destroy()
                    student_main()

                sot=Tk()
                sot.title('SORTING PAGE')
                width =500
                height =300
                screen_width = sot.winfo_screenwidth()
                screen_height = sot.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                sot.geometry("%dx%d+%d+%d" % (width, height, x, y))
                sot.config(bg='black')
                sot.resizable(0,0)
                #====================================title
                labeld=Label(sot,text='Sort contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="gold")
                labeld.place(x=150,y=15)
                #====================================request
                labeld=Label(sot,text='Please select your choice !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=120,y=80)
                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select your choice!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select your choice!')
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(sot, width = 30,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('name',
                                        'surname',
                                        'phone',
                                        'dob',
                                        'label',
                                        'email',
                                        'sex',
                                        'address')
                entry_type.current()
                entry_type.place(x=75,y=140)
                entry_type.insert(0,"Select your choice!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(sot,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for decending
                button_done=Button(sot,text='Descending',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=Descending,
                            cursor="hand2",bg="lime green",fg="black",border=0)
                button_done.place(x=265,y=230)
                #==================================button for accending
                button_done=Button(sot,text='Ascending',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=Ascending,
                            cursor="hand2",bg="dodger blue",fg="black",border=0)
                button_done.place(x=35,y=230)
                #====================================mainloop 
                sot.mainloop()
            sortmain()

        #=================================================STUDENT SEARCH

        def student_search_page():
            def popo():
                def s2cms():
                    search2.destroy()
                    popo()
                def searchmain():
                    c=entry_s.get().title()
                    global search2
                    ch=entry_type.get()
                    if ch=='Contact name':
                        if c=="Search..." or c=="":
                            label3=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name !")
                            label3.place(x=170,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        elif c.isdigit():
                            label3=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact name in alphabet !")
                            label3.place(x=130,y=190)
                            label3.after(2000,lambda:label3.destroy())
                        else:
                            query1="select name , label from contacts"
                            cursor.execute(query1)
                            data1=cursor.fetchall()
                            for i in data1:
                                if c in i and st_special1 in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                src.destroy()
                                search2=Tk()
                                width =925
                                height =520
                                screen_width = search2.winfo_screenwidth()
                                screen_height = search2.winfo_screenheight()
                                x = (screen_width/2) - (width/2)
                                y = (screen_height/2) - (height/2)
                                search2.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                search2.title('SEARCH CONTACT PAGE')
                                search2.configure(bg='black')
                                search2.resizable(False,False)
                                button_not=Button(search2,text='←Back',
                                                font=("Algeria",13,"bold"),
                                                cursor="hand2",
                                                activebackground="black",
                                                command=s2cms,
                                                bg="black",fg="white",bd=0)
                                button_not.place(x=0,y=0)
                                o=c.upper()
                                label4=Label(search2,bg="black",fg="peach puff",
                                            text="DATA OF "+o+" CONTACT IS.....",font=("Microsoft YeHei UI Light",25,"bold"))
                                label4.place(x=150,y=10)
                                def o(p):
                                    l=["Firstname","Surname","Phone number","Date of birth","Label","Email","Gender","Address"]
                                    for j in p:
                                        h=0
                                        o=90
                                        for i in j:
                                            Label(search2,text=l[h]+" : "+i,bg="black",
                                                fg="white",font=("Microsoft YeHei UI Light",18,"bold")).place(x=30,y=o)
                                            o+=45
                                            h+=1
                                cursor.execute("select * from contacts where name='{}' and label='{}'".format(c, st_special1))
                                data_name = cursor.fetchall()

                                o(data_name)
                                search2.mainloop()
                            else:
                                label=Label(src,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact name does not exist !")
                                label.place(x=105,y=190)
                                label.after(2000,lambda:label.destroy())
                                                        

                    elif ch=='Contact phone number':
                        pn="+91"+c
                        if c=="Search..." or c=="":
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone number !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif c.isalpha():
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in integer !")
                            label2.place(x=135,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        elif len(c) != 10:
                            label2=Label(src,bg="black",fg="red",
                                        font=("Microsoft YeHei UI Light",12,"bold"),text="Enter contact phone in 10 digit !")
                            label2.place(x=130,y=190)
                            label2.after(2000,lambda:label2.destroy())
                        else:
                            query2="select phone , label from contacts"
                            cursor.execute(query2)
                            data2=cursor.fetchall()
                            for i in data2:
                                if pn in i and st_special1 in i:
                                    w=True
                                    break
                                else:
                                    w=False
                            if w==True:
                                    src.destroy()
                                    search2=Tk()
                                    width =925
                                    height =520
                                    screen_width = search2.winfo_screenwidth()
                                    screen_height = search2.winfo_screenheight()
                                    x = (screen_width/2) - (width/2)
                                    y = (screen_height/2) - (height/2)
                                    search2.geometry("%dx%d+%d+%d" % (width, height, x, y))
                                    search2.title('SEARCH CONTACT PAGE')
                                    search2.configure(bg='black')
                                    search2.resizable(False,False)
                                    button_not=Button(search2,text='←Back',
                                                    font=("Algeria",13,"bold"),
                                                    cursor="hand2",
                                                    activebackground="black",
                                                    command=s2cms,
                                                    bg="black",fg="white",bd=0)
                                    button_not.place(x=0,y=0)
                                    label4=Label(search2,bg="black",fg="peach puff",
                                                text="DATA OF "+pn+" CONTACT IS.....",font=("Microsoft YeHei UI Light",25,"bold"))
                                    label4.place(x=150,y=10)
                                    def d(p):
                                        l=["Firstname","Surname","Phone number","Date of birth","Label","Email","Gender","Address"]
                                        for j in p:
                                            h=0
                                            o=90
                                            for i in j:
                                                Label(search2,bg="black",fg="white",
                                                    font=("Microsoft YeHei UI Light",18,"bold"),text=l[h]+" : "+i).place(x=30,y=o)
                                                o+=45
                                                h+=1
                                    cursor.execute("select * from contacts where phone='{}' and label='{}'".format(pn, st_special1))
                                    data_phone = cursor.fetchall()

                                    d(data_phone) 
                                    search2.mainloop()
                            else:
                                label=Label(src,bg="black",fg="red",
                                            font=("Microsoft YeHei UI Light",12,"bold"),text="Entered contact phone number does not exist!")
                                label.place(x=80,y=190)
                                label.after(2000,lambda:label.destroy())
            
                    else:
                        label1=Label(src,bg="black",fg="red",font=("Microsoft YeHei UI Light",12,"bold")
                                    ,text="Select which type of data to search ?")
                        label1.place(x=115,y=190)
                        label1.after(2000,lambda:label1.destroy())

                def back():
                    src.destroy()
                    student_main()

                src=Tk()
                src.title('SEARCH PAGE')
                width =500
                height =300
                screen_width = src.winfo_screenwidth()
                screen_height = src.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                src.geometry("%dx%d+%d+%d" % (width, height, x, y))
                src.config(bg='black')
                src.resizable(0,0)
                #====================================title
                labeld=Label(src,text='Search contact',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="peach puff")
                labeld.place(x=135,y=15)
                #====================================request
                labeld=Label(src,text='Please enter contact Name or Phone number !',font=("Century Schoolbook L",15,"bold"),
                            bg="black",fg="white")
                labeld.place(x=30,y=80)
                #====================================type
                def on_entryt(rock):
                    if entry_type.get()=='Select type!':
                        entry_type.delete(0,END)

                def on_leavet(pock):
                    if entry_type.get()=='':
                        entry_type.insert(0,'Select type!')
                #====================================search
                def on_entryse(rock1):
                    if entry_s.get()=='Search...':
                        entry_s.delete(0,END)

                def on_leavese(pock1):
                    if entry_s.get()=='':
                        entry_s.insert(0,'Search...')
                #====================================search
                entry_s=Entry(src,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_s.place(x=30,y=140)
                entry_s.insert(0,"Search...")
                entry_s.bind('<FocusIn>',on_entryse)
                entry_s.bind('<FocusOut>',on_leavese)
                #====================================type of data
                w = StringVar()
                entry_type=ttk.Combobox(src, width = 15,font=("Microsoft YeHei UI Light",15),
                                            justify='center', textvariable = w)
                #====================================Adding combobox drop down list
                entry_type['values'] = ('Contact name',
                                        'Contact phone number')
                entry_type.current()
                entry_type.place(x=280,y=140)
                entry_type.insert(0,"Select type!")
                entry_type.bind('<FocusIn>',on_entryt)
                entry_type.bind('<FocusOut>',on_leavet)
                #==================================back to cms page
                button_back=Button(src,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for delete data in database
                button_done=Button(src,text='Search it!',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=searchmain,
                            cursor="hand2",bg="peach puff",fg="black",border=0)
                button_done.place(x=150,y=230)
                #====================================mainloop 
                src.mainloop()
            popo()

        #=================================================STUDENT PRINT

        def student_print_page():
            def tata():
                ganga.destroy()
                student_main()
            def aim():
                fj=entry_s.get().title()
                if fj=='' or fj=='File Name':
                    label6=Label(ganga,bg="black",fg="red",
                                font=("Microsoft YeHei UI Light",12,"bold"),text="Please enter your file name !")
                    label6.place(x=135,y=190)
                    label6.after(2000,lambda:label6.destroy())
                else:
                    # Execute a query to fetch data from the 'contacts' table
                    query = "SELECT * FROM contacts WHERE label = '{}'".format(st_special1)
                    cursor.execute(query)
                    data = cursor.fetchall()

                    # Ask the user for a file name
                    output_file = fj + '.txt'

                    # Define the widths for each column
                    column_widths = [25, 15, 15, 15, 30, 10, 30]

                    # Create a format string for each row based on column widths
                    format_string = ' | '.join('{{:<{}}}'.format(width) for width in column_widths)

                    # Write data to the text file with headings and formatted rows
                    with open(output_file, 'w') as file:
                        headings = ["Name", "Phone Number", "Date of Birth", "Label", "Email", "Sex", "Address"]
                        separator_line = '-+-'.join('-' * width for width in column_widths)
                        file.write(format_string.format(*headings) + '\n')
                        file.write(separator_line + '\n')
                        for row in data:
                            name = f"{row[0]} {row[1]}".ljust(column_widths[0])
                            formatted_row = [name] + list(str(item).ljust(width) for item, width in zip(row[2:], column_widths[1:]))
                            file.write(format_string.format(*formatted_row) + '\n')

                    # Close the database connection
                    ganga.destroy()
                    student_main()
                        

            ganga=Tk()
            ganga.title('PRINT PAGE')
            width =500
            height =300
            screen_width = ganga.winfo_screenwidth()
            screen_height = ganga.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            ganga.geometry("%dx%d+%d+%d" % (width, height, x, y))
            ganga.config(bg='black')
            ganga.resizable(0,0)
            #====================================title
            labeld=Label(ganga,text='Print contact',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="cyan")
            labeld.place(x=140,y=15)
            #====================================request
            labeld=Label(ganga,text='Please enter your file name to save data !',font=("Century Schoolbook L",15,"bold"),
                        bg="black",fg="white")
            labeld.place(x=50,y=80)
            #====================================file name
            def on_entryse(rock1):
                if entry_s.get()=='File Name':
                    entry_s.delete(0,END)

            def on_leavese(pock1):
                if entry_s.get()=='':
                    entry_s.insert(0,'File Name')
            #====================================file name
            entry_s=Entry(ganga,width=30,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_s.place(x=75,y=140)
            entry_s.insert(0,"File Name")
            entry_s.bind('<FocusIn>',on_entryse)
            entry_s.bind('<FocusOut>',on_leavese)
            #==================================back to cms page
            button_back=Button(ganga,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=tata,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for delete data in database
            button_done=Button(ganga,text='Print it!',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=aim,
                        cursor="hand2",bg="cyan",fg="black",border=0)
            button_done.place(x=140,y=230)
            ganga.mainloop()

        #=================================================STUDENT MAIN PAGE

        def student_main():
            def sort():
                main.destroy()
                student_sort_page()
            def search():
                main.destroy()
                student_search_page()
            def prin():
                main.destroy()
                student_print_page()
            def back():
                main.destroy()
                panel()
            #=================================================main window 
            main=Tk()
            main.title('STUDENT MAIN PAGE OF CONTACT MANAGEMENT SYSTEM')
            width =1475
            height =705
            screen_width = main.winfo_screenwidth()
            screen_height = main.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            main.geometry("%dx%d+%d+%d" % (width, height, x, y))
            main.configure(bg='black')
            main.resizable(0,0)
            #=================================================upper frame
            frameu=Frame(main,width=1465,height=60,bg="grey93",bd=0)
            frameu.place(x=5,y=5)
            #====================================photo import
            h=PhotoImage(file='healding.png')
            lablef=Label(frameu,image=h,bd=0,bg="grey93")
            lablef.place(x=0,y=0)
            #====================================photo import
            sm=PhotoImage(file='smain.png')
            lableb=Label(frameu,image=sm,bd=0,bg="grey93")
            lableb.place(x=1400,y=2)
            #===================================hi label
            labelh=Label(frameu,text=("Hi! "+st_special2),font=("Century Schoolbook L",20,"bold"),
                            bg="grey93",fg="black")
            labelh.place(x=1100,y=10)
            #===================================menu
            menubutton = Menubutton(frameu, text='▼')  # Unicode for downward arrow
            menu = Menu(menubutton, tearoff=0,activebackground="black")
            menu.add_command(label='Logout',command=back)
            menubutton.config(menu=menu)
            menubutton.place(x=1375,y=15)
            #=================================================left side frame
            framel=Frame(main,width=200,height=630,bg="grey93",bd=0)
            framel.place(x=5,y=70)
            #=================================================features label
            label1=Label(framel,text='Features !',font=("Century Schoolbook L",20,"bold"),
                            bg="grey93",fg="black")
            label1.place(x=35,y=100)
            #==================================button to sort contact
            button_done=Button(framel,text='Sort contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=sort,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=170)
            #==================================button to search contact
            button_done=Button(framel,text='Search contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=search,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=230)
            #==================================button to print contact
            button_done=Button(framel,text='Print contact',font=("Algeria",15,"bold"),
                        width=17,pady=5,activebackground="grey91",
                        command=prin,
                        cursor="hand2",bg="grey91",fg="black",border=0)
            button_done.place(x=0,y=290)
            #=================================================date
            lable_d=Label(framel,text=f"Date:- {wox}",
                            font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            lable_d.place(x=6,y=5)
            #=================================================time
            def update_clock():
                current_time = datetime.now().strftime("%H:%M:%S")
                clock_label.config(text=current_time)
                clock_label.after(1000, update_clock)# Update every 1 second (1000 milliseconds)

            lable_t=Label(framel,text="Time:- ",
                            font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            lable_t.place(x=4,y=40)

            clock_label = Label(framel,font=("Microsoft YeHei UI Light",18,"bold"),bg="grey93",fg="black")
            clock_label.place(x=80,y=40)

            update_clock()
            #=================================================main frame
            t=Frame(main,width=1065,height=615,bg="white",bd=0)
            t.place(x=210,y=70)
            #=================================================tree view diaplay
            def tree():
                cursor.execute("SELECT * FROM contacts WHERE label = '{}'".format(st_special1))
                data = cursor.fetchall()


                global c
                c = 0
                for record in data:
                    if c % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=c, values=record, tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=c, values=record, tags=('oddrow',))
                    c += 1

            yscroll=Scrollbar(t,orient=VERTICAL)
            yscroll.pack(side=RIGHT,fill=Y)
            xscroll=Scrollbar(t,orient=HORIZONTAL)
            xscroll.pack(side=BOTTOM,fill=X)

            columns = ("firstname", "surname", "phoneNo", "DOB", "label", "email", "sex", "address")
            my_tree = ttk.Treeview(t,height=23, show="headings",selectmode="browse",
                                    columns=columns,yscrollcommand=yscroll.set,
                                    xscrollcommand=xscroll.set)
            my_tree.pack()

            yscroll.config(command=my_tree.yview)
            xscroll.config(command=my_tree.xview)

            my_tree.column("firstname", anchor=CENTER, width=100, minwidth=110)
            my_tree.column("surname", anchor=CENTER, width=110, minwidth=150)
            my_tree.column("phoneNo", anchor=CENTER, width=145, minwidth=165)
            my_tree.column("DOB", anchor=CENTER, width=100, minwidth=150)
            my_tree.column("label", anchor=CENTER, width=150, minwidth=200)
            my_tree.column("email", anchor=CENTER, width=250, minwidth=300)
            my_tree.column("sex", anchor=CENTER, width=100, minwidth=110)
            my_tree.column("address", anchor=CENTER, width=285, minwidth=345)

            my_tree.heading("firstname", text="Firstname", anchor=CENTER)
            my_tree.heading("surname", text="Surname", anchor=CENTER)
            my_tree.heading("phoneNo", text="PhoneNo", anchor=CENTER)
            my_tree.heading("DOB", text="DOB", anchor=CENTER)
            my_tree.heading("label", text="Label", anchor=CENTER)
            my_tree.heading("email", text="Email", anchor=CENTER)
            my_tree.heading("sex", text="Sex", anchor=CENTER)
            my_tree.heading("address", text="Address", anchor=CENTER)

            # Define styles for treeview table
            style = ttk.Style()
            style.theme_use("clam")  # Choose a theme ('clam' is just an example)

            # Configure the header style
            style.configure("Treeview.Heading",
                            font=("Century Gothic", 16, "bold"),
                            foreground="black")

            # Configure the row style
            style.configure("Treeview",
                            font=("Century Gothic", 16),
                            background="white",
                            foreground="black",rowheight=25)

            style.map('Treeview', background=[('selected', 'dodger blue')])


            my_tree.tag_configure('oddrow', background='white')
            my_tree.tag_configure('evenrow', background='lightblue')

            tree()  # Call the main function to populate the treeview

            #==================================================mainloop
            main.mainloop()

        student_main()

#=====================================================STUDENT LOGIN PAGE

    def student_login_page():

#======================================================SUDENT FORGET PASSWORD

        def student_forget_password():
            def forget_update():
                den.destroy()
                def back():
                    wet.destroy()
                    student_sign_in()
                def power():
                    use=user
                    p=entry_npas.get()
                    o=entry_cpas.get()
                    if p=="New password" and o=="Confirm password":
                        lable_nc=Label(wet,text="All field's are required !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nc.place(x=165,y=395)
                        lable_nc.after(2000,lambda:lable_nc.destroy())
                    elif p=="" or p=="New password":
                        lable_n=Label(wet,text="Enter new password !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_n.place(x=165,y=395)
                        lable_n.after(2000,lambda:lable_n.destroy())
                    elif o=="" or o=="Confirm password":
                        lable_c=Label(wet,text="Enter confirm password !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_c.place(x=157,y=395)
                        lable_c.after(2000,lambda:lable_c.destroy())
                    else:
                        if p==o:
                            query="update register set password='{}' where username='{}'".format(p,use)
                            cursor.execute(query)
                            deb.commit()
                            back()
                        else:
                            lable_mo=Label(wet,text='New password and confirm password not matched !',
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_mo.place(x=60,y=395)
                            lable_mo.after(2000,lambda:lable_mo.destroy())

                #====================================new password
                def on_entrynpas(rock):
                    if entry_npas.get()=='New password':
                        entry_npas.delete(0,END)
                        entry_npas.config(show=('*'))
                def on_leavenpas(pock):
                    if entry_npas.get()=='':
                        entry_npas.config(show=(''))
                        entry_npas.insert(0,'New password')

                #==================================== new eye
                def hide1():
                    openneye.config(file="eye2.png")
                    entry_npas.config(show=('*'))
                    eyenButton.config(command=show1)

                def show1():
                    openneye.config(file="eye1.png")
                    entry_npas.config(show=(''))
                    eyenButton.config(command=hide1)
                #====================================password
                def on_entrycpas(rock):
                    if entry_cpas.get()=='Confirm password':
                        entry_cpas.delete(0,END)
                        entry_cpas.config(show=('*'))
                def on_leavecpas(pock):
                    if entry_cpas.get()=='':
                        entry_cpas.config(show=(''))
                        entry_cpas.insert(0,'Confirm password')

                #====================================eye
                def hide2():
                    openceye.config(file="eye2.png")
                    entry_cpas.config(show=('*'))
                    eyecButton.config(command=show2)

                def show2():
                    openceye.config(file="eye1.png")
                    entry_cpas.config(show=(''))
                    eyecButton.config(command=hide2)
                #====================================new password entry
                #===============================creating window
                wet=Tk()
                wet.title('FORGET PAGE')
                #wet.geometry('500x500+500+150')
                width =500
                height =500
                screen_width = wet.winfo_screenwidth()
                screen_height = wet.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                wet.geometry("%dx%d+%d+%d" % (width, height, x, y))
                wet.configure(bg='black')
                wet.resizable(0,0)
                #====================================photo import
                sop=PhotoImage(file='student.png')
                lableb=Label(wet,image=sop,bd=0,bg="black")
                lableb.place(x=177,y=20)
                #====================================requesting
                label2=Label(wet,text='Please enter your new password !',font=("Century Schoolbook L",15),
                            bg="black",fg="white")
                label2.place(x=105,y=250)
                #==================================back to sign in page
                button_back=Button(wet,text='←Back',font=("Algeria",13,"bold"),
                            width=7,pady=3,activebackground="black",
                            command=back,
                            cursor="hand2",bg="black",fg="white",border=0)
                button_back.place(x=0,y=0)
                #==================================button for save data in database
                button_done=Button(wet,text='Reset password',font=("Algeria",13,"bold"),
                            width=20,pady=5,activebackground="black",
                            command=power,
                            cursor="hand2",bg="gold2",fg="black",border=0)
                button_done.place(x=150,y=430)
                #====================================title
                label1=Label(wet,text='Student Forget password',font=("Century Schoolbook L",25,"bold"),
                            bg="black",fg="gold2")
                label1.place(x=50,y=180)
                #====================================new password entry
                entry_npas=Entry(wet,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_npas.place(x=130,y=300)
                entry_npas.insert(0,"New password")
                entry_npas.bind('<FocusIn>',on_entrynpas)
                entry_npas.bind('<FocusOut>',on_leavenpas)
                #==================================eye button
                openneye=PhotoImage(file="eye2.png")
                eyenButton=Button(wet,image=openneye,bd=0,bg='black',activebackground='black'
                                ,cursor='hand2',command=show1)
                eyenButton.place(x=380,y=300)
                #====================================confirm password entry
                entry_cpas=Entry(wet,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
                entry_cpas.place(x=130,y=350)
                entry_cpas.insert(0,"Confirm password")
                entry_cpas.bind('<FocusIn>',on_entrycpas)
                entry_cpas.bind('<FocusOut>',on_leavecpas)
                #==================================eye button
                openceye=PhotoImage(file="eye2.png")
                eyecButton=Button(wet,image=openceye,bd=0,bg='black',activebackground='black'
                                ,cursor='hand2',command=show2)
                eyecButton.place(x=380,y=350)
                #===============================mainloop
                wet.mainloop()

            def back1():
                den.destroy()
                student_sign_in()
            def search():
                global user
                name=entry_name.get().title()
                email=entry_email.get()
                user=entry_user.get()
                if name=="Name" and email=="Email" and user=="Username":
                    lable_up=Label(den,text="All field's are required !'",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=160,y=445)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif name=="" or name=="Name":
                    lable_name=Label(den,text='Enter your Name !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_name.place(x=180,y=445)   
                    lable_name.after(2000,lambda:lable_name.destroy())
                elif email=="" or email=="Email":
                    lable_email=Label(den,text='Enter your Email !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_email.place(x=180,y=445)   
                    lable_email.after(2000,lambda:lable_email.destroy())
                elif user=="" or user=="Username":
                    lable_user=Label(den,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=170,y=445)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                else:
                    query="select name,email,username from register where username='{}'".format(user)
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if name in i and user in i and email in i:
                            w=True
                        else:
                            w=False
                    if w==False:
                        lable_nok=Label(den,text='Enter correct data !'
                                        ,font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=180,y=445)
                        lable_nok.after(3000,lambda:lable_nok.destroy())
                    else:
                        forget_update()
            #====================================name
            def on_entryname(rock):
                if entry_name.get()=='Name':
                    entry_name.delete(0,END)

            def on_leavename(pock):
                if entry_name.get()=='':
                    entry_name.insert(0,'Name')
            #====================================email
            def on_entryemail(rock2):
                if entry_email.get()=='Email':
                    entry_email.delete(0,END)

            def on_leaveemail(pock2):
                if entry_email.get()=='':
                    entry_email.insert(0,'Email')
            #====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #====================================creating sign up page
            den=Tk()
            den.title('FORGET PAGE')
            #den.geometry('500x600+500+70')
            width =500
            height =600
            screen_width = den.winfo_screenwidth()
            screen_height = den.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            den.geometry("%dx%d+%d+%d" % (width, height, x, y))
            den.configure(bg='black')
            den.resizable(0,0)
            #====================================photo import
            sop=PhotoImage(file='student.png')
            lableb=Label(den,image=sop,bd=0,bg="black")
            lableb.place(x=177,y=20)
            #====================================title
            label1=Label(den,text='Student Forget password',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="gold2")
            label1.place(x=50,y=180)
            #====================================requesting
            label2=Label(den,text='Please enter data for verification !',font=("Century Schoolbook L",15),
                        bg="black",fg="white")
            label2.place(x=105,y=250)
            #====================================name entry
            entry_name=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_name.place(x=130,y=300)
            entry_name.insert(0,"Name")
            entry_name.bind('<FocusIn>',on_entryname)
            entry_name.bind('<FocusOut>',on_leavename)
            #====================================email entry
            entry_email=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_email.place(x=130,y=350)
            entry_email.insert(0,"Email")
            entry_email.bind('<FocusIn>',on_entryemail)
            entry_email.bind('<FocusOut>',on_leaveemail)
            #====================================username entry
            entry_user=Entry(den,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=400)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #====================================back to sign in
            button_create=Button(den,text='Back to sign in',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=back1,
                                bg="black",fg="gold2",border=0)
            button_create.place(x=200,y=520)
            #==================================back to sign in page
            button_back=Button(den,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back1,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for search data from database
            button_done=Button(den,text='Enter',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="gold2",fg="black",border=0)
            button_done.place(x=150,y=480)
            #====================================mainloop
            den.mainloop()

#=======================================================STUDENT SIGN UP

        def student_sign_up():
            def back():
                stu.destroy()
                student_sign_in()
            def search():
                name=entry_name.get().title()
                phone=entry_phone.get()
                email=entry_email.get()
                sex=entry_sex.get()
                user=entry_user.get()
                pas=entry_pas.get()
                date=wox
                tame=time
                tepy=entry_class.get()
                if name=="Name" and phone=="Phone number" and email=="Email" and sex=="Gender" and user=="Username" and pas=="Password" and tepy=="Class":
                    lable_up=Label(stu,text="All field's are required !'",
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=160,y=585)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif name=="Name" or name=="":
                    lable_name=Label(stu,text='Enter your Name !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_name.place(x=180,y=585)   
                    lable_name.after(2000,lambda:lable_name.destroy())
                elif phone=="Phone number" or phone=="":
                    lable_phone=Label(stu,text='Enter your Phone number !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_phone.place(x=147,y=585)   
                    lable_phone.after(2000,lambda:lable_phone.destroy())
                elif email=="Email" or email=="":
                    lable_email=Label(stu,text='Enter your Email !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_email.place(x=180,y=585)   
                    lable_email.after(2000,lambda:lable_email.destroy())
                elif sex=="Gender" or sex=="":
                    lable_sex=Label(stu,text='Enter your Gender !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_sex.place(x=180,y=585)   
                    lable_sex.after(2000,lambda:lable_sex.destroy())
                elif user=="Username" or user=="":
                    lable_user=Label(stu,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=170,y=585)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                elif pas=="Password" or pas=="":
                    lable_pas=Label(stu,text='Enter your password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_pas.place(x=170,y=585)   
                    lable_pas.after(2000,lambda:lable_pas.destroy())
                elif tepy=="Class" or tepy=="":
                    lable_tepy=Label(stu,text='Enter your class !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_tepy.place(x=180,y=585)   
                    lable_tepy.after(2000,lambda:lable_tepy.destroy())
                else:
                    query="select username from register"
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if user in i:
                            w=True
                            break
                        else:
                            w=False
                    if w==True:
                        lable_nok=Label(stu,text='Username alredy exist !',
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=160,y=585)   
                        lable_nok.after(2000,lambda:lable_nok.destroy())   
                    else:
                        if name.replace(" ", "").isalpha():
                            if sex.isalpha():
                                if "@gmail.com" in email or "@yahoo.com" in email or "@outlook.com" in email:
                                    if phone.isdigit():
                                        if len(phone) == 10:
                                            phoneno="+91"+phone
                                            query="Insert into register values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,phoneno,email,sex,user,pas,date,tame,tepy)
                                            cursor.execute(query)
                                            deb.commit()
                                            back()
                                        else:
                                            lable_na=Label(stu,text="Please enter number in 10 digit !",
                                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                            lable_na.place(x=125,y=585)
                                            lable_na.after(2000,lambda:lable_na.destroy())
                                    else:
                                        lable_no=Label(stu,text="Enter number in integer !",
                                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                        lable_no.place(x=153,y=585)
                                        lable_no.after(2000,lambda:lable_no.destroy()) 
                                else:
                                    lable_no=Label(stu,text="Enter valid in email !",
                                                font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                    lable_no.place(x=165,y=585)
                                    lable_no.after(2000,lambda:lable_no.destroy())
                            else:
                                lable_no=Label(stu,text="Enter gender in alphabet!",
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                                lable_no.place(x=153,y=585)
                                lable_no.after(2000,lambda:lable_no.destroy()) 
                        else:
                            lable_no=Label(stu,text="Enter name in alphabet !",
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_no.place(x=155,y=585)
                            lable_no.after(2000,lambda:lable_no.destroy()) 
            #====================================name
            def on_entryname(rock):
                if entry_name.get()=='Name':
                    entry_name.delete(0,END)

            def on_leavename(pock):
                if entry_name.get()=='':
                    entry_name.insert(0,'Name')
            #====================================phone
            def on_entryphone(rock1):
                if entry_phone.get()=='Phone number':
                    entry_phone.delete(0,END)

            def on_leavephone(pock1):
                if entry_phone.get()=='':
                    entry_phone.insert(0,'Phone number')
            #====================================email
            def on_entryemail(rock2):
                if entry_email.get()=='Email':
                    entry_email.delete(0,END)

            def on_leaveemail(pock2):
                if entry_email.get()=='':
                    entry_email.insert(0,'Email')
            #====================================gender
            def on_entrysex(rock3):
                if entry_sex.get()=='Gender':
                    entry_sex.delete(0,END)

            def on_leavesex(pock3):
                if entry_sex.get()=='':
                    entry_sex.insert(0,'Gender')
            #====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #====================================password
            def on_entrypas(rock):
                if entry_pas.get()=='Password':
                    entry_pas.delete(0,END)
                    entry_pas.config(show=('*'))
            def on_leavepas(pock):
                if entry_pas.get()=='':
                    entry_pas.config(show=(''))
                    entry_pas.insert(0,'Password')

            #====================================eye
            def hide():
                openeye.config(file="eye2.png")
                entry_pas.config(show=('*'))
                eyeButton.config(command=show)

            def show():
                openeye.config(file="eye1.png")
                entry_pas.config(show=(''))
                eyeButton.config(command=hide)
            #====================================class
            def on_entryclass(rock):
                if entry_class.get()=='Class':
                    entry_class.delete(0,END)
            def on_leaveclass(pock):
                if entry_class.get()=='':
                    entry_class.insert(0,'Class')
            #====================================creating sign up page
            stu=Tk()
            stu.title('SIGN IN PAGE')
            #stu.geometry('500x700+500+70')
            width =500
            height =700
            screen_width = stu.winfo_screenwidth()
            screen_height = stu.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            stu.geometry("%dx%d+%d+%d" % (width, height, x, y))
            stu.configure(bg='black')
            stu.resizable(0,0)
            #====================================photo import
            sop=PhotoImage(file='student.png')
            lableb=Label(stu,image=sop,bd=0,bg="black")
            lableb.place(x=177,y=15)
            #====================================title
            label1=Label(stu,text='Student Sign up',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="gold2")
            label1.place(x=127,y=170)
            #====================================requesting
            label2=Label(stu,text='Please enter your data to Sign up',font=("Century Schoolbook L",14),
                        bg="black",fg="white")
            label2.place(x=110,y=215)
            #====================================name entry
            entry_name=Entry(stu,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_name.place(x=130,y=250)
            entry_name.insert(0,"Name")
            entry_name.bind('<FocusIn>',on_entryname)
            entry_name.bind('<FocusOut>',on_leavename)
            #====================================phone no entry
            entry_phone=Entry(stu,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_phone.place(x=130,y=300)
            entry_phone.insert(0,"Phone number")
            entry_phone.bind('<FocusIn>',on_entryphone)
            entry_phone.bind('<FocusOut>',on_leavephone)
            label4=Label(stu,text='+91',font=("Microsoft YeHei UI Light",15,"bold"),bg="black",fg="white")
            label4.place(x=85,y=300)
            #====================================email entry
            entry_email=Entry(stu,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_email.place(x=130,y=350)
            entry_email.insert(0,"Email")
            entry_email.bind('<FocusIn>',on_entryemail)
            entry_email.bind('<FocusOut>',on_leaveemail)
            #====================================gender entry
            #====================================Combobox creation
            n = StringVar()
            entry_sex=ttk.Combobox(stu, width = 20,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = n)
            #====================================Adding combobox drop down list
            entry_sex['values'] = ('Male',
                                    'Female',
                                    'Others')
            entry_sex.current()
            entry_sex.place(x=130,y=400)
            entry_sex.insert(0,"Gender")
            entry_sex.bind('<FocusIn>',on_entrysex)
            entry_sex.bind('<FocusOut>',on_leavesex)
            #====================================username entry
            entry_user=Entry(stu,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=450)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #====================================password entry
            entry_pas=Entry(stu,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_pas.place(x=130,y=500)
            entry_pas.insert(0,"Password")
            entry_pas.bind('<FocusIn>',on_entrypas)
            entry_pas.bind('<FocusOut>',on_leavepas)
            #==================================eye button
            openeye=PhotoImage(file="eye2.png")
            eyeButton=Button(stu,image=openeye,bd=0,bg='black',activebackground='black'
                            ,cursor='hand2',command=show)
            eyeButton.place(x=380,y=500)
            #==================================class type
            #====================================Combobox creation
            var= StringVar()
            entry_class=ttk.Combobox(stu, width = 20,font=("Microsoft YeHei UI Light",15),
                                        justify='center', textvariable = var)
            #====================================Adding combobox drop down list
            entry_class['values'] = ('Student 12A',
                                    'Student 12B')
            entry_class.current()
            entry_class.place(x=130,y=550)
            entry_class.insert(0,"Class")
            entry_class.bind('<FocusIn>',on_entryclass)
            entry_class.bind('<FocusOut>',on_leaveclass)
            #==================================back to sign in page
            button_back=Button(stu,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================button for save data in database
            button_done=Button(stu,text='Sign up',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="gold2",fg="black",border=0)
            button_done.place(x=147,y=615)
            #==================================create account
            labed=Label(stu,text="I have account?",font=("Microsoft YeHei UI Light",11)
                        ,bg="black",fg="white")
            labed.place(x=170,y=660)
            button_create=Button(stu,text='Sign in',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=back,
                                bg="black",fg="gold2",border=0)
            button_create.place(x=280,y=660)
            #===================================mainloop
            stu.mainloop()

#========================================================STUDENT SIGN IN

        def student_sign_in():
            def call_sign_up():
                login.destroy()
                student_sign_up()
            def call_forget():
                login.destroy()
                student_forget_password()
            def back():
                login.destroy()
                panel()
            #=====================================checking data from table
            def search():
                user=entry_user.get()
                pas=entry_passw.get()
                tepy1="Student 12A" 
                tepy2="Student 12B"
                if user=="Username" and pas=="Password":
                    lable_up=Label(login,text='Enter your username & password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_up.place(x=120,y=510)   
                    lable_up.after(2000,lambda:lable_up.destroy())
                elif user=="Username":
                    lable_user=Label(login,text='Enter your username !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_user.place(x=165,y=510)   
                    lable_user.after(2000,lambda:lable_user.destroy())
                elif pas=="Password":
                    lable_pas=Label(login,text='Enter your password !',
                                    font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                    lable_pas.place(x=165,y=510)   
                    lable_pas.after(2000,lambda:lable_pas.destroy())
                else:
                    query= "SELECT type FROM register WHERE username = '{}'".format(user)
                    cursor.execute(query)
                    data=cursor.fetchall()
                    w=()
                    for i in data:
                        if tepy1 in i or tepy2 in i:
                            w=True
                            break
                        else:
                            w=False
                    if w==False:
                        lable_nok=Label(login,text='You are not student !',
                                        font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                        lable_nok.place(x=170,y=510)   
                        lable_nok.after(2000,lambda:lable_nok.destroy())   
                    else:
                        query="select username,password from register"
                        cursor.execute(query)
                        data=cursor.fetchall()
                        w=()
                        for i in data:
                            if user in i and pas in i:
                                w=True
                                break
                            else:
                                w=False
                        if w==True:
                            global tpcolumn1_value , tpcolumn2_value
                            na=user
                            cursor.execute("SELECT name , type FROM register WHERE username = '{}'".format(na))
                            row = cursor.fetchone()
                            tpcolumn1_value = row[0]
                            tpcolumn2_value = row[1]
                            login.destroy()
                            #============================creating welcome page
                            wel = Tk()
                            wel.title("WELCOME PAGE")
                            wel.geometry('600x305+450+230')
                            wel.configure(bg="black")
                            #=============================importing photo
                            do=PhotoImage(file='welcome.png')
                            lable=Label(wel,image=do,bd=0,bg="black")
                            lable.place(x=0,y=0)
                            #=============================destroy windlow after 2 second
                            wel.after(2000,lambda:wel.destroy())
                            wel.mainloop()
                            student_cms_page()
            #========================================================================================main page call   
                        else:
                            lable_nok=Label(login,text='Enter correct username or password !',
                                            font=("Microsoft YeHei UI Light",12,"bold"),bg="black",fg="red")
                            lable_nok.place(x=110,y=510)   
                            lable_nok.after(2000,lambda:lable_nok.destroy())
                        
            #=====================================username
            def on_entryuser(rock):
                if entry_user.get()=='Username':
                    entry_user.delete(0,END)

            def on_leaveuser(pock):
                if entry_user.get()=='':
                    entry_user.insert(0,'Username')
            #=====================================password
            def on_entrypassw(rock2):
                if entry_passw.get()=='Password':
                    entry_passw.delete(0,END)
                    entry_passw.config(show=('*'))

            def on_leavepassw(pock):
                if entry_passw.get()=='':
                    entry_passw.config(show=(''))
                    entry_passw.insert(0,'Password')
            #====================================eye
            def hide():
                openeye.config(file="eye2.png")
                entry_passw.config(show=('*'))
                eyeButton.config(command=show)

            def show():
                openeye.config(file="eye1.png")
                entry_passw.config(show=(''))
                eyeButton.config(command=hide)
            #====================================student login window
            login=Tk()
            login.title('SIGN IN PAGE')
            #login.geometry('500x700+500+70')
            width =500
            height =700
            screen_width = login.winfo_screenwidth()
            screen_height = login.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            login.geometry("%dx%d+%d+%d" % (width, height, x, y))
            login.configure(bg='black')
            login.resizable(0,0)
            #====================================photo import
            stu=PhotoImage(file='student.png')
            lableb=Label(login,image=stu,bd=0,bg="black")
            lableb.place(x=177,y=70)
            #====================================title
            label1=Label(login,text='Student Sign in',font=("Century Schoolbook L",25,"bold"),
                        bg="black",fg="gold2")
            label1.place(x=127,y=260)
            #====================================requesting
            label2=Label(login,text='Please enter your Username & Password',font=("Century Schoolbook L",15),
                        bg="black",fg="white")
            label2.place(x=70,y=325)
            #====================================username entry
            entry_user=Entry(login,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_user.place(x=130,y=380)
            entry_user.insert(0,"Username")
            entry_user.bind('<FocusIn>',on_entryuser)
            entry_user.bind('<FocusOut>',on_leaveuser)
            #===================================password entry
            entry_passw=Entry(login,width=22,font=("Microsoft YeHei UI Light",15),justify='center',bd=2)
            entry_passw.place(x=130,y=440)
            entry_passw.insert(0,"Password")
            entry_passw.bind('<FocusIn>',on_entrypassw)
            entry_passw.bind('<FocusOut>',on_leavepassw)
            #==================================eye button
            openeye=PhotoImage(file="eye2.png")
            eyeButton=Button(login,image=openeye,bd=0,bg='black',activebackground='black'
                            ,cursor='hand2',command=show)
            eyeButton.place(x=380,y=441)
            #==================================button for search data from database
            button_done=Button(login,text='Sign in',font=("Algeria",13,"bold"),
                        width=20,pady=5,activebackground="black",
                        command=search,
                        cursor="hand2",bg="gold2",fg="black",border=0)
            button_done.place(x=150,y=550)
            #==================================forget password button
            button_forget=Button(login,text="Forget password ?",font=("Algeria",11),
                                width=16,pady=3,
                                cursor="hand2",
                                activebackground="black",
                                command=call_forget,
                                bg="black",fg="gold2",
                                border=0)
            button_forget.place(x=240,y=470)
            #==================================create account
            labed=Label(login,text="Don't have an account?",font=("Microsoft YeHei UI Light",11)
                        ,bg="black",fg="white")
            labed.place(x=140,y=595)
            button_create=Button(login,text='Sign up',font=("Algeria",11),
                                cursor="hand2",activebackground="black",
                                command=call_sign_up,
                                bg="black",fg="gold2",border=0)
            button_create.place(x=300,y=595)
            #==================================back to selection page
            button_back=Button(login,text='←Back',font=("Algeria",13,"bold"),
                        width=7,pady=3,activebackground="black",
                        command=back,
                        cursor="hand2",bg="black",fg="white",border=0)
            button_back.place(x=0,y=0)
            #==================================window run
            login.mainloop()
        #======================================calling sign in page to start 
        student_sign_in()
    
#=====================================================CALLING FUNCTION TO START STUDENT LOGIN PAGE

    student_login_page()

#========================================================SELECTION PANEL

def panel():
    def exit():
        pow.destroy()
    def tall():
        pow.destroy()
        teacher()
    def call():
        pow.destroy()
        student()
    pow=Tk()
    #pow.geometry("981x537+300+150")
    width =981
    height =537
    screen_width = pow.winfo_screenwidth()
    screen_height = pow.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    pow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    pow.resizable(0,0)
    pow.title("Who's using Contact Management System?")
    pow.config(bg="black")
    #==========================================PHOTOIMAGE
    bow=PhotoImage(file='background.png')
    lableb=Label(pow,image=bow,bd=0,bg="black")
    lableb.place(x=0,y=0)

    bteacher=Button(pow,text='Teacher',font=("Arial 25 bold"),
                    width=0,pady=0,activebackground="black",command=tall,
                    cursor="hand2",bg="black",fg="white",border=0)
    bteacher.place(x=360,y=280)

    bstudent=Button(pow,text='Student',font=("Arial 25 bold"),
                    width=0,pady=0,activebackground="black",command=call,
                    cursor="hand2",bg="black",fg="white",border=0)
    bstudent.place(x=360,y=380)
    #==================================back to selection page
    button_back=Button(pow,text='<-] Exit',font=("Algeria",13,"bold"),
                width=7,pady=3,activebackground="black",
                command=exit,
                cursor="hand2",bg="black",fg="red",border=0)
    button_back.place(x=0,y=0)
    #===========================================mainloop
    pow.mainloop()

#======================================================MAIN FUNCTION CALLING TO START PROGRAMME

panel()