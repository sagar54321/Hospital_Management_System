from tkinter import *
from tkinter import ttk
from tkinter import font
from ttkthemes import themed_tk as tk

# from pymysql import *
import psycopg2
from tkinter import messagebox


class Insertpatient:
    
    def __init__(self):
        self.root = tk.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("breeze")
        self.root.wm_geometry("650x500")
        self.root.title("New Patient")

        self.lblid = ttk.Label(master=self.root, text="Id", font=("consolas", 18, "bold"))
        self.lblid.place(x=50, y=20, width=160, height=35)

        self.enid = ttk.Entry(master=self.root, font=("consolas", 14, "bold"))
        self.enid.place(x=220, y=20, width=200, height=35)

        self.lblname = ttk.Label(master=self.root, text="Name", font=("consolas", 18, "bold"))
        self.lblname.place(x=50, y=70, width=160, height=35)

        self.enname = ttk.Entry(master=self.root, font=("consolas", 14,"bold"))
        self.enname.place(x=220, y=70, width=200, height=35)

        self.lbldis = ttk.Label(master=self.root, text="Disease", font=("consolas", 18, "bold"))
        self.lbldis.place(x=50, y=120, width=160, height=35)

        self.endis = ttk.Entry(master=self.root, font=("consolas", 14, "bold"))
        self.endis.place(x=220, y=120, width=200, height=35)

        self.lbldrn = ttk.Label(master=self.root, text="Doctor name", font=("consolas", 18, "bold"))
        self.lbldrn.place(x=50, y=170, width=160, height=35)
        
        # self.doc = ('Dr.Jayant','Dr.Abhishek')
        # self.option_var = StringVar()
        # self.option_var.get()
        # self.create_wigets1()

        self.combo = ttk.Combobox(
                state="normal",
                values=['Dr.Jayant','Dr.Abhishek'])       
        self.combo.place(x=220, y=170,width=200,height=35)
        self.combo.set('Dr.Jayant')
       

        self.lblrty = ttk.Label(master=self.root, text="Room type", font=("consolas", 18, "bold"))
        self.lblrty.place(x=50, y=220, width=160, height=35)

        # self.room = ('General','Deluxe Non AC','Deluxe AC')
        # self.option_var1 = StringVar()
        # self.option_var1.get()
        # self.create_wigets2()
        self.combo1 = ttk.Combobox(
                state="readonly",
                values=['General','Deluxe Non AC','Deluxe AC'])       
        self.combo1.place(x=220, y=220,width=200,height=35)
        self.combo1.set('General')
        
        self.lblch = ttk.Label(master=self.root, text="Charges", font=("consolas", 18, "bold"))
        self.lblch.place(x=50, y=270, width=160, height=35)
        
        self.lblch1 = ttk.Label(master=self.root, text="Doctor: Rs2000 \nRooms:\n\tGeneral: Rs500/day\n\tDeluxe Non AC: Rs1000/day\n\tDeluxe AC: Rs1500/day",
         font=("consolas", 13))
        self.lblch1.place(x=220, y=270, width=300, height=105)

        s = ttk.Style()
        s.configure('my.TButton', font=('consolas', 12,"bold"))
        self.btnsub = ttk.Button(master=self.root, text="Submit",style='my.TButton',command=self.insert)
        self.btnsub.place(x=190, y=400, width=90, height=35)


        self.root.mainloop()
    
    def connectToDB(self):
        self.conn = psycopg2.connect(host="localhost", port=5432 , user="postgres", password="admin", dbname="hospital")
        self.cur = self.conn.cursor()


    def create_wigets1(self):
        paddings = {'padx': 5, 'pady': 5}
        option_menu = ttk.OptionMenu(
            self.root,
            self.option_var,
            self.doc[0],
            *self.doc,
            )
        option_menu.grid( sticky=N, **paddings)
        option_menu.place(x=220, y=170, width=200, height=35)
    
    
    def create_wigets2(self):
        paddings = {'padx': 5, 'pady': 5}
        option_menu = ttk.OptionMenu(
            self.root,
            self.option_var1,
            self.room[0],
            *self.room,
            )
        option_menu.grid( sticky=N, **paddings)
        option_menu.place(x=220, y=220, width=200, height=35)
        


    def insert(self):
      
        self.connectToDB()
        self.dname = (self.combo.get())
        self.cur.execute("select did from doctor where dname=%s",(self.dname,))
        self.data2 = self.cur.fetchall()
        d2 = str(self.data2[0][0])
        # self.cur.execute("INSERT INTO patient(did) SELECT did from doctor where dname=%s",d2)
        self.rtype = (self.combo1.get())
        self.cur.execute("select rid from rooms where type=%s",(self.rtype,))
        self.data3 = self.cur.fetchall()
        r3 = str(self.data3[0][0])
        # self.cur.execute("INSERT INTO patient(rid) SELECT rid from rooms where type= ",r3)
        id = self.enid.get()
        name = self.enname.get()
        Disease = self.endis.get()
        # charge = self.ench.get()
        # self.cur.execute("INSERT INTO patient(Pid,Pname, AddmissionDate ,rid,did, Diseases) VALUES ("+id+ ",'"+name+"',""CURRENT_DATE""," + r3 + "," + d2 + ",'"+Disease+"')")
        self.cur.execute("INSERT INTO patient (Pid, Pname, AddmissionDate, rid, did, Diseases) VALUES (%s, %s, CURRENT_DATE, %s, %s, %s)",(id, name, r3, d2, Disease))
        self.conn.commit()
        self.root.destroy()
        messagebox.showinfo("Success", "Record inserted successfully!")
      

if __name__=='__main__':
    i = Insertpatient()
    