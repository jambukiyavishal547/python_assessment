
from tkinter import *
import random
import mysql.connector
import tkinter.messagebox as msg

def create_con():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_tk"
        )


x = random.randint(1000,9999)
#cbill_en.insert(0,"RS."+str(x))
#All Of Action Variable,fuction
def total():
    global bath,cream,wash,spray,lotion,rice,daal ,food_oil,wheat,sugar,maza,coke,frooti,nimko,biscuits,total_bill 
    global total_cosmetics ,total_grocery ,total_other ,cos_tax ,groc_tax ,other_tax 

    #price
    #Cosmetics
    bath=int(bath_en.get())*20
    cream=int( face_en.get())*50
    wash=int(wash_en.get())*80
    spray=int(hair_en.get())*120
    lotion=int(lotion_en.get())*100
    total_cosmetics=bath+cream+wash+spray+lotion
    cosm_en.delete(0,END)
    cosm_en.insert(0,"RS."+str(total_cosmetics))
    costex_en.delete(0,END)
    cos_tax=total_cosmetics*0.5
    costex_en.insert(0,"RS."+str(cos_tax))
    #grocery
    rice=int(rice_en.get())*70
    daal=int(daal_en.get())*120
    food_oil=int(food_en.get())*200
    wheat=int(wheat_en.get())*25
    sugar=int(suger_en.get())*45
    total_grocery=rice+daal+food_oil+wheat+sugar
    groce_en.delete(0,END)
    groce_en.insert(0,"RS."+str(total_grocery))
    grotex_en.delete(0,END)
    groc_tax=total_grocery*0.10
    grotex_en.insert(0,"RS."+str(groc_tax))
    #other
    maza=int(maza_en.get())*20
    coke=int(coke_en.get())*20
    frooti=int(frooti_en.get())*30
    nimko=int(nimkos_en.get())*40
    biscuits=int(bis_en.get())*20
    total_other=maza+coke+frooti+nimko+biscuits
    other_en.delete(0,END)
    other_en.insert(0,"RS."+str(total_other))
    othertex_en.delete(0,END)
    other_tax=total_other*0.5
    othertex_en.insert(0,"RS."+str(other_tax))
    total_bill=total_cosmetics+cos_tax+total_grocery+groc_tax+total_other+other_tax

def alert():
    msg.showwarning("","Do You Want TO Continue")

def bill():
    if cname_en.get()=="" or cphon_en.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatary")
    elif cosm_en.get()=="" and groce_en.get()=="" and other_en.get()=="":
        msg.showinfo("Insert Status","Pleace Select Prodects")
    elif cosm_en.get()=="" and groce_en.get()=="" and other_en.get()=="":
        msg.showinfo("Insert Status","No Prodect Are Selected")
    else:
        con=create_con()
        cursor=con.cursor()
        query="insert into billing(bill_no,c_name,phone_no,Total_cosmetics,	Total_grocery,Others_total,Cosmetics_tax,Grocery_tax,Others_tax) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(cbill_en.get(),cname_en.get(),cphon_en.get(),cosm_en.get(),groce_en.get(),other_en.get(),costex_en.get(),grotex_en.get(),othertex_en.get())
        cursor.execute(query,args)
        con.commit()
        con.close() 
        txt.delete(1.0,END)
        txt.insert(END,"********WELCOME CUSTOMER**********")
        txt.insert(END,"\n\nBill Number:"+ cbill_en.get())
        txt.insert(END,"\nCustomer Name:"+ cname_en.get())
        txt.insert(END,"\nPhone Number:"+ cphon_en.get())
        txt.insert(END,"\n===================================")
        txt.insert(END,"\nProduct\t\tQTY\tPrice")
        txt.insert(END,"\n===================================")

        #Cosmetics
        if bath_en.get()!="0":
            txt.insert(END,"\nBath Soap\t\t"+str(bath_en.get())+"\t"+str(bath))
        if face_en.get()!="0":
            txt.insert(END,"\nFacecream\t\t"+str(face_en.get())+"\t"+str(cream))
        if wash_en.get()!="0":
            txt.insert(END,"\nFacewash\t\t"+str(wash_en.get())+"\t"+str(wash))
        if hair_en.get()!="0":
            txt.insert(END,"\nHairspray\t\t"+str(hair_en.get())+"\t"+str(spray))
        if lotion_en.get()!="0":
            txt.insert(END,"\nBodylotion\t\t"+str(lotion_en.get())+"\t"+str(lotion))

        #grocery
        if rice_en.get()!="0":
            txt.insert(END,"\nRice\t\t"+str(rice_en.get())+"\t"+str(rice))
        if food_en.get()!="0":
            txt.insert(END,"\nFood\t\t"+str(food_en.get())+"\t"+str(food_oil))
        if daal_en.get()!="0":
            txt.insert(END,"\nDaal\t\t"+str(daal_en.get())+"\t"+str(daal))
        if wheat_en.get()!="0":
            txt.insert(END,"\nWheat\t\t"+str(wheat_en.get())+"\t"+str(wheat))
        if suger_en.get()!="0":
            txt.insert(END,"\nSugar\t\t"+str(suger_en.get())+"\t"+str(sugar))
            
        #other
        if maza_en.get()!="0":
            txt.insert(END,"\nMaza\t\t"+str(maza_en.get())+"\t"+str(maza))
        if coke_en.get()!="0":
            txt.insert(END,"\nCoke\t\t"+str(coke_en.get())+"\t"+str(coke))
        if frooti_en.get()!="0":
            txt.insert(END,"\nFrooti\t\t"+str(frooti_en.get())+"\t"+str(frooti))
        if nimkos_en.get()!="0":
            txt.insert(END,"\nNimkos\t\t"+str(nimkos_en.get())+"\t"+str(nimko))
        if bis_en.get()!="0":
            txt.insert(END,"\nBiscuits\t\t"+str(bis_en.get())+"\t"+str(biscuits))

        txt.insert(END,"\n===================================")
        if costex_en.get()!="Rs.0.0":
            txt.insert(END,"\nCosmetic Tax\t\t"+str(costex_en.get()))
        if grotex_en.get()!="Rs.0.0":
            txt.insert(END,"\nGrocery Tax\t\t"+str(grotex_en.get()))
        if othertex_en.get()!="Rs.0.0":
            txt.insert(END,"\nOthers Tax\t\t"+str(othertex_en.get()))
        txt.insert(END,"\n===================================")
        txt.insert(END,"\nTotal Bill\t\t"+"Rs."+str(total_bill))
        

def clear():
    #total clear
    cosm_en.delete(0,END)
    groce_en.delete(0,END)
    other_en.delete(0,END)
    costex_en.delete(0,END)
    grotex_en.delete(0,END)
    othertex_en.delete(0,END)

    #object clear
    #Cosmetics
    bath_en.delete(1,END)
    face_en.delete(1,END)
    wash_en.delete(1,END)
    hair_en.delete(1,END)
    lotion_en.delete(1,END)
    #grosary
    rice_en.delete(1,END)
    daal_en.delete(1,END)
    food_en.delete(1,END)
    wheat_en.delete(1,END)
    suger_en.delete(1,END)
    #other
    maza_en.delete(1,END)
    coke_en.delete(1,END)
    frooti_en.delete(1,END)
    nimkos_en.delete(1,END)
    bis_en.delete(1,END)

    cname_en.delete(0,END)
    cphon_en.delete(0,END)
    cbill_en.delete(0,END)

def exit():
    jv.destroy()

jv=Tk()
jv.geometry("1300x700+20+0")
jv.maxsize(width = 1280,height = 700)
jv.minsize(width = 1280,height = 700)
jv.title("Billing Software")

bg_color = "#074463"
fg_color = "white"
lbl_color = 'white'
#Title of App
title = Label(jv,text = "Billing Software",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

#Customer Frame
F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F1.place(x = 0,y = 80,relwidth = 1)

#Custome Name
cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
cname_en = Entry(F1,bd = 8,relief = GROOVE)
cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

#Customer Phone
cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
cphon_en = Entry(F1,bd = 8,relief = GROOVE)
cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

#Customer Bill no
cbill_lbl = Label(F1,text = "Bill No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
cbill_lbl.grid(row = 0,column = 4,padx = 20)
cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable=x)
cbill_en.grid(row = 0,column = 5,ipady = 4,ipadx = 30,pady = 5)
cbill_en.insert(0,str(x))

#Enter Button
bill_btn=Button(F1,text="Enter",bd=7, relief=GROOVE,bg=bg_color,fg=fg_color,font=("times new roman",15,"bold"), command=alert)
bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)
#cosmetics frame
F2 = LabelFrame(jv,text = "Cosmetics",font = ("time new roman",13,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F2.place(x = 5,y = 180,width = 325,height=380)

#bath soap
bath_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Bath Soap")
bath_lbl.grid(row=0,column=0,padx=10,pady=20)
bath_en=Entry(F2,bd=8,relief=GROOVE)
bath_en.grid(row=0,column=1,ipady=5,ipadx=5)
bath_en.insert(0,0)

#face crime 
face_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Face Crime")
face_lbl.grid(row=1,column=0,padx=10,pady=20)
face_en=Entry(F2,bd=8,relief=GROOVE)
face_en.grid(row=1,column=1,ipady=5,ipadx=5)
face_en.insert(0,0)

#face wash 
wash_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Face Wash")
wash_lbl.grid(row=2,column=0,padx=10,pady=20)
wash_en=Entry(F2,bd=8,relief=GROOVE)
wash_en.grid(row=2,column=1,ipady=5,ipadx=5)
wash_en.insert(0,0)

#hair spary
hair_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Hair Spary")
hair_lbl.grid(row=3,column=0,padx=10,pady=20)
hair_en=Entry(F2,bd=8,relief=GROOVE)
hair_en.grid(row=3,column=1,ipady=5,ipadx=5)
hair_en.insert(0,0)


#body lotion
lotion_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Body Lotion")
lotion_lbl.grid(row=4,column=0,padx=10,pady=20)
lotion_en=Entry(F2,bd=8,relief=GROOVE)
lotion_en.grid(row=4,column=1,ipady=5,ipadx=5)
lotion_en.insert(0,0)



#Grocery frame
F2 = LabelFrame(jv,text = "Grocery",font = ("time new roman",13,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F2.place(x = 330,y = 180,width = 325,height=380)

#content
#rice textbox
rice_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Rice")
rice_lbl.grid(row=0,column=0,padx=10,pady=20)
rice_en=Entry(F2,bd=8,relief=GROOVE)
rice_en.grid(row=0,column=1,ipady=5,ipadx=5)
rice_en.insert(0,0)

#food oil
food_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Food Oil")
food_lbl.grid(row=1,column=0,padx=10,pady=20)
food_en=Entry(F2,bd=8,relief=GROOVE)
food_en.grid(row=1,column=1,ipady=5,ipadx=5)
food_en.insert(0,0)

#daal
daal_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Daal")
daal_lbl.grid(row=2,column=0,padx=10,pady=20)
daal_en=Entry(F2,bd=8,relief=GROOVE)
daal_en.grid(row=2,column=1,ipady=5,ipadx=5)
daal_en.insert(0,0)

#wheat
wheat_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Wheat")
wheat_lbl.grid(row=3,column=0,padx=10,pady=20)
wheat_en=Entry(F2,bd=8,relief=GROOVE)
wheat_en.grid(row=3,column=1,ipady=5,ipadx=5)
wheat_en.insert(0,0)

#suger
suger_lbl=Label(F2,font=("times new roman",15,"bold"),fg=lbl_color,bg=bg_color,text="Suger")
suger_lbl.grid(row=4,column=0,padx=10,pady=20)
suger_en=Entry(F2,bd=8,relief=GROOVE)
suger_en.grid(row=4,column=1,ipady=5,ipadx=5)
suger_en.insert(0,0)


#other Frame
F2 = LabelFrame(jv,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
F2.place(x = 655,y = 180,width = 325,height = 380)

#fram content
#maza
maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maza")
maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
maza_en = Entry(F2,bd = 8,relief = GROOVE)
maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)
maza_en.insert(0,0)

#coke
coke_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "coke")
coke_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
coke_en = Entry(F2,bd = 8,relief = GROOVE)
coke_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
coke_en.insert(0,0)

#frooti
frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Frooti")
frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
frooti_en = Entry(F2,bd = 8,relief = GROOVE)
frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)
frooti_en.insert(0,0)


#nimkos
nimkos_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nimkos")
nimkos_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
nimkos_en = Entry(F2,bd = 8,relief = GROOVE)
nimkos_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)
nimkos_en.insert(0,0)

#biscuits
bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "bis")
bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
bis_en = Entry(F2,bd = 8,relief = GROOVE)
bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
bis_en.insert(0,0)

#bill Box
F3=Label(jv,bd=0,relief=GROOVE)
F3.place(x=950,y=180,width=325,height=380)

#title of text box
bill_title = Label(F3,text = "Bill Area",bd = 7,relief = GROOVE,font=("times new roman",15,"bold"))
bill_title.pack(fill = X)
    
#============
scroll_y = Scrollbar(F3,orient = VERTICAL)
txt = Text(F3,yscrollcommand = scroll_y.set)
scroll_y.pack(side = RIGHT,fill = Y)
scroll_y.config(command = txt.yview)
txt.pack(fill = BOTH,expand = 1)
#
#bill manu
F4 = LabelFrame(jv,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
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
costex_en = Entry(F4,bd = 8,relief = GROOVE)
costex_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

#tex area
#grocery Tex
grotex_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tex")
grotex_lbl.grid(row = 1,column = 2,padx = 10,pady = 0)
grotex_en = Entry(F4,bd = 8,relief = GROOVE)
grotex_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

#tex area
#other tex
othertex_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Othes Tex")
othertex_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
othertex_en = Entry(F4,bd = 8,relief = GROOVE)
othertex_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)


#total Button
total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command=total)
total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

#genrete Button
genret_bill_btn = Button(F4,text = "Genrete Bill",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command=bill)
genret_bill_btn.grid(row = 1,column = 5,ipadx = 20,padx = 30)

#Clear Button
clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command=clear)
clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

#Exit Button
exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("times new roman",12,"bold"),bd = 7,relief = GROOVE,command=exit)
exit_btn.grid(row = 1,column = 7,ipadx = 20,padx = 30)

jv.mainloop()
