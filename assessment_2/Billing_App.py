
from tkinter import *
import random,math,os,sys
import mysql.connector
import tkinter.messagebox as msg
import datetime
import time

def create_con():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )

class bill:
    def __init__(self,jv):
        self.jv = jv
        self.jv.geometry("1300x700+20+0")
        self.jv.maxsize(width = 1280,height = 700)
        self.jv.minsize(width = 1280,height = 700)
        self.jv.title("Billing Software")
        

        #All Of Action Variable
        self.c_name=StringVar()
        self.c_phone=StringVar()

        #bll_no
       # bill_no=random.randint(1000,9999)
        #self.c_billno=IntVar()
        #self.c_billno.set(IntVar(bill_no))

        #cosmetics
        self.bath=IntVar()
        self.cream=IntVar()
        self.wash=IntVar()
        self.spray=IntVar()
        self.lotion=IntVar()

        #grocery
        self.rice=IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()

        #other
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.nimko = IntVar()
        self.biscuits = IntVar()

        #bill menu
        self.total_cosmetics = str()
        self.total_grocery = str()
        self.total_other = str()
        self.cos_tax = str()
        self.groc_tax = str()
        self.other_tax = str()

        #all of fuctions



        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.jv,text = "Billing Software",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #Customer Frame
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #Custome Name
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #Customer Phone
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable=self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #Customer Bill no
        cbill_lbl = Label(F1,text = "Bill No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE)
        cbill_en.grid(row = 0,column = 5,ipady = 4,ipadx = 30,pady = 5)

        #Enter Button
        bill_btn=Button(F1,text="Enter",bd=7, relief=GROOVE,bg=bg_color,fg=fg_color,font=("times new roman",15,"bold"))
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)
        #cosmetics frame
        F2 = LabelFrame(self.jv,text = "Cosmetics",font = ("time new roman",13,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F2.place(x = 5,y = 180,width = 325,height=380)

        #bath soap
        bath_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Bath Soap")
        bath_lbl.grid(row=0,column=0,padx=10,pady=20)
        bath_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.bath)
        bath_en.grid(row=0,column=1,ipady=5,ipadx=5)

        #face crime 
        face_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Face Crime")
        face_lbl.grid(row=1,column=0,padx=10,pady=20)
        face_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.cream)
        face_en.grid(row=1,column=1,ipady=5,ipadx=5)

        #face wash 
        wash_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Face Wash")
        wash_lbl.grid(row=2,column=0,padx=10,pady=20)
        wash_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.wash)
        wash_en.grid(row=2,column=1,ipady=5,ipadx=5)

        #hair spary
        hair_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Hair Spary")
        hair_lbl.grid(row=3,column=0,padx=10,pady=20)
        hair_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.spray)
        hair_en.grid(row=3,column=1,ipady=5,ipadx=5)


        #body lotion
        lotion_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Body Lotion")
        lotion_lbl.grid(row=4,column=0,padx=10,pady=20)
        lotion_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.lotion)
        lotion_en.grid(row=4,column=1,ipady=5,ipadx=5)



        #Grocery frame
        F2 = LabelFrame(self.jv,text = "Grocery",font = ("time new roman",13,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F2.place(x = 330,y = 180,width = 325,height=380)

        #content
        #rice textbox
        rice_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Rice")
        rice_lbl.grid(row=0,column=0,padx=10,pady=20)
        rice_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.rice)
        rice_en.grid(row=0,column=1,ipady=5,ipadx=5)

        #food oil
        food_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Food Oil")
        food_lbl.grid(row=1,column=0,padx=10,pady=20)
        food_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.food_oil)
        food_en.grid(row=1,column=1,ipady=5,ipadx=5)

        #daal
        daal_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Daal")
        daal_lbl.grid(row=2,column=0,padx=10,pady=20)
        daal_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.daal)
        daal_en.grid(row=2,column=1,ipady=5,ipadx=5)

        #wheat
        wheat_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Wheat")
        wheat_lbl.grid(row=3,column=0,padx=10,pady=20)
        wheat_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.wheat)
        wheat_en.grid(row=3,column=1,ipady=5,ipadx=5)

        #suger
        suger_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Suger")
        suger_lbl.grid(row=4,column=0,padx=10,pady=20)
        suger_en=Entry(F2,bd=8,relief=GROOVE,textvariable=self.sugar)
        suger_en.grid(row=4,column=1,ipady=5,ipadx=5)


        #other Frame
        F2 = LabelFrame(self.jv,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #fram content
        #maza
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable=self.maza)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #coke
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "coke")
        coke_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,bd = 8,relief = GROOVE,textvariable=self.coke)
        coke_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #frooti
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
        coke_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,bd = 8,relief = GROOVE,textvariable=self.frooti)
        coke_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #nimkos
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nimkos")
        coke_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,bd = 8,relief = GROOVE,textvariable=self.nimko)
        coke_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #biscuits
        coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        coke_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        coke_en = Entry(F2,bd = 8,relief = GROOVE,textvariable=self.biscuits)
        coke_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #bill Box
        F3=Label(self.jv,bd=10,relief=GROOVE)
        F3.place(x=950,y=180,width=325,height=380)

        #title of text box
        bill_title = Label(F3,text = "Bill Area",bd = 7,relief = GROOVE,font=("times new roman",15,"bold"))
        bill_title.pack(fill = X)
    
        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)
        #
        #bill manu
        F4 = LabelFrame(self.jv,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #Total Cosmetics
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #total grocery
        groce_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        groce_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        groce_en = Entry(F4,bd = 8,relief = GROOVE)
        groce_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5) 

        #other total
        other_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = " Other Total")
        other_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        other_en = Entry(F4,bd = 8,relief = GROOVE)
        other_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5) 

        #tex area
        #cosmetics Tex
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tex")
        cosmt_lbl.grid(row = 0,column = 2,padx = 10,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #tex area
        #grocery Tex
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tex")
        cosmt_lbl.grid(row = 1,column = 2,padx = 10,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE)
        cosmt_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #tex area
        #other tex
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Othes Tex")
        cosmt_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE)
        cosmt_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)


        #total Button
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #genrete Button
        genret_bill_btn = Button(F4,text = "Genrete Bill",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE)
        genret_bill_btn.grid(row = 1,column = 5,ipadx = 20,padx = 30)

        #Clear Button
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #Exit Button
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE)
        exit_btn.grid(row = 1,column = 7,ipadx = 20,padx = 30)

        
        

jv=Tk()
obj=bill(jv)
jv.configure()
jv.mainloop()
