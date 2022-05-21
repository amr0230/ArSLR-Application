"""""""""""""""
By: Amr IDrees
"""""""""""""""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # pip install pillow
import pymysql  #pip install pymysql (Dealing with Database)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x800+0+0")
        self.root.config(bg="#fcd900")
        
        #=====Bg Image=====
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #====Left Image====
        self.left=ImageTk.PhotoImage(file="images/reg.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)


        #====Register Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=50)

        #----------------1st Row---------------------------------------------------------------------------------------------
        f_name=Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------2nd Row---------------------------------------------------------------------------------------------
        contact=Label(frame1,text="Contact No.", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)



        #----------------3rd Row---------------------------------------------------------------------------------------------
        question=Label(frame1,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly")
        self.cmb_quest['values']=("Select","Your Mother Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
    

        answer=Label(frame1,text="Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #----------------4th Row---------------------------------------------------------------------------------------------
        pw=Label(frame1,text="Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_pw=Entry(frame1,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_pw.place(x=50,y=340,width=250)

        cpw=Label(frame1,text="Confirm Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpw=Entry(frame1,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_cpw.place(x=370,y=340,width=250)

        #Show/Hide Password
        self.var_check=IntVar()
        self.check=Checkbutton(frame1,text="Show Password",variable=self.var_check,command=self.show_pw,onvalue=1,offvalue=0,bg="white",font=("times new roman",12))
        self.check.place(x=50,y=370)

        #====Terms====
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=400)#on&offvalue!!!

        #----------------Last Row---------------------------------------------------------------------------------------------
        self.btn_img=ImageTk.PhotoImage(file="images/btn_reg.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=4,cursor="hand2",command=self.register_data).place(x=50,y=440)
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20,"bold"),bd=10,cursor="hand2",bg="#169c0c",fg="white").place(x=200,y=460,width=180)


    def show_pw(self):
        if  self.var_check.get():
            self.txt_pw['show']="" 
            self.txt_cpw['show']=""
        else:
            self.txt_pw['show']="*"
            self.txt_cpw['show']="*"



    # Function to connect two python files in the same folder  
    def login_window(self):
       self.root.destroy()
       import login


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_pw.delete(0,END)
        self.txt_cpw.delete(0,END)
        self.var_chk.set(0)



    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_pw.get() =="" or self.txt_cpw.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_pw.get()!= self.txt_cpw.get():
            messagebox.showerror("Error","Those Passwords didn't match.Try again",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)
        else:
            try:#creat connection to the database
                con =  pymysql.connect(host="localhost",user="root",password="",database="app_users")
                # create a new cursor to execute queries with!!!!!
                cur = con.cursor()
                cur.execute("select * from users where email=%s",self.txt_email.get()) # To bring all data from the table
                #Method cur.fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available
                row = cur.fetchone()
                #print (row) This helps us see if there is a similarity in the rows within the same table, there for we do the following:
                if row!=None: # if there is similarity or repetition , do  
                    messagebox.showerror("Error","User already exist,Please try with another Email",parent=self.root)
                else:
                    cur.execute("INSERT INTO users(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_pw.get()
                                 ))
                    con.commit()      #stable storage
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)#!!!!!!!!!

           

             

root = Tk()
obj = Register(root)
root.mainloop()
