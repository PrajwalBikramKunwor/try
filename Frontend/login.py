from tkinter import*
from tkinter import ttk, messagebox
import pymysql
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1350x700+0+0")
        

        frame1= Frame(self.root, bg="gray")
        frame1.place(x=480, y = 100,width=500 ,height=400)
        
        title=Label(frame1,text="LOGIN TO ON_CART ONLINE WORLD",font=("new times roman",19,"italic"),bg="gray",fg="black").place(x=50,y=30)

        username= Label(frame1,text="Username:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=100)
        self.txt_username= Entry(frame1,font=("times new roman", 16),bg="white")
        self.txt_username.place(x=50,y=130,width = 350)
        password= Label(frame1,text="Password:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=170)
        self.txt_password= Entry(frame1,font=("times new roman", 15),bg="white")
        self.txt_password.place(x=50,y=200,width = 350)
        #------------Buttons department--------------#
        btn_login= Button(frame1,text="Login",font=("New times roman",15,"bold"),bg="gray",fg="black",cursor="hand2",command= self.login_data).place(x=50,y=240, width = 300)

        btn_register= Button(frame1,text="New to ON_Cart: Register here:",font=("New times roman",15,"bold"),bg="gray",fg="black",cursor="hand2").place(x=50,y=290, width = 300)

        btn_exit= Button(frame1,text="Exit",font=("New times roman",15,"bold"),bg="gray",fg="red",cursor="hand2").place(x=50,y=340, width = 300)

    def login_data(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("ERROR", "Fill up both username and password", parent= self.root)
        else:
            try:
                con= pymysql.connect(host="localhost",user="root",password="",database="ita assignment")
                cur=con.cursor()
                cur.execute("select* from registration table where username = %s and password=%s",(self.txt_username.get(),self.txt_password.get()))
                row=cur.fetchone()
                print(row)        
            except Exception as es:
                messagebox.showerror("Error",f"ERROR{str(es)}", parent= self.root)

        

root=Tk()
obj = login(root)
root= mainloop()