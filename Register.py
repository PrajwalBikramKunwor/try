from tkinter import*
class Register:
    def __init__ (self,root):
        self.root=root
        self.root.title("REGISTRATION WINDOW")
        self.root.geometry("1350x700+0+0")
       
        frame1=Frame(self.root,bg="gray")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title= Label(frame1,text="------------------REGISTER TO ON_CART:-------------------", font=("New times roman", 20,"italic"),fg="black",bg="gray").place (x=50,y=30)


        f_name= Label(frame1,text="First name:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=100)
        txt_fname= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=50,y=130,width = 250)

        l_name= Label(frame1,text="Last name:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=100)
        txt_lname= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=370,y=130,width = 250)

        Address= Label(frame1,text="Address:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=170)
        txt_address= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=50,y=200,width = 250)

        Age= Label(frame1,text="Age:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=170)
        txt_Age= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=370,y=200,width = 250)

        username= Label(frame1,text="Username:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=50,y=240)
        txt_username= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=50,y=270,width = 250)

        password= Label(frame1,text="Password:", font=("New times roman", 15,"bold"),fg="black",bg="gray").place (x=370,y=240)
        txt_password= Entry(frame1,font=("times new roman", 15),bg="dark gray").place(x=370,y=270,width = 250)
root=Tk()
obj = Register(root)
root.mainloop()