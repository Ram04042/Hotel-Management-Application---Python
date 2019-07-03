from tkinter import *
from datetime import *
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import webbrowser as wb
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import zerosms
#from PIL import Image, ImageTk
#from texttable import Texttable


class login:
    def __init__(self,master):
        global u,p,password
        self.master=master
        #self.l=Frame(master,width=500,height=600)
        #self.l.propagate(0)
        #self.l.pack()
        u=StringVar()
        p=StringVar()
        heading=Label(master,text="Login Portal",font=('Times new Roman',-50,'bold')).grid(row=0,column=1,padx=20,pady=50)
        userlabel=Label(master,text="Username").grid(row=1,column=0)
        username=Entry(master,textvariable=u).grid(row=1,column=1)
        passlabel=Label(master,text="Password").grid(row=2,column=0)
        password=Entry(master,textvariable=p,show='*').grid(row=2,column=1)
        loginbutton=Button(master,text="Login",command=self.loginfn,font=('times new roman',-20),width=10,height=3).grid(row=3,column=1,padx=20,pady=50)

    def loginfn(self):
        
        if ((u.get()=='admin')&(p.get()=='admin')):
            #password.delete(0,END)
            root=Toplevel(self.master)
            h=hotelmanagement(root)
        else:
            messagebox.showerror("No access", "Incorrect username or password")
        


class hotelmanagement:
    def __init__(self,master):

        #conn=sqlite3.connect("hotelman.db")
        #c=conn.cursor()
        #c.execute("drop table custdetails")
        #c.execute("create table custdetails(name varchar[20],address varchar[30],mobno varchar[20],idproof varchar[20],idno varchar[20],starthour varchar[20],startmin varchar[20],startsec varchar[20],roomtype varchar[20],roomno varchar[20],costoffood integer,email varchar[30])")
        #conn.commit()
        
        #ronn=sqlite3.connect("room.db")
        #r=ronn.cursor()
        #r.execute("create table room(roomtype varchar[10],roomno integer)")
        #for i in range(5):
        #    str="
        #r.execute(str)
        
        
        self.master=master
        self.f=Frame(master,width=1000,height=600)
        self.f.propagate(0)
        self.f.pack()
        self.f["bg"]='#2874A6'
        heading=Label(self.f,text="Mango Hotel",bg='#2874A6',font=('Times new Roman',-50,'bold')).grid(row=1,column=2,padx=20,pady=50)
        #heading.place(x=350,y=200)
        buttonbook=Button(self.f,text="Book Room",command=self.book,font=('times new roman',-20),width=10,height=3).grid(row=6,column=1,padx=20,pady=50)
        buttonvaccate=Button(self.f,text="Vacate Room",command=self.vaccate,font=('times new roman',-20),width=10,height=3).grid(row=6,column=2,padx=20,pady=50)
        buttonorder=Button(self.f,text="Room status",command=self.roomstat,font=('times new roman',-20),width=10,height=3).grid(row=6,column=3,padx=20,pady=50)
        
        #load=Image.open('ram.png')
        #render=ImageTk.PhotoImage(load)
        #img=Label(self.f,image=render).grid(row=0,column=2)
        mainimg=PhotoImage(file="giphy.gif")
        cimg=Canvas(self.f,bg="white")
        
        #f=cimg.create_image(0,0,anchor=NW,image=mainimg)
        cimg.grid(row=0,column=2)

    def book(self):
        root2=Toplevel(self.master)
        b=bookrooms(root2)

    def vaccate(self):
        root3=Toplevel(self.master)
        v=vaccaterooms(root3)

    def roomstat(self):
        root4=Toplevel(self.master)
        r=roomstatus(root4)


class bookrooms:
    global sd,d,n
    sd=('1','2','3','4','5')
    d=('1','2','3','4','5')
    n=('1','2','3','4','5')    

    def __init__(self,master):

        self.master=master
        self.f1=Frame(master,width=1000,height=800)
        self.f1.propagate(0)

        global s1,s2,s3,s4,s5,rt,idproofv,em,namet
        s1=StringVar()
        s2=StringVar()
        s3=StringVar()
        s4=StringVar()
        s5=StringVar()
        em=StringVar()
        
        heading=Label(master,text="Book Rooms",font=('Times new Roman',-50,'bold')).grid(row=0,column=1)
        name=Label(master,text="Name").grid(row=1,column=0)
        namet=Entry(master,textvariable=s1).grid(row=1,column=1)
        address=Label(master,width=20,height=1,text="Address").grid(row=2,column=0)
        addresst=Entry(master,textvariable=s2).grid(row=2,column=1)
        mobno=Label(master,text="Mobile no").grid(row=3,column=0)
        mobnot=Entry(master,textvariable=s3).grid(row=3,column=1)

        emaillabel=Label(master,text="Email ID").grid(row=4,column=0)
        emaile=Entry(master,textvariable=em).grid(row=4,column=1)

        idproof=Label(master,text="ID Proof").grid(row=5,column=0)
        idproofv= StringVar(master)
        idproofv.set("Aadhar card")

        idprooft= OptionMenu(master, idproofv, "Pan card", "Driving Licence", "Aadhar card").grid(row=5,column=1)

        idno=Label(master,text="Id no").grid(row=6,column=0)
        idnot=Entry(master,textvariable=s4).grid(row=6,column=1)
        #options=['super deluxe','delux','normal']
        rt = StringVar(master)
        rt.set("Normal") # default value
        roomtype=Label(master,text="Room type").grid(row=7,column=0)
        w = OptionMenu(master, rt, "Super Deluxe", "Deluxe", "Normal").grid(row=7,column=1)
        roomno=Label(master,text="Room No.").grid(row=8,column=0)
        roomnot=Entry(master,textvariable=s5).grid(row=8,column=1)

        self.availrooms()
        #roomtypespin=Spinbox(self.f1,values=('super deluxe','delux','normal')).grid(row=2,column=2,padx=20,pady=50)
        #super= Radiobutton(self.f, text="Regular",value=1).grid(row=2,column=1,padx=20,pady=5)
        #print(roomtypespin.get())
        #availbutton=Button(master,text="Show available rooms",font=('times new roman',-15),command=self.availrooms).grid(row=8,column=2)
        bookfinal=Button(master,text="Book",font=('times new roman',-15),command=self.bookf).grid(row=9,column=1,pady=30)
        

    def availrooms(self):
        
        conn=sqlite3.connect("hotelman.db")
        c=conn.cursor()

        rlab=Label(self.master,text="Available Rooms:",font=('Times new Roman',-20,'bold')).grid(row=1,column=2,padx=20)

        c.execute("select * from custdetails where roomtype='Super Deluxe'")
        rows=c.fetchall()
        brsd=[]
        for row in rows:
            brsd.append(row[9])
        brsdt=tuple(brsd)
        rlab=Label(self.master,text="Super deluxe: '{}'".format(tuple(sorted(set(sd).difference(set(brsdt)))))).grid(row=2,column=2,padx=20)

        c.execute("select * from custdetails where roomtype='Deluxe'")
        rows=c.fetchall()
        brd=[]
        for row in rows:
            brd.append(row[9])
        brdt=tuple(brd)
        rlab=Label(self.master,text="Deluxe: '{}'".format(tuple(sorted(set(d).difference(set(brdt)))))).grid(row=3,column=2,padx=20)


        c.execute("select * from custdetails where roomtype='Normal'")
        rows=c.fetchall()
        brn=[]
        for row in rows:
            brn.append(row[9])
        brnt=tuple(brn)
        rlab=Label(self.master,text="Normal: '{}'".format(tuple(sorted(set(n).difference(set(brnt)))))).grid(row=4,column=2,padx=20)
        conn.close()
       
    def bookf(self):
        nam=s1.get()
        a=s2.get()
        m=s3.get()
        if not nam.isalpha():
            messagebox.showerror("Error", "Name should contain only alphabets")
        elif not m.isdigit():
            messagebox.showerror("Error", "Mobile no should contain only numbers")
        #elif(strlen(m)<10):
         #   messagebox.showerror("Error", "Mobile no contains more than 10 numbers")
        else:
            
            conn=sqlite3.connect("hotelman.db")
            c=conn.cursor()
            r=rt.get()
            rno=s5.get()
            e=0
            if(r=='Super Deluxe'):
                if rno in sd:
                    e=1
            if(r=='Deluxe'):
                if rno in d:
                    e=1
            if(r=='Normal'):
                if rno in n:
                    e=1

            
            c.execute("select * from custdetails where roomtype='%s' and roomno='%s'" %(r,rno))
            row=c.fetchone()
            if ((row is None)&(rno!="")&(e==1)):
                #s=sam.get()
                
                itype=idproofv.get()
                ino=s4.get()
                now=datetime.now()       
                dh=now.hour
                dm=now.minute
                ds=now.second
                    
                conn=sqlite3.connect("hotelman.db")
                c=conn.cursor()        
                c.execute("insert into custdetails values(?,?,?,?,?,?,?,?,?,?,?,?)",(nam,a,m,itype,ino,dh,dm,ds,r,rno,0,em.get()))
                conn.commit()
                conn.close()
                successlabel=Label(self.master,text="Room successfully booked",font=('Times new Roman',-15,'bold')).grid(row=10,column=1,padx=20,pady=50)
            #    self.namet.delete(0, 'end')
                self.availrooms()
                
            else:
                messagebox.showerror("Error", "Room not available")
                
            

class vaccaterooms:
    global listbox

    def __init__(self,master):
        #self.master=master
        global listbox
        #self.f1=Frame(master,width=1000,height=800)
        #self.f1.propagate(0)
        heading=Label(master,text="Vacate room",font=('Times new Roman',-50,'bold')).grid(row=0,column=2,padx=20,pady=50)
        listbox=Listbox(master,width=40,font=('Times new Roman',-20))
        listbox.grid(row =1,column=2,padx=30)
        conn=sqlite3.connect("hotelman.db")
        c=conn.cursor()
        c.execute("Select * from custdetails")
        rows=c.fetchall()
        #print(rows)
        for row in rows:
            string="%s   %s   %s"%(row[0],row[8],row[9])
            listbox.insert(END,string)
        #listbox.bind('<<Listboxselect>>',self.genbill)  
        conn.close()
        

        vacbutton=Button(master,text="Generate bill",command=self.genbill,font=('times new roman',-20),width=10,height=3).grid(row=2,column=2,padx=20,pady=50)
        
    def genbill(self):
        

        






        
        s=listbox.get(listbox.curselection())
        #print(s)
        listbox.delete(listbox.curselection());
        a=s.split("   ")

        now=datetime.now()
        #pdfname='{}/{}/{}'.format(now.day,now.month,now.year)
        #print(pdfname)
        
        p=canvas.Canvas("{}.pdf".format(a[0]),pagesize=landscape(letter))
        p.setFont('Helvetica',48,leading=None)
        p.drawCentredString(415,500,"Mango Hotel")
        p.setFont('Helvetica',15,leading=None)
        p.drawCentredString(415,450,"Address: Bandstand Fort, Byramji Jeejeebhoy Road, Mount Mary, Bandra West, Mumbai, Maharashtra 400050")
        p.setFont('Helvetica',35,leading=None)
        p.drawString(80,400,"Invoice")
        conn=sqlite3.connect("hotelman.db")
        c=conn.cursor()
        c.execute("select * from custdetails where roomtype='%s' and roomno='%s'" %(a[1],a[2]))
        row=c.fetchone()
        checkin="{}:{}:{}".format(row[5],row[6],row[7])
        
        now=datetime.now()
        h=now.hour
        m=now.minute
        s=now.second
        checkout="{}:{}:{}".format(h,m,s)
        timedursec=(s-int(row[7]))+(m-int(row[6]))*60+(h-int(row[5]))*60*60

        if row[8]=="Super Deluxe":
            cost=timedursec*3
        if row[8]=="Deluxe":
            cost=timedursec*2
        if row[8]=="Normal":
            cost=timedursec*3

        p.setFont('Helvetica',18,leading=None)
        p.drawString(80,360,"Customer Details")
        p.setFont('Helvetica',15,leading=None)
        p.drawString(80,340,"Name:   {}".format(row[0]))
        p.drawString(80,320,"Address:{}".format(row[1]))
        p.drawString(80,300,"Mob.no: {}".format(row[2]))
        p.drawString(80,280,"{} no:  {}".format(row[3],row[4]))
        p.drawString(60,250,"-------------------------------------------------------------------------------------------------------------------------------------------")
        p.setFont('Helvetica',15,leading=None)
        p.drawString(60,230,"Room Type          Room No.        Check-in            Check-out       Time duration           Cost of room    ")
        p.drawString(60,200,"{}                 {}              {}                  {}              {}                      {}    ".format(row[8],row[9],checkin,checkout,timedursec,cost))
        p.drawString(60,170,"                                                                                                                                   +   Cost of food")
        p.drawString(60,150,"                                                                                                                                        {}     ".format(row[10]))
        p.setFont('Helvetica',30,leading=None)
        p.drawString(60,120,"                                       Total  Cost: {}".format(cost+row[10]))
        logo="M.jpg"
        p.drawImage(logo,500,270,width=None,height=None)
        
        p.showPage()
        p.save()



        '''content="Dear Sir/Madam,\nThank you very much for staying with us at Mango Hotel, We hope we acheved our goal of making your stay memorable and Comfortable.\n\nHere is an attached copy of the invoice of your stay.\n\nOnce again we appreciate you for choosing our hotel.\nWe hope to serve you again\n\nRegards,\nRahul Sharma\nManager"

        msg=MIMEMultipart()
        msg['From']="Hotel Mango"
        msg['Subject']="Letter of Thanks"

        filename="{}.pdf".format(row[0])
        filename="M.jpg"
        attachment=open(filename,'rb')
        part=MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment;filename="+filename)
        msg.attach(part)
        text=msg.as_string()'''

        fromaddr = 'marimuthuv214@gmail.com'
        toaddr = row[11]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'Letter of thenks'
        body = "Dear Sir/Madam,\nThank you very much for staying with us at Mango Hotel, We hope we acheved our goal of making your stay memorable and Comfortable.\n\nHere is an attached copy of the invoice of your stay.\n\nOnce again we appreciate you for choosing our hotel.\nWe hope to serve you again\n\nRegards,\nRahul Sharma\nManager"
        msg.attach(MIMEText(body, 'plain'))
        filename = row[0] + '.pdf'
        attachment = open('F:/Projects/SE Miniprojects/ram osl project/'+row[0] + '.pdf', 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                            'attachment; filename= %s' % filename)
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, '24026284')
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        
        '''#server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('marimuthuv214@gmail.com','24026284')
        server.sendmail('marimuthuv214@gmail.com',row[11],content)
        server.quit()'''
        
        #client=Client("AC7eda11d6751fd264c577dcf0aed53f2c","4c604f55923fafab92a75eb32299f6fa")
        #client.api.account.messages.create(from_="8454069811",to=row[2],body="Dear Sir/Madam,\nThank you very much for staying with us at Mango Hotel,\nWe hope to serve you again\n\nRegards,\nRahul Sharma\nManager")
        zerosms.sms(phno='8454069811',passwd='N8248M',message='Thanks for visiting Hotel Mango.\nRegards,\nRahul Sharma\nManager',receivernum=row[2])

        filepath="{}.pdf".format(row[0])
        conn=sqlite3.connect("hotelman.db")
        c=conn.cursor()
        c.execute("delete from custdetails where roomtype='%s' and roomno='%s'"%(a[1],a[2]))
        conn.commit()
        
        wb.open_new(r'{}.pdf'.format(row[0]))
        

class roomstatus:
    def __init__(self,master):
        #w, h = master.winfo_screenwidth(), root.winfo_screenheight()
        #master.geometry("%dx%d+0+0" % (w, h))
        conn=sqlite3.connect("hotelman.db")
        c=conn.cursor()

        i=0
        h1=Label(master,font=('Times new Roman',25,'bold'),text="Super Deluxe").grid(row=i,column=0)
        i=i=1
        l1=Label(master,font=('Times new Roman',-20,'bold'),text="%-8s %-15s %-15s %-11s %-15s %-15s %8s"%('Room.No','Name','Address','Mob no.','Id type','Id no.','Check-in')).grid(row=i,column=0)
        c.execute("select * from custdetails where roomtype='%s'" %('Super Deluxe'))
        rows=c.fetchall()
        i=i+1
        for row in rows:
            l=Label(master,font=('Times new Roman',-20),text="%-7s %-15s %-15s %-11s %-15s %-15s %s:%s:%s"%(row[9],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])).grid(row=i,column=0)
            i=i+1
    

        h1=Label(master,font=('Times new Roman',25,'bold'),text="Deluxe").grid(row=i,column=0)
        i=i+1
        l2=Label(master,font=('Times new Roman',-20,'bold'),text="%-4s %-15s %-15s %-11s %-15s %-15s %8s"%('Room.No','Name','Address','Mob no.','Id type','Id no.','Check-in')).grid(row=i,column=0)
        c.execute("select * from custdetails where roomtype='%s'" %('Deluxe'))
        rows=c.fetchall()
        i=i+1
        for row in rows:
            l=Label(master,font=('Times new Roman',-20),text="%-7s %-15s %-15s %-11s %-15s %-15s %s:%s:%s"%(row[9],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])).grid(row=i,column=0)
            i=i+1
        

        h1=Label(master,font=('Times new Roman',25,'bold'),text="Normal").grid(row=i,column=0)
        i=i+1
        l3=Label(master,font=('Times new Roman',-20,'bold'),text="%-4s %-15s %-15s %-11s %-15s %-15s %8s"%('Room.No','Name','Address','Mob no.','Id type','Id no.','Check-in')).grid(row=i,column=0)
        c.execute("select * from custdetails where roomtype='%s'" %('Normal'))
        rows=c.fetchall()
        i=i+1
        for row in rows:
            l=Label(master,font=('Times new Roman',-20),text="%-7s %-15s %-15s %-11s %-15s %-15s %s:%s:%s"%(row[9],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])).grid(row=i,column=0)
            i=i+1

        
root=Tk()
hm=login(root)
root.mainloop()
