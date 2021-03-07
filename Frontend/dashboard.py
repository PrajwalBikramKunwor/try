from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:
    def __init__ (self,root):
        self.root = root
        self.root.title("Softwarica 5-star Hotel Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="gray")
#--------------------------------FRAME DEPARTMENT------------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame , bd=14 , width = 1350 , height = 550, padx = 20, relief = RIDGE, bg = "white")
        TopFrame.pack(side = TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450, height=700, padx=2, relief= RIDGE, bg="gray")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820, height=700, padx=2, relief=RIDGE, bg="white")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame,bd=10, width=1350, height=150, padx=20, relief=RIDGE, bg="gray")
        BottomFrame.pack(side=BOTTOM)
        
#---------------------------------BUTTON FUNNCTION DEPARTMENT---------------------------#
        def iExit():
            iExit=tkinter.messagebox.askyesno("Softwaica Hotel", "Confirm if you want to exit*YOU  ARE ABOUT TO MISS A LIFETIME EXPERIENCE BUDDY")
            if iExit>0:
                root.destroy()
                return
        def Receipt():
            
                self.txtReceipt.insert(END, CustomerRef.get()+"\t"+Name.get()+"\t"+Address.get()+"\t"+Mobile.get()+"\t"+Gender.get()+"\t"+Roomnumber.get()+"\t"+CheckInDate.get()+"\t"+CheckOutDate.get()+"\t"+PaidTax.get()+"\t"+SubTotal.get()+"\t"+TotalCost.get()+"\n")
        
             
                    
        def Reset():
            CustomerRef.set("")
            Name.set("")
            Address.set("")
            Mobile.set("")
            IDtype.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Mealtype.set("")
            Roomtype.set("")
            Roomnumber.set("")
            RoomExtNumber.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            self.txtReceipt.delete("1.0", END)

        def search_customer():
            search =Receipt.get()
            print(search)
            
            
        def TotalCostandDate():
            InDate = CheckInDate.get()
            OutDate = CheckOutDate.get()
            InDate = datetime.strptime(InDate, "%d/%m/%Y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
            TotalDays.set(abs((OutDate - InDate).days))
            
            
            if (Mealtype.get() == "Breakfast" and Roomtype.get() == "A/C"):
                q1= float(500)
                q2= float(2000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            
            elif (Mealtype.get() == "Breakfast" and Roomtype.get() == "Deluxe"):
                q1= float(500)
                q2= float(5000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "Breakfast" and Roomtype.get() == "Suite"):
                q1= float(500)
                q2= float(8000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "Lunch" and Roomtype.get() == "A/C"):
                q1= float(800)
                q2= float(2000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            
            elif (Mealtype.get() == "Lunch" and Roomtype.get() == " Deluxe"):
                q1= float(800)
                q2= float(5000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "Lunch" and Roomtype.get() == "Suite"):
                q1= float(800)
                q2= float(8000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "Dinner" and Roomtype.get() == "A/C"):
                q1= float(1000)
                q2= float(2000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            
            elif (Mealtype.get() == "Dinner" and Roomtype.get() == "Deluxe"):
                q1= float(1000)
                q2= float(5000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "Dinner" and Roomtype.get() == "Suite"):
                q1= float(1000)
                q2= float(8000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif (Mealtype.get() == "All three" and Roomtype.get() == "A/C"):
                q1= float(1500)
                q2= float(2000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            
            elif (Mealtype.get() == "All three" and Roomtype.get() == "Deluxe"):
                q1= float(1500)
                q2= float(5000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))
            elif(Mealtype.get() == "All three" and Roomtype.get() == "Suite"):
                q1= float(1500)
                q2= float(8000)
                q3=float(TotalDays.get())
                q4= float(q1 +q2)
                q5=float(q4 * q3)
                Tax = "Rs" + str("%.2f" % ((q5) * 0.13))
                ST = "Rs" + str("%.2f"%((q5)))
                TT =  "Rs" + str("%.2f"%( q5 + ((q5) * 0.13)))
                PaidTax.set((Tax))
                SubTotal.set((ST))
                TotalCost.set((TT))

            
#---------------------------VARIABLES ----------------------#
        
        CustomerRef = StringVar() 
        Name= StringVar()
        Address = StringVar()
        Mobile= StringVar()
        IDtype = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Mealtype= StringVar()
        Roomtype= StringVar()
        Roomnumber = StringVar()
        RoomExtNumber= StringVar()
        TotalCost= StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()
        search= StringVar()
        sort= StringVar()

        
        
       #------------------------------------LEFT FRAME--------------------------#
        self.lblCustomer_Ref = Label(LeftFrame , font=("arial", 12, "bold"), text= "CustomerRef", padx=2, pady=2 ,bg="gray")
        self.lblCustomer_Ref.grid(row=0,column=0, sticky=W)
        self.txtCustomer_Ref = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= CustomerRef, width=20)
        self.txtCustomer_Ref.grid(row=0,column=1, pady=3, padx=20)
        
        self.lblName = Label(LeftFrame , font=("arial", 12, "bold"), text= "Name", padx=2,pady=2, bg="gray")
        self.lblName.grid(row=1,column=0, sticky=W)
        self.txtName = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= Name, width=20)
        self.txtName.grid(row=1,column=1, pady=3, padx=20)

        
       
        self.lblAddress= Label(LeftFrame , font=("arial", 12, "bold"), text= "Address", padx=2, pady= 2 ,bg="gray")
        self.lblAddress.grid(row=3,column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= Address, width=20)
        self.txtAddress.grid(row=3,column=1, pady=3, padx=20)


        
        self.lblMobile = Label(LeftFrame , font=("arial", 12, "bold"), text= "Mobile", padx=2,pady=2 ,bg="gray")
        self.lblMobile.grid(row=5,column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= Mobile, width=20)
        self.txtMobile.grid(row=5,column=1, pady=3, padx=20)


        self.lblIDtype= Label(LeftFrame , font=("arial", 12, "bold"), text= "IDtype", padx=2, pady= 2 ,bg="gray")
        self.lblIDtype.grid(row=9,column=0, sticky=W)
        self.cboIDtype=ttk.Combobox(LeftFrame, textvariable= IDtype, state="read only", font=("arial",12, "bold"),width=18)
        self.cboIDtype["value"]= ("", "Citizenship", "Driving Liscence", "Student IDs", "Transport Card", "Passport","Any other valid id")
        self.cboIDtype.current(0)
        self.cboIDtype.grid(row=9,column=1, pady=3, padx=20)

        self.lblGender= Label(LeftFrame , font=("arial", 12, "bold"), text= "Gender", padx=2, pady= 2 ,bg="gray")
        self.lblGender.grid(row=10,column=0, sticky=W)
        self.cboGender=ttk.Combobox(LeftFrame, textvariable= Gender, state="read only", font=("arial",12, "bold"),width=18)
        self.cboGender["value"]= ("", "Male", "Female", "Any Other")
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1, pady=3, padx=20)

        self.lblCheckInDate = Label(LeftFrame , font=("arial", 12, "bold"), text= "CheckInDate(d/m/y)", padx=2, pady= 2 ,bg="gray")
        self.lblCheckInDate.grid(row=11,column=0, sticky=W)
        self.txtCheckInDate= Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= CheckInDate, width=20)
        self.txtCheckInDate.grid(row=11,column=1, pady=3, padx=20)

        self.lblCheckOutDate= Label(LeftFrame , font=("arial", 12, "bold"), text= "CheckOutDate", padx=2, pady= 2 ,bg="gray")
        self.lblCheckOutDate.grid(row=12,column=0, sticky=W)
        self.txtCheckOutDate= Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= CheckOutDate, width=20)
        self.txtCheckOutDate.grid(row=12,column=1, pady=3, padx=20)

        self.lblMealtype= Label(LeftFrame , font=("arial", 12, "bold"), text= "Mealtype", padx=2, pady= 2 ,bg="gray")
        self.lblMealtype.grid(row=13,column=0, sticky=W)
        self.cboMealtype=ttk.Combobox(LeftFrame, textvariable= Mealtype, state="read only", font=("arial",12, "bold"),width=18)
        self.cboMealtype["value"]= ("", "Breakfast", "Lunch", "Dinner", "All three")
        self.cboMealtype.current(0)
        self.cboMealtype.grid(row=13,column=1, pady=3, padx=20)

        self.lblRoomtype= Label(LeftFrame , font=("arial", 12, "bold"), text= " Roomtype", padx=2, pady= 2 ,bg="gray")
        self.lblRoomtype.grid(row=14,column=0, sticky=W)
        self.cboRoomtype=ttk.Combobox(LeftFrame, textvariable=  Roomtype, state="read only", font=("arial",12, "bold"),width=18)
        self.cboRoomtype["value"]= ("", "A/C", "Deluxe", "Suite")
        self.cboRoomtype.current(0)
        self.cboRoomtype.grid(row=14,column=1, pady=3, padx=20)

        self.lblRoomnumber= Label(LeftFrame , font=("arial", 12, "bold"), text= "Roomnumber", padx=2, pady= 2 ,bg="gray")
        self.lblRoomnumber.grid(row=15,column=0, sticky=W)
        self.txtRoomnumber= Entry(LeftFrame , font=("arial", 12, "bold"), textvariable= Roomnumber, width=20)
        self.txtRoomnumber.grid(row=15,column=1, pady=3, padx=20)

        self.btnAdd = Button(LeftFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 13, "bold"), width=6,
                               height=1, bg="skyblue", cursor="hand2", text="Add").grid(
            row=16, column=0, padx=4)
        self.btnUpdate= Button(LeftFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 13, "bold"), width=6,
                             height=1, bg="skyblue", cursor="hand2", text="Update").grid(
            row=17, column=0, padx=4)
        self.btnDelete = Button(LeftFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 13, "bold"), width=6,
                             height=1, bg="skyblue", cursor="hand2", text="Delete").grid(
            row=18, column=0, padx=4)



#---------------------------RIGHT FRAME-----------------------------------#
        self.lblLabel = Label(RightFrame, font=("arial", 10, "bold"),pady=10, bg= "cadet Blue",text = "Customer Ref\t Name\tAddress\t Mobile\t  Gender\t  Room number\t  CheckInDate\t  CheckOutDate\tPaid tax\tSubtotal\tTotalcost")
        self.lblLabel.grid(row=0, column=0, columnspan = 17)
        self.txtReceipt = Text(RightFrame, height = 10, width=108, bd= 10, font=("arial",11,"bold"))
        self.txtReceipt.grid(row=1, column=0,columnspan=2,padx=2,pady=5)

        self.lblDays = Label(RightFrame, font=("arial",14, "bold"),text = "Number of Days", bd =7 , bg="white", fg = "black",)
        self.lblDays.grid(row=2,column=0,sticky=W)
        self.txtDays = Entry(RightFrame,font=("arial", 14,"bold"), textvariable=TotalDays,bd=7 , bg="sky blue", width=50, justify = LEFT)
        self.txtDays.grid(row=2, column=1)

        self.lblPaidTax = Label(RightFrame, font=("arial",14, "bold"),text = "PaidTax", bd =7 , bg="white", fg = "black",)
        self.lblPaidTax.grid(row=3,column=0,sticky=W)
        self.txtPaidTax = Entry(RightFrame,font=("arial", 14,"bold"), textvariable=PaidTax,bd=7 , bg="skyblue", width=50, justify = LEFT)
        self.txtPaidTax.grid(row=3, column=1)

        self.lblSubTotal = Label(RightFrame, font=("arial",14, "bold"),text = "SubTotal", bd =7 , bg="white", fg = "black",)
        self.lblSubTotal.grid(row=4,column=0,sticky=W)
        self.txtSubTotal = Entry(RightFrame,font=("arial", 14,"bold"), textvariable=SubTotal,bd=7 , bg="skyblue", width=50, justify = LEFT)
        self.txtSubTotal.grid(row=4, column=1)

        self.lblTotalCost = Label(RightFrame, font=("arial",14, "bold"),text = "TotalCost", bd =7 , bg="white", fg = "black",)
        self.lblTotalCost.grid(row=5,column=0,sticky=W)
        self.txtTotalCost= Entry(RightFrame,font=("arial", 14,"bold"), textvariable=TotalCost,bd=7 , bg="skyblue", width=50, justify = LEFT)
        self.txtTotalCost.grid(row=5, column=1)

        self.search = Label(RightFrame,padx=10,pady=1,bd=4,fg="black",font=("arial",13,"bold"),width=10,  height=1,bg="sky blue",cursor="hand2", text="Search By").grid(row=6,column=0,padx=5)
        self.cboSearch = ttk.Combobox(RightFrame, textvariable=search, state="read only", font=("arial", 12, "bold"),
                                        width=18)
        self.cboSearch["value"] = ("", "Customer ref", "Mobile")
        self.cboSearch.current(0)
        self.cboSearch.grid(row=6, column=1, pady=3, padx=15)


        self.sort = Label(RightFrame, padx=10, pady=1, bd=4, fg="black", font=("arial", 13, "bold"), width=10,
                            height=1, bg="sky blue", cursor="hand2", text="Sort By").grid(row=7, column=0, padx=5)
        self.cboSort = ttk.Combobox(RightFrame, textvariable=sort, state="read only", font=("arial", 12, "bold"),
                                      width=18)
        self.cboSort["value"] = ("", "Checkindate", "Name")
        self.cboSort.current(0)
        self.cboSort.grid(row=7, column=1, pady=3, padx=15)

        #---------------------------BUTTON DEPARTMENT-----------------------------#
        self.btnTotal= Button(BottomFrame,padx= 16, pady= 1, bd= 4, fg= "black", font=("arial",13, "bold"), width=21, height= 2, bg= "skyblue",cursor="hand2", text= "Total", command = TotalCostandDate). grid(row=0,column=4,padx=4)

        self.btnReceipt= Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial",13,"bold"),width=21, height=2,bg="skyblue",cursor="hand2", text="Receipt", command=Receipt).grid(row=0,column=5,padx=5)

        self.btnReset= Button(BottomFrame,padx= 16, pady= 1, bd= 4, fg= "black", font=("arial",13, "bold"), width=21, height= 2, bg= "skyblue",cursor="hand2", text= "Reset",command = Reset ). grid(row=0,column=6,padx=5)

        self.btnExit= Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial",13,"bold"),width=21, height=2,bg="skyblue",cursor="hand2", text="Exit", command= iExit).grid(row=0,column=7,padx=5)
        
        self.btnSearch= Button(BottomFrame, padx=16, pady=1, bd=4, fg="black", font=("arial",13,"bold"),width=21, height=2,bg="skyblue",cursor="hand2", text="Search", command= search_customer ).grid(row=0,column=8,padx=5)

        







if __name__ =='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()