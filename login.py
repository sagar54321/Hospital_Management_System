from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
# from pymysql import *
import psycopg2
from tkinter import messagebox
from welcome import *
class Login:
    def __init__(self):
        self.root = tk.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("breeze")
        self.root.wm_geometry("390x240+500+150")
        self.root.title("Login")
        self.root.attributes("-toolwindow",True)

        self.lbluser=ttk.Label(master=self.root,text='UserName:',font=("consolas", 18, "bold"))
        self.lbluser.place(x=20, y=50, width=120, height=30)

        self.enuser = ttk.Entry(master=self.root,font=("consolas", 11))
        self.enuser.place(x=170, y=50, width=180, height=35)

        self.lblpass=ttk.Label(master=self.root,text='Password:',font=("consolas", 18, "bold"))
        self.lblpass.place(x=20, y=100, width=120, height=30)

        self.enpass = ttk.Entry(master=self.root,font=("consolas", 11),show='*')
        self.enpass.place(x=170, y=100, width=180, height=35)

        self.btnlgn = ttk.Button(master=self.root, text="Login", command=self.validlogin)
        self.btnlgn.place(x=90, y=150, width=90, height=30)

        self.btnsgnin = ttk.Button(master=self.root, text="SignUp", command=self.signup)
        self.btnsgnin.place(x=200, y=150, width=90, height=30)

        self.connectToDB()
        self.root.mainloop()


    def connectToDB(self):
        self.conn = psycopg2.connect(host="localhost", port=5432 , user="postgres", password="admin", dbname="hospital" )
        self.cur = self.conn.cursor()

    def login(self):
        self.connectToDB()
        self.user = self.enuser.get()
        self.passw = self.enpass.get()
        self.cur.execute("SELECT * FROM login WHERE username='"+self.user+"' and password='"+self.passw+"'")
        self.data = self.cur.fetchone()
        
    def validlogin(self):
        self.login()
        if self.data==None:
            messagebox.showerror("Error","Invalid User Name And Password")
        else:
            messagebox.showinfo("Success","Successfully Login")
            self.root.destroy()
            Welcome()

      
    def signup(self):
        self.root.destroy()
        self.win = tk.ThemedTk()
        self.root.get_themes()
        self.root.set_theme("breeze")
        self.win.wm_geometry("390x240+500+150")
        self.win.title("SignUp")

        self.lbluadd=ttk.Label(master=self.win,text='UserName:',font=("consolas", 18, "bold"))
        self.lbluadd.place(x=20, y=50, width=120, height=30)

        self.enuadd = ttk.Entry(master=self.win,font=("consolas", 18, "bold"))
        self.enuadd.place(x=170, y=50, width=180, height=30)

        self.lblpadd=ttk.Label(master=self.win,text='Password:',font=("consolas", 18, "bold"))
        self.lblpadd.place(x=20, y=100, width=120, height=30)

        self.enpadd = ttk.Entry(master=self.win,font=("consolas", 18, "bold"),show='*')
        self.enpadd.place(x=170, y=100, width=180, height=30)

        self.btnsub = ttk.Button(master=self.win, text="Submit",command=self.getinsert)
        self.btnsub.place(x=140, y=150, width=90, height=30)
        self.win.mainloop()

    def getinsert(self):
        self.connectToDB()
        self.user = self.enuadd.get()
        self.passw = self.enpadd.get()
        self.cur.execute("insert into login values('"+ self.user +"','"+ self.passw +"')")
        self.conn.commit()
        if self.enuadd.get()=='' and self.enpadd.get()=='':
            pass
        else:
            messagebox.showinfo("Info","Inserted")
            self.win.destroy()
            self.__init__()
         

if __name__ == "__main__":
    l = Login()