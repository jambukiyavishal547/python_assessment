import logging
logging.basicConfig(filename='student_management.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#class students:
d={}
op="y"
    # all method for counsellor 
    # for add student 
def add_student(snumber,fname,lname,cno):
    if snumber in d: 
         logging.warning("The entered serial nmuber is already avaliable in the database")
    else: 
        d[snumber] = {
         "fname": fname,
         "lname": lname,
         "contact": cno,
         "subjects": {},
         "faculty":faculty
        }
        logging.info("Student data entered successfully.")
#for remove student
def remove_student(snumber):
    if snumber in d:
        del d[snumber]       
        op=input("Do You Want To Delete Record?? (y/n)")
        if op=='y':                                  
         logging.info("student removed successfully")
    else:
        logging.warning("entered serial number doesnot exsist")

        #for view all student 
def view_all_student():
        logging.info(d)    
        print(d)
        #view specific student
def view_specifirc_student(snumber):
    snumber=int(input("Enter Snumber: "))
    if snumber in d:
        logging.info(d[snumber])
        print(d[snumber])
        student = d[snumber]
    else:
        logging.warning("entered serial number doesnot exsist")
    #all method for faculty
#add subject mark in dictonary
def add_subject(snumber,sub,mark,fees,sub2,mark2,fees2):
    if snumber in d:
        d[snumber]["subjects"][sub] = {"marks":mark,"fees":fees}
        d[snumber]["subjects"][sub2] = {"marks":mark2,"fees":fees2}
    else:    
        logging.warning("entered serial number doesnot exsist")
    #view all student is above in counseller
    #all method for student
    
#st=students()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

while True:
    #for all action
    print("********** press 1 for counsellor **********")
    print("********** press 2 for faculty    **********")
    print("********** press 3 for student    **********")
    print("********** press 4 for Exit       **********")

    logging.info("********** press 1 for counsellor **********")
    logging.info("********** press 2 for faculty    **********")
    logging.info("********** press 3 for student    **********")
    logging.info("********** press 4 for Exit       **********")

    rol_id=int(input("Enter Role Id: "))
    #for select one number
    if rol_id==1 and op=='y':
        #for all counsellor action
        print("1. add student")
        print("2. Remove student")
        print("3. View All student")
        print("4. View Specific Student")
        
        logging.info("1. add student")
        logging.info("2. Remove student")
        logging.info("3. View All student")
        logging.info("4. View Specific Student")
        c_choice=int(input("Enter A Choice: "))
        #if select 1 in counsellor
        if c_choice==1:
            print("Add Student Data:  ")
            snumber=int(input("Enter a Serial number: "))
            fname=str(input("Enter a First Name: "))
            lname=str(input("Enter a Last Name: "))
            cno=int(input("Enter a Contect number: "))
            sub=str(input("Enter a Subject: "))
            mark=int(input("Enter a Mark: "))
            fees=int(input("Enter a Fees:"))
            sub2=str(input("Enter a Subject: "))
            mark2=int(input("Enter a Mark: "))
            fees2=int(input("Enter a Fees:"))
            faculty=str(input("Enter your faculty: "))
            add_student(snumber,fname,lname,cno)
            add_subject(snumber,sub,mark,fees,sub2,mark2,fees2)
            
            op = input("Do you want to perform any other operation(y/n) :")

         #if select 2 for counsellor
        elif c_choice==2:
            logging.info("For Remove Student data: ")
            snumber=int(input("Enter Student Serial for remove: "))
            remove_student(snumber)
            op = input("Do you want to perform any other operation(y/n) :")
            #if select 3 for counsellor view all 
        elif c_choice==3:
            logging.info("View all student data")
            view_all_student()
            op = input("Do you want to perform any other operation(y/n) :")
        #if select 4 for counsellor view specifice
        elif c_choice==4:
            logging.info("For Specifice Student Data:    ")
            view_specifirc_student(snumber)
            op = input("Do you want to perform any other operation(y/n) :")
    
    if rol_id==2 and op=='y':
        #for faculty
        print("1. add mark to student")
        print("2. View All student")   

        logging.info("1. add mark to student")
        logging.info("2. View All student")   
          
        f_choice=int(input("Enter a choice by Faculty "))
        if f_choice==1:
            snumber=int(input("Enter Serial number: "))
            if snumber in d:
                subj = input("Enter the subject :")
                mark = int(input("Enter marks :"))
                fees = int(input("Enter fees :"))
                sub2 = input("Enter the other subject :")
                mark2 = int(input("enter marks :"))
                fees2 = int(input("Enter fees :"))
                add_subject(snumber,sub,mark,fees,sub2,mark2,fees2)
                logging.info("Student marks data entered successfully.")

            else:
                logging.warning("The entered serial does not exist")
                  
            op = input("Do you want to perform any other operation(y/n) :")

        elif f_choice == 2:
        #for faculty to view all student data
            logging.info("View all student data")
            view_all_student()
            op = input("Do you want to perform any other operation(y/n) :")
 
    if rol_id == 3 and op == "y":
        #for student
        logging.info("Enter your Serial Number to view your details")
        view_specifirc_student(snumber)
        logging.info("For any other Quries Contact faculty")
    
    if rol_id == 4:
        logging.info("Thank You For Using Our System ")
        print("Thank You For Using Our System ")
        break
