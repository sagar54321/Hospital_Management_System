from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from datetime import date
import webbrowser
# from pymysql import *
import psycopg2
from tkinter import messagebox
from instpatient import *
from PIL import ImageTk, Image
import webbrowser


class Welcome:
    def __init__(self):
        self.root1 = tk.ThemedTk()
        self.root1.get_themes()
        self.root1.set_theme("breeze")
        self.root1.wm_geometry("550x400+200+100")
        self.root1.title("Welcome")
        
        self.lblp = ttk.Label(self.root1,text="WELCOME",font=("consolas",25,"bold"))
        self.lblp.place(x=200,y=0,width=500,height=40)

        self.mb=  Menubutton ( self.root1, text="New", relief=RAISED )
        self.mb.grid()
        self.mb.menu =  Menu ( self.mb, tearoff = 0 ,font=("consolas",14,"bold"))
        self.mb["menu"] =  self.mb.menu
        self.mb.menu.add_command ( label="ViewPatient",command=self.viewpatient )
        self.mb.menu.add_command ( label="ViewDoctor",command=self.viewdoctor )
        self.mb.menu.add_command ( label="ViewRooms",command=self.viewroom )
        self.mb.place(x=120,y=100,width=160,height=60)
        

        self.hp=  Menubutton ( self.root1, text="Help", relief=RAISED )
        self.hp.grid()
        self.hp.menu =  Menu ( self.hp, tearoff = 0,font=("consolas",16))
        self.hp["menu"] =  self.hp.menu
        self.hp.menu.add_command ( label="About",command=self.about)
        self.hp.menu.add_command ( label="Exit",command=self.root1.destroy)
        self.hp.place(x=300,y=100,width=120,height=60)

        self.root1.mainloop()

    
    def connecttodb(self):
        self.con1 = psycopg2.connect(dbname="hospital", port=5432 , user="postgres", password="admin",host="localhost" )
        self.cur1 = self.con1.cursor()

    

    def about(self):
        self.w2 = Toplevel()
        self.w2.title("About")
        self.w2.wm_geometry("1000x600+300+70")
        self.w2.config(bg='white')

        img = ImageTk.PhotoImage(Image.open("D:\Project\images\help.jpeg"))
        self.lbl = Label(master=self.w2,image=img)
        self.lbl.place(x=30,y=40,width=400,height=400)

        self.link = Label(self.w2,text="Contact Us",font=("consolas",25),fg='blue',cursor='hand2')
        self.link.place(x=350,y=460,width=400,height=50)
        
        self.link = Label(self.w2,text="Contact Us",font=("consolas",25),cursor='hand2')
        self.link.place(x=350,y=460,width=400,height=50)
        self.link.bind("<Button-1>", lambda e: webbrowser.open('mailto:moonsagar220@gmail.com', new=1))
        

        self.w2.mainloop()

    def men(self):
        self.menubar= Menu(self.root2)
        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command (label="View Patient",command=self.viewpatient)
        self.file.add_separator()
        self.file.add_command (label="View Doctor",command=self.viewdoctor)
        self.file.add_separator()
        self.file.add_command (label="View Rooms",command=self.viewroom)
        self.menubar.add_cascade (label="File", menu=self.file)

        help=Menu(self.menubar, tearoff=0, background='white', foreground='black') 
        help.add_command (label="About", command=self.about)
        help.add_separator()
        help.add_command(label="Exit", command=self.root2.destroy) 
        self.menubar.add_cascade (label="Help", menu=help)
        self.root2.config(menu=self.menubar)
    
            
    def viewpatient(self):
        self.root2 = tk.ThemedTk()
        self.root2.get_themes()
        self.root2.set_theme("breeze")
        self.root2.wm_geometry("900x600+200+100")
        self.root2.title("Patient List")
        # self.root1.destroy()
        self.men()
    
        self.lblp = ttk.Label(self.root2,text="Patients",font=("consolas",25,"bold"))
        self.lblp.place(x=100,y=0,width=500,height=40)

        self.connecttodb()
        self.cur1.execute("Select * from patient")
        self.data = self.cur1.fetchall()

        self.main_frame = Frame(self.root2)
        self.main_frame.place(x=20,y=60,width=640,height=150)

        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.place(width=640,height=150)

        self.my_scrollbar = ttk.Scrollbar(self.main_frame ,orient=VERTICAL,command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e:self.my_canvas.configure(scrollregion=(0,0,500,500)))
        
        self.sec_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0,0), window=self.sec_frame , anchor="nw")
        
        
        #self.b=ttk.Label(self.sec_frame,font=("breeze",10),text='', relief='ridge',anchor='center')
        #self.b.grid(row=0,column=0,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='PID', relief='ridge',anchor='center')
        self.b.grid(row=0,column=1,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Name', relief='ridge',anchor='center')
        self.b.grid(row=0,column=2,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='AddmissionDate', relief='ridge',anchor='center')
        self.b.grid(row=0,column=3,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='rid', relief='ridge',anchor='center')
        self.b.grid(row=0,column=4,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='did', relief='ridge',anchor='center')
        self.b.grid(row=0,column=5,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Disease', relief='ridge',anchor='center')
        self.b.grid(row=0,column=6,ipadx=10,ipady=8,sticky="nwe")
        
        i=1
        for patient in self.data: 
            for j in range(len(patient)): 
                self.b = ttk.Label(self.sec_frame,font=("consolas",10),borderwidth=2,relief='ridge',width=10,text=patient[j],anchor='center')
                self.b.grid(row=i, column=j+1,ipadx=10,ipady=8,sticky="nwe")
                #self.b.insert(END,root2tor[j]) 
                
                #ttk.Checkbutton(self.sec_frame,command=self.checkbtn).grid(row=i, column=0,ipadx=6,ipady=6)
            i=i+1
            
        Grid.rowconfigure(self.sec_frame,i,weight=1)
        for k in range(0,len(patient)):
            Grid.columnconfigure(self.sec_frame,k,weight=1)
    
        self.btninst = ttk.Button(self.root2,text="Insert",command=Insertpatient)
        self.btninst.place(x=150,y=300,width=100,height=30)

        self.btnchk = ttk.Button(self.root2,text="CheckOut",command=self.checkout)
        self.btnchk.place(x=300,y=300,width=100,height=30)
        
        self.root1.destroy()
        

    # # def checkbtn(self):
    #     self.data = []
    #     for k in range(len(self.data)):
    #         self.selected=""
    #         if self.data[k].get()>=1:
    #             self.selected += str(k)
    #             Insertpatient()

    
    def checkout(self):
        self.root2 = tk.ThemedTk()
        self.root2.get_themes()
        self.root2.set_theme("breeze")
        self.root2.wm_geometry("390x240+500+150")
        self.root2.title("checkout") 
        
        self.lbsn = ttk.Label(self.root2,text="Search Name",font=("consolas",18,"bold"))
        self.lbsn.place(x=120,y=20,width=200,height=45)    

        self.ensn = ttk.Entry(master=self.root2,font=("consolas", 18, "bold"))
        self.ensn.place(x=100, y=70, width=200, height=40)
        self.ensn.focus_force()

        self.btnbill = ttk.Button(master=self.root2, text="Bill",command=self.validname)
        self.btnbill.place(x=150, y=120, width=90, height=30)

        
        
    def validname(self):
        self.connecttodb()
        self.name = self.ensn.get()
        #self.cur1.execute("SELECT Pid,Pname,Diseases,AddmissionDate,dname,Charge,type,cost FROM patient INNER JOIN doctor ON patient.did=doctor.did INNER JOIN rooms ON patient.rid=rooms.rid WHERE Pname=%s",(self.name,))
        self.cur1.execute("""SELECT p.Pid,p.Pname,p.Diseases,p.AddmissionDate,d.dname,d.charge,r.type,r.cost FROM patient as p
INNER JOIN doctor as d
ON p.did=d.did 
INNER JOIN rooms as r
ON p.rid=r.rid WHERE Pname=%s""",(self.name,))
        self.data1 = self.cur1.fetchall()
        print(self.data1)
        if self.data1==None:
            messagebox.showerror("Error","Invalid name")
        else:
            self.root2.destroy()
            self.billing()
   

    def viewdoctor(self):
        self.root2 = tk.ThemedTk()
        self.root2.get_themes()
        self.root2.set_theme("breeze")
        self.root2.wm_geometry("900x600+200+100")
        self.root2.title("Doctor List")

        self.men()
        
        self.lbld = ttk.Label(self.root2,text="Doctors",font=("consolas",25,"bold"))
        self.lbld.place(x=0,y=0,width=500,height=40)

        self.connecttodb()
        self.cur1.execute("Select * from doctor")
        self.data = self.cur1.fetchall()

        self.main_frame = Frame(self.root2)
        self.main_frame.place(x=20,y=60,width=700,height=150)

        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.place(width=800,height=150)

        self.my_scrollbar = ttk.Scrollbar(self.main_frame ,orient=VERTICAL,command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e:self.my_canvas.configure(scrollregion=(0,0,500,500)))
        
        self.sec_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0,0), window=self.sec_frame , anchor="nw")
        
        
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='', relief='ridge',anchor='center')
        self.b.grid(row=0,column=0,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='DID', relief='ridge',anchor='center')
        self.b.grid(row=0,column=1,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Name', relief='ridge',anchor='center')
        self.b.grid(row=0,column=2,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Speciality', relief='ridge',anchor='center')
        self.b.grid(row=0,column=3,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Joining', relief='ridge',anchor='center')
        self.b.grid(row=0,column=4,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Experience', relief='ridge',anchor='center')
        self.b.grid(row=0,column=5,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Status', relief='ridge',anchor='center')
        self.b.grid(row=0,column=6,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Charge', relief='ridge',anchor='center')
        self.b.grid(row=0,column=7,ipadx=10,ipady=8,sticky="nwe")
        
        i=1
        for doctor in self.data: 
            for j in range(len(doctor)): 
                self.b = ttk.Label(self.sec_frame,font=("consolas",10),borderwidth=2,relief='ridge',width=10,text=doctor[j],anchor='center')
                self.b.grid(row=i, column=j+1,ipadx=10,ipady=8,sticky="nwe")
                #self.b.insert(END,root2tor[j]) 
                
                #ttk.Checkbutton(self.sec_frame).grid(row=i, column=0,ipadx=5,ipady=6)
            i=i+1
            
        Grid.rowconfigure(self.sec_frame,i,weight=1)
        for k in range(0,len(doctor)):
            Grid.columnconfigure(self.sec_frame,k,weight=1)


    def viewroom(self):
        self.root2 = tk.ThemedTk()
        self.root2.get_themes()
        self.root2.set_theme("breeze")
        self.root2.wm_geometry("900x600+200+100")
        self.root2.title("Room List")

        self.men()

        self.lblr = ttk.Label(self.root2,text="Rooms",font=("consolas",25,"bold"))
        self.lblr.place(x=0,y=0,width=500,height=40)

        self.connecttodb()
        self.cur1.execute("Select * from rooms")
        self.data = self.cur1.fetchall()

        self.main_frame = Frame(self.root2)
        self.main_frame.place(x=20,y=60,width=500,height=150)

        self.my_canvas = Canvas(self.main_frame)
        self.my_canvas.place(width=500,height=150)

        self.my_scrollbar = ttk.Scrollbar(self.main_frame ,orient=VERTICAL,command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e:self.my_canvas.configure(scrollregion=(0,0,500,500)))
        
        self.sec_frame = Frame(self.my_canvas)
        self.my_canvas.create_window((0,0), window=self.sec_frame , anchor="nw")
        
        
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='', relief='ridge',anchor='center')
        self.b.grid(row=0,column=0,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='RID', relief='ridge',anchor='center')
        self.b.grid(row=0,column=1,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Type', relief='ridge',anchor='center')
        self.b.grid(row=0,column=2,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Cost', relief='ridge',anchor='center')
        self.b.grid(row=0,column=3,ipadx=10,ipady=8,sticky="nwe")
        self.b=ttk.Label(self.sec_frame,font=("consolas",10),text='Count', relief='ridge',anchor='center')
        self.b.grid(row=0,column=4,ipadx=10,ipady=8,sticky="nwe")
        
        
        i=1
        for rooms in self.data: 
            for j in range(len(rooms)): 
                self.b = ttk.Label(self.sec_frame,font=("consolas",10),borderwidth=2,relief='ridge',width=10,text=rooms[j],anchor='center')
                self.b.grid(row=i, column=j+1,ipadx=10,ipady=8,sticky="nwe")
                #self.b.insert(END,root2tor[j]) 
                
                #ttk.Checkbutton(self.sec_frame).grid(row=i, column=0,ipadx=5,ipady=6)
            i=i+1
            
        Grid.rowconfigure(self.sec_frame,i,weight=1)
        for k in range(0,len(rooms)):
            Grid.columnconfigure(self.sec_frame,k,weight=1)
    
    def billing(self):
        self.root3 = tk.ThemedTk()
        self.root3.get_themes()
        self.root3.set_theme("breeze")
        self.root3.wm_geometry("600x600+400+100")
        self.root3.title("Bill")
        

        self.d1=self.data1[0][3]
        self.d2=date.today()
        self.date=self.d2-self.d1
        print(len(self.data1))

        print(self.date.days)
        print(self.data1[0][5])
        print(self.data1[0][7])
        self.delta = (self.data1[0][5]*self.date.days) + (self.data1[0][7]*self.date.days)
        self.tcharge=str(self.delta)
        

        self.lblid = ttk.Label(master=self.root3, text="Id:" , font=("consolas", 14, "bold"))
        self.lblid.place(x=50, y=20, width=160, height=35)

        self.lbid = ttk.Label(master=self.root3,text=self.data1[0][0],font=("consolas", 14, "bold"))
        self.lbid.place(x=240, y=20, width=200, height=35)

        self.lblname = ttk.Label(master=self.root3, text="Name:", font=("consolas", 14, "bold"))
        self.lblname.place(x=50, y=70, width=160, height=35)

        self.lbname = ttk.Label(master=self.root3,text=self.data1[0][1], font=("consolas", 14,"bold"))
        self.lbname.place(x=240, y=70, width=200, height=35)

        self.lbldis = ttk.Label(master=self.root3, text="Disease:", font=("consolas", 14, "bold"))
        self.lbldis.place(x=50, y=120, width=160, height=35)

        self.lbdis = ttk.Label(master=self.root3,text=self.data1[0][2], font=("consolas", 14, "bold"))
        self.lbdis.place(x=240, y=120, width=200, height=35)

        self.lblad = ttk.Label(master=self.root3, text="Addmission Date:", font=("consolas", 14, "bold"))
        self.lblad.place(x=50, y=170, width=160, height=35)
        
        self.lbad = ttk.Label(master=self.root3, text=self.data1[0][3],font=("consolas", 14,"bold"))
        self.lbad.place(x=240, y=170, width=300, height=35)

        self.lblad = ttk.Label(master=self.root3, text="Discharge Date:", font=("consolas", 14, "bold"))
        self.lblad.place(x=50, y=220, width=160, height=35)
        
        self.lbad = ttk.Label(master=self.root3, text=self.d2,font=("consolas", 14,"bold"))
        self.lbad.place(x=240, y=220, width=300, height=35)

        self.lbldrn = ttk.Label(master=self.root3, text="Doctor name:", font=("consolas", 14, "bold"))
        self.lbldrn.place(x=50, y=270, width=160, height=35)
        
        self.lbdrn = ttk.Label(master=self.root3, text=self.data1[0][4],font=("consolas", 14,"bold"))
        self.lbdrn.place(x=240, y=270, width=300, height=35)
        
        self.lbldrc = ttk.Label(master=self.root3, text="Doctor Charge:", font=("consolas", 14, "bold"))
        self.lbldrc.place(x=50, y=320, width=160, height=35)
        
        self.lbdrc = ttk.Label(master=self.root3, text=self.data1[0][5],font=("consolas", 14,"bold"))
        self.lbdrc.place(x=240, y=320, width=300, height=35)

        self.lbldrc = ttk.Label(master=self.root3, text="Room Type:", font=("consolas", 14, "bold"))
        self.lbldrc.place(x=50, y=370, width=160, height=35)
        
        self.lbdrc = ttk.Label(master=self.root3, text=self.data1[0][6],font=("consolas", 14,"bold"))
        self.lbdrc.place(x=240, y=370, width=300, height=35)

        self.lblrc = ttk.Label(master=self.root3, text="Room Cost:", font=("consolas", 14, "bold"))
        self.lblrc.place(x=50, y=420, width=160, height=35)
        
        self.lbrc = ttk.Label(master=self.root3, text=self.data1[0][7],font=("consolas", 14,"bold"))
        self.lbrc.place(x=240, y=420, width=300, height=35)        

        self.lbltot = ttk.Label(master=self.root3, text="Total Cost:", font=("consolas", 14, "bold"))
        self.lbltot.place(x=50, y=470, width=160, height=35)
        
        self.lbtot = ttk.Label(master=self.root3, text='Rs '+self.tcharge,font=("consolas", 14,"bold"))
        self.lbtot.place(x=240, y=470, width=102, height=35) 

        self.data3=str(self.data1)
        print(self.data3)
        self.cur1.execute("INSERT INTO billing(bid, Pname, Disease, AddmissionDate, DischargeDate, Doctor Name, Doctor Charge, Room Type, Room cost, Total Bill) VALUES ("+self.data1[0][0]+",'"+self.data1[0][1]+"','"+self.data1[0][2]+"',"+self.d1+","+self.d2+",'"+self.data1[0][4]+"',"+self.data1[0][5]+",'"+self.data1[0][6]+","+self.data1[0][7]+","+self.tcharge+")")
        
        self.con1.commit()

        self.root1.mainloop()

    
if __name__ == "__main__":
    w = Welcome()
    
