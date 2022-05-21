"""""""""""""""
By: Amr IDrees
"""""""""""""""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk
#import tkMessageBox



class user_management:
    def __init__(self,root):
        self.root=root
        self.root.title("Users Management System")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Users Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),fg="black",bg="lightgray")
        title.pack(side=TOP,fill=X)# .pack()--> The Pack geometry manager packs widgets in rows or columns. We can use options like fill, expand, and side to control this geometry manager
        exit_btn=Button(self.root,text="Exit",width=5,command=self.exit_button,bg="red",fg="white",bd=5,font=("times new roman",20,"bold"))
        exit_btn.place(x=1247,y=13)


        #==================All Variables============================
        
        self.id_var=StringVar()
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.contact_var=StringVar()
        self.email_var=StringVar()
        self.question_var=StringVar()
        self.answer_var=StringVar()
        self.password_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        

        #==================Manage Frame(LEFT)=======================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0bb36a")
        Manage_Frame.place(x=20,y=100,width=450,height=590)
        
        m_title=Label(Manage_Frame,text="Manage Users",bg="#0bb36a",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        """
        The Grid geometry manager puts the widgets in a 2-dimensional table.
        The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget
        """
        #ID
        lbl_id=Label(Manage_Frame,text="ID.",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        """
        sticky − What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell.
        sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW,
        compass directions indicating the sides and corners of the cell to which widget sticks
        """
        txt_id=Entry(Manage_Frame,textvariable=self.id_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        #First Name
        lbl_fname=Label(Manage_Frame,text="First Name",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_fname.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_fname=Entry(Manage_Frame,textvariable=self.fname_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_fname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #Last Name
        lbl_lname=Label(Manage_Frame,text="Last Name",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_lname.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_lname=Entry(Manage_Frame,textvariable=self.lname_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_lname.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #Contact
        lbl_contact=Label(Manage_Frame,text="Contact",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #Email
        lbl_email=Label(Manage_Frame,text="Email",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_email.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #Question
        lbl_question=Label(Manage_Frame,text="Security Question",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_question.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        combo_quest=ttk.Combobox(Manage_Frame,textvariable=self.question_var,font=("times new roman",12,"bold"),state="readonly")
        combo_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        combo_quest.grid(row=6,column=1,padx=20,pady=10)
        combo_quest.current(0)
    

        #Answer of a question
        lbl_answer=Label(Manage_Frame,text="Answer",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_answer.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        txt_answer=Entry(Manage_Frame,textvariable=self.answer_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_answer.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #Password
        lbl_pw=Label(Manage_Frame,text="Password",bg="#0bb36a",fg="white",font=("times new roman",15,"bold"))
        lbl_pw.grid(row=8,column=0,pady=10,padx=20,sticky="w")
        
        txt_pw=Entry(Manage_Frame,textvariable=self.password_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_pw.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #==================Buttons Manage Frame=====================
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#0bb36a")
        btn_Frame.place(x=6,y=500,width=430)

        add_btn=Button(btn_Frame,text="Add",width=8,height=2,command=self.add_users,bg="#006600",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=12,pady=7)
        update_btn=Button(btn_Frame,text="Update",width=8,height=2,command=self.update_data,bg="#038f0f",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=1,padx=10,pady=7)
        delete_btn=Button(btn_Frame,text="Delete",width=8,height=2,command=self.delete_data,bg="#ff0000",fg="white",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=10,pady=7)
        clear_btn=Button(btn_Frame,text="Clear",width=8,height=2,command=self.clear,bg="white",fg="black",font=("times new roman",12,"bold")).grid(row=0,column=3,padx=10,pady=7)           
               
        
        

        #==================Details Frame(RIGHT)=====================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0bb36a")
        Detail_Frame.place(x=500,y=100,width=800,height=590)

        #Search Frame           
        lbl_search=Label(Detail_Frame,text="Search By",bg="#0bb36a",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=10,pady=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("id","f_name","l_name","contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn=Button(Detail_Frame,command=self.search_data,text="Search",width=10,pady=5,bg="white",fg="black",font=("times new roman",10,"bold"))
        search_btn.grid(row=0,column=3,padx=10,pady=10)
        
        show_all_btn=Button(Detail_Frame,command=self.fetch_data,text="Show All",width=10,pady=5,bg="white",fg="black",font=("times new roman",10,"bold"))
        show_all_btn.grid(row=0,column=4,padx=10,pady=10)



        #==================Table Frame(RIGHT)=====================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#0bb36a")
        Table_Frame.place(x=10,y=70,width=770,height=500)

        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
        """
        Scrollbar:
        This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas.
        Note that you can also create horizontal scrollbars on Entry widgets.
        """
        
        self.users_table=ttk.Treeview(Table_Frame,columns=("id","f_name","l_name","contact","email","question","answer","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        """
        Treeview:
        The ttk. Treeview widget displays a hierarchical collection of items. ...
        The order in which data values are displayed may be controlled by setting the widget option display columns .
        The tree widget can also display column headings. ...
        Each item is identified by a unique name.
        """

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.users_table.xview)
        scroll_y.config(command=self.users_table.yview)

        self.users_table.heading("id",text="ID")
        self.users_table.heading("f_name",text="First Name")
        self.users_table.heading("l_name",text="Last Name")
        self.users_table.heading("contact",text="Contact")
        self.users_table.heading("email",text="Email")
        self.users_table.heading("question",text="Security Question")
        self.users_table.heading("answer",text="Answer")
        self.users_table.heading("password",text="Password")

        #Sizes 
        self.users_table['show']='headings'
        self.users_table.column("id",width=40)
        self.users_table.column("f_name",width=100)
        self.users_table.column("l_name",width=100)
        self.users_table.column("contact",width=100)
        self.users_table.column("email",width=100)
        self.users_table.column("question",width=120)
        self.users_table.column("answer",width=100)
        self.users_table.column("password",width=100)

        self.users_table.pack(fill=BOTH,expand=1)
        self.users_table.bind("<ButtonRelease-1>",self.get_cursor)
        """
        The binding function is used to deal with the events.
        We can bind Python's Functions and methods to an event as well as we can bind these functions to any particular widget.
        Binding mouse movement with tkinter Frame
        """        
        self.fetch_data()



    def add_users(self):
        if self.id_var.get()=="" or self.fname_var.get()=="" or self.lname_var.get()=="" or self.contact_var.get()=="" or self.email_var.get()=="" or self.question_var.get()=="Select" or self.answer_var.get()=="" or self.password_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="app_users")
            cur=con.cursor()
            cur.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),self.fname_var.get(),self.lname_var.get(),self.contact_var.get(),self.email_var.get(), self.question_var.get(),self.answer_var.get(),self.password_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    # TO show the data on the table
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="app_users")
        cur=con.cursor()
        cur.execute("select * from users")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.users_table.delete(*self.users_table.get_children())
            for row in rows:
                self.users_table.insert('',END,values=row)
            con.commit()
            con.close()


    def clear(self):
        self.id_var.set("")
        self.fname_var.set("")
        self.lname_var.set("")
        self.contact_var.set("")
        self.email_var.set("")
        self.question_var.set("Select")
        self.answer_var.set("")
        self.password_var.set("")


    def get_cursor(self,event):
        cursor_row=self.users_table.focus()
        contents=self.users_table.item(cursor_row)
        row=contents['values']
        #print(row)
        self.id_var.set(row[0])
        self.fname_var.set(row[1])
        self.lname_var.set(row[2])
        self.contact_var.set(row[3])
        self.email_var.set(row[4])
        self.question_var.set(row[5])
        self.answer_var.set(row[6])
        self.password_var.set(row[7])

    def update_data(self):
        if self.id_var.get()=="" or self.fname_var.get()=="" or self.lname_var.get()=="" or self.contact_var.get()=="" or self.email_var.get()=="" or self.question_var.get()=="Select" or self.answer_var.get()=="" or self.password_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="app_users")
            cur=con.cursor()
            cur.execute("update users set f_name=%s,l_name=%s,contact=%s,email=%s,question=%s,answer=%s,password=%s where id=%s",(self.fname_var.get(),self.lname_var.get(),self.contact_var.get(),self.email_var.get(), self.question_var.get(),self.answer_var.get(),self.password_var.get(),self.id_var.get()))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been updated")


    def delete_data(self):
        if self.id_var.get()=="" or self.fname_var.get()=="" or self.lname_var.get()=="" or self.contact_var.get()=="" or self.email_var.get()=="" or self.question_var.get()=="Select" or self.answer_var.get()=="" or self.password_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            result=messagebox.askquestion("Delete a row of data","Are you sure?", icon='warning')
            if result =='yes':
                con=pymysql.connect(host="localhost",user="root",password="",database="app_users")
                cur=con.cursor()
                cur.execute("delete from users where id=%s",self.id_var.get())
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been deleted")
            else:
                pass


    def search_data(self):
        if self.search_txt.get()=="" or self.search_by.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="app_users")
            cur=con.cursor()
            
            cur.execute("select * from users where "+str(self.search_by.get())+" LIKE '%" +str(self.search_txt.get())+"%'")#!
            rows=cur.fetchall()
            if len(rows)!=0:
                self.users_table.delete(*self.users_table.get_children())
                for row in rows:
                    self.users_table.insert('',END,values=row)
                con.commit()
                con.close()
            else:
                messagebox.showerror("Error","There is no information about what you are searching for")

    def exit_button(self):
        self.root.destroy()
        import login
           
    

root=Tk()
obj=user_management(root)
root.mainloop()
