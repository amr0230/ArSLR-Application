"""""""""""""""
By: Amr IDrees
"""""""""""""""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install Pillow
#from datetime import*
#import time
#from math import*
import pymysql #pip install pymysql
from tkinter import messagebox,ttk



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Arabic Alphabet Sign Language Recognition - Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black") #bg="#021e2f" ->Very dark (mostly black) blue
      
        
        #===================Background Color====================       
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=265,y=0,relwidth=1,relheight=1)      
        """
        relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget
        """
        
        Name_of_project=Label(self.root,text="Arabic Alphabet Sign Language Recognition \nBased on Machine Learning Methods",font=("Times New Roman",25,"bold"),fg="#b1b505",bg="black")
        #Name_of_project.pack(side=TOP)
        Name_of_project.place(x=370,y=0,height=100)
     
        #===================Frames==============================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=380,y=99,width=800,height=510)
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        self.logo=ImageTk.PhotoImage(file="images/ISL.png")
        logo=Label(self.root,image=self.logo).place(x=180,y=99)
        
        #Email Side    
        email=Label(login_frame,text="Email Address",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        #Password Side
        pw_email=Label(login_frame,text="Password",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pw_email=Entry(login_frame,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_pw_email.place(x=250,y=280,width=350,height=35)

        #Show/Hide Password
        self.var_chk=IntVar()
        self.chk=Checkbutton(login_frame,text="Show Password",variable=self.var_chk,onvalue=1,offvalue=0,command=self.show_pw,bg="white",fg="gray",font=("times new roman",14,"bold"))
        self.chk.place(x=610,y=285,width=150,height=30)


        #Login or Register or forget PW side (three Buttons)//// command=self.login(when click on a button do what in the function login())
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#003e9c",cursor="hand2").place(x=250,y=330,width=190,height=40)
        btn_forget=Button(login_frame,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=335)
        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#003e9c").place(x=250,y=390)


        developed_by=Label(self.root,text="Developed by: Amr Idrees\nInformation Technology Department\nAhliya University",font=("Times New Roman",13,"bold"),fg="#b1b505",bg="black")
        #developed_by.pack(side=BOTTOM)
        developed_by.place(x=865,y=610,height=100)
        ##217dd9

    def show_pw(self):
        if  self.var_chk.get():
            self.txt_pw_email['show']=""
        else:
            self.txt_pw_email['show']="*"

        
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_new_pw.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pw_email.delete(0,END)




    def forget_password(self):
        #print(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_new_pw.get())
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pw.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.fproot)
        else:
            try:
                con =  pymysql.connect(host="localhost",user="root",password="",database="app_users")
                cur = con.cursor()
                cur.execute("select * from users where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                #Method cur.fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available
                row = cur.fetchone()
                #print(row)
                if row ==None:
                    messagebox.showerror("Error","Please Select the correct Security Question / Enter Answer",parent=self.fproot)
                else:
                    cur.execute("update users set password=%s where email=%s",(self.txt_new_pw.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset, Please login with new password",parent=self.fproot)
                    self.reset()
                    self.fproot.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

                
    
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the Email Address to reset your password",parent=self.root)
        else:
            try:
                con =  pymysql.connect(host="localhost",user="root",password="",database="app_users")
                cur = con.cursor()
                cur.execute("select * from users where email=%s",self.txt_email.get())
                #Method cur.fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available
                row = cur.fetchone()
                #print(row)
                if row ==None:
                    messagebox.showerror("Error","Please enter the valid Email Address to reset your password",parent=self.root)
                else:
                    con.close()#!!!!!!
                    self.fproot=Toplevel()
                    self.fproot.title("Forget Password")
                    self.fproot.geometry("350x400+500+150")
                    self.fproot.config(bg="white")
                    self.fproot.focus_force()#focus_forse: Direct input focus to this widget even if the application does not have the focus
                    self.fproot.grab_set()# A grap directs all events to this descendant widgets in the application

                    t=Label(self.fproot,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #================================Combobox, Answer, New paswword==========================================
                    #Combobox
                    question=Label(self.fproot,text="Security Question", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
                    self.cmb_quest=ttk.Combobox(self.fproot,font=("times new roman",13),state="readonly")
                    self.cmb_quest['values']=("Select","Your Mother Name  ","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)

                    #Answer
                    answer=Label(self.fproot,text="Answer", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.fproot,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    #New Password  
                    new_pw=Label(self.fproot,text="New Password", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pw=Entry(self.fproot,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pw.place(x=50,y=290,width=250)

                    #Button to Change/Reset a password
                    btn_change_pw=Button(self.fproot,text="Reset Password",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold")).place(x=95,y=340)
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
   
          

    def register_window(self):
        self.root.destroy()
        import register
        

    def login(self):
        #print(self.txt_email.get(),self.txt_pw_email.get())

        if self.txt_email.get()=="" or self.txt_pw_email.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con =  pymysql.connect(host="localhost",user="root",password="",database="app_users")
                cur = con.cursor()
                cur.execute("select * from users where email=%s and password=%s",(self.txt_email.get(),self.txt_pw_email.get()))
                #Method cur.fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available
                row = cur.fetchone()
                #print(row)
                if row ==None:
                    messagebox.showerror("Error","Invalid Email Addrees or Password",parent=self.root)
                else:
                    #messagebox.showinfo("Success","Welcome!",parent=self.root)
                    if str(self.txt_email.get())=="amridrees84@gmail.com":
                        result=messagebox.askquestion("Going to the Application","Do you want to go to the Application?")
                        if result =='yes':
                            self.root.destroy()
                            print("Please wait a few Seconds!")
                            import Sign_Language_Recognition
                        else:
                            self.root.destroy()
                            import users_management_system
                    else:
                        self.root.destroy()
                        print("Please wait a few Seconds!")
                        import Sign_Language_Recognition
                con.close()
                

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
   
     

 
root=Tk()
obj=Login_window(root)
root.mainloop()
