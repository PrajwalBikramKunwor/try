from tkinter import*
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1350x700+0+0")
        

        frame1= Frame(self.root, bg="gray")
        frame1.place(x=480, y = 100,width=700 ,height=500)
        
        title=Label(frame1,text="LOGIN TO ON_CART ONLINE WORLD",font=("new times roman",19,"italic"),bg="gray",fg="black").place(x=50,y=30)

        username= Label(frame1,text="Username:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=100)
        txt_username= Entry(frame1,font=("times new roman", 16),bg="white").place(x=50,y=130,width = 250)

        password= Label(frame1,text="Password:", font=("New times roman", 16,"bold"),fg="green",bg="gray").place (x=50,y=170)
        txt_password= Entry(frame1,font=("times new roman", 15),bg="white").place(x=50,y=200,width = 250)








root=Tk()
obj = login(root)
root= mainloop()