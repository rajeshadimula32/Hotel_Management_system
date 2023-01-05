from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import random


class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer page")
        self.root.geometry("1290x550+235+230")

        
        # title
        title_label=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title_label.place(x=0,y=0,width=1290,height=50)


        img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\logo_hotel.jpg")
        img2=img2.resize((102,52),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label_img2=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        label_img2.place(x=0,y=0,width=102,height=52)


        #label frame
        label_frame_left=LabelFrame(self.root,bd=1,relief=RIDGE,text="Customer Details",padx=4,font=("times new roman",12,"bold"))
        label_frame_left.place(x=5,y=50,width=420,height=490)

        self.var_ref=StringVar()
        global x
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))



        # labels and entries
        cust_ref_label=Label(label_frame_left,text="Customer Ref",font=("times new roman",12,"bold"),padx=4,pady=6)
        cust_ref_label.grid(row=0,column=0,sticky=W)
        cust_ref_box=ttk.Entry(label_frame_left,textvariable=self.var_ref,state="readonly", width=29,font=("times new roman",12,"bold"))
        cust_ref_box.grid(row=0,column=1)


        cname_label=Label(label_frame_left,text="Customer Name",font=("times new roman",12,"bold"),padx=4,pady=6)
        cname_label.grid(row=1,column=0,sticky=W)
        self.cname_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.cname_box.grid(row=1,column=1)

        mname_label=Label(label_frame_left,text="Father Name",font=("times new roman",12,"bold"),padx=4,pady=6)
        mname_label.grid(row=2,column=0,sticky=W)
        self.mname_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold")) 
        self.mname_box.grid(row=2,column=1)

        self.var_gender=StringVar()

        gender_label=Label(label_frame_left,text="Gender",font=("times new roman",12,"bold"),padx=4,pady=6)
        gender_label.grid(row=3,column=0,sticky=W)
        self.combo_gender=ttk.Combobox(label_frame_left,textvariable=self.var_gender, state="readonly" ,font=("times new roman",12,"bold"),width=27)
        self.combo_gender['values']=("select","Male","Female","Other")
        self.combo_gender.grid(row=3,column=1)
        self.combo_gender.current(0)


        postcode_label=Label(label_frame_left,text="Postcode",font=("times new roman",12,"bold"),padx=4,pady=6)
        postcode_label.grid(row=4,column=0,sticky=W)
        self.postcode_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.postcode_box.grid(row=4,column=1)

        mobile_label=Label(label_frame_left,text="Mobile",font=("times new roman",12,"bold"),padx=4,pady=6)
        mobile_label.grid(row=5,column=0,sticky=W)
        self.mobile_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.mobile_box.grid(row=5,column=1)

        email_label=Label(label_frame_left,text="Email",font=("times new roman",12,"bold"),padx=4,pady=6)
        email_label.grid(row=6,column=0,sticky=W)
        self.email_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.email_box.grid(row=6,column=1)

        self.var_nationality=StringVar()
        nationality_label=Label(label_frame_left,text="Nationality",font=("times new roman",12,"bold"),padx=4,pady=6)
        nationality_label.grid(row=7,column=0,sticky=W)
        self.combo_nationality=ttk.Combobox(label_frame_left,textvariable=self.var_nationality, state="readonly" ,font=("times new roman",12,"bold"),width=27)
        self.combo_nationality['values']=("select","Indian","American","French")
        self.combo_nationality.grid(row=7,column=1)
        self.combo_nationality.current(0)

        self.var_idproof=StringVar()
        idproof_label=Label(label_frame_left,text="Id proof type",font=("times new roman",12,"bold"),padx=4,pady=6)
        idproof_label.grid(row=8,column=0,sticky=W)
        self.combo_idproof=ttk.Combobox(label_frame_left,textvariable=self.var_idproof, state="readonly" ,font=("times new roman",12,"bold"),width=27)
        self.combo_idproof['values']=("select","Aadhar Card","Driving Licesence","Pan Card")
        self.combo_idproof.grid(row=8,column=1)
        self.combo_idproof.current(0)

        idnumber_label=Label(label_frame_left,text="Id number",font=("times new roman",12,"bold"),padx=4,pady=6)
        idnumber_label.grid(row=9,column=0,sticky=W)
        self.idnumber_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.idnumber_box.grid(row=9,column=1)

        address_label=Label(label_frame_left,text="Address",font=("times new roman",12,"bold"),padx=4,pady=6)
        address_label.grid(row=10,column=0,sticky=W)
        self.address_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.address_box.grid(row=10,column=1)


        #buttons
        bn_frame=Frame(label_frame_left)
        bn_frame.place(x=0,y=400,width=412,height=40)

        add_bn=Button(bn_frame,text="Add",command=self.add_data, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        add_bn.grid(row=0,column=0,padx=1)

        update_bn=Button(bn_frame,text="Update",command=self.update_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        update_bn.grid(row=0,column=1,padx=1)

        delete_bn=Button(bn_frame,text="Delete",command=self.delete_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        delete_bn.grid(row=0,column=2,padx=1)

        reset_bn=Button(bn_frame,text="Reset",command=self.reset_data, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        reset_bn.grid(row=0,column=3,padx=1)

        #table frame
        table_frame=LabelFrame(self.root,bd=1,relief=RIDGE,text="View Details and Search System",padx=4,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=850,height=490)

        search_label=Label(table_frame,text="Search by",font=("times new roman",13,"bold"),bg="brown",fg="white")
        search_label.grid(row=0,column=0,sticky=W,padx=2,pady=2)

        self.combo_search=ttk.Combobox(table_frame,state="readonly" ,font=("times new roman",13,"bold"),width=20)
        self.combo_search['values']=("select","Mobile","Name","Ref Number")
        self.combo_search.grid(row=0,column=1,padx=2,pady=2)
        self.combo_search.current(0)

        self.search_box=ttk.Entry(table_frame,width=22,font=("times new roman",13,"bold"))
        self.search_box.grid(row=0,column=2,padx=2,pady=2)

        search_bn=Button(table_frame,text="Search",command=self.search_record, font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        search_bn.grid(row=0,column=3,padx=2,pady=2)

        show_bn=Button(table_frame,text="Show All",command=self.show_all, font=("times new roman",13,"bold"),bg="black",fg="gold",width=9)
        show_bn.grid(row=0,column=4,padx=2,pady=2)


        #Add some style
        style=ttk.Style()

        #chage selected color
        style.map('Treeview',background=[('selected',"#447711")])
        # tree view
        tree_frame=Frame(table_frame,bd=2,relief=RIDGE)
        tree_frame.place(x=0,y=50,width=850,height=350)

        

        scroll_x=ttk.Scrollbar(tree_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tree_frame,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(tree_frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        #define our columns
        self.cust_details_table['columns']=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address")

        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Father Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="PostCode")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id number")
        self.cust_details_table.heading("address",text="Addresss")

        self.cust_details_table["show"]="headings"
        

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)


        self.cust_details_table.pack(fill=BOTH,expand=1)

        #create striped row tags
        self.cust_details_table.tag_configure('oddrow',background="white")
        self.cust_details_table.tag_configure('evenrow',background="lightblue")

        #calling to create database table
        self.create_table()
        self.fetch_data()

        def clicker(e):
                self.select_record()
        #bindings
        #my_tree.bind("<Double-1>",clicker)
        self.cust_details_table.bind("<ButtonRelease-1>",clicker)

    def select_record(self):
        self.cname_box.delete(0,END)
        self.mname_box.delete(0,END)
        self.combo_gender.current(0)
        self.postcode_box.delete(0,END)
        self.mobile_box.delete(0,END)
        self.email_box.delete(0,END)
        self.combo_nationality.current(0)
        self.combo_idproof.current(0)
        self.idnumber_box.delete(0,END)
        self.address_box.delete(0,END)

        #grab record number
        selected=self.cust_details_table.focus()
        values=self.cust_details_table.item(selected,'values')

        self.var_ref.set(values[0])
        self.cname_box.insert(0,values[1])
        self.mname_box.insert(0,values[2])
        self.var_gender.set(values[3])
        self.postcode_box.insert(0,values[4])
        self.mobile_box.insert(0,values[5])
        self.email_box.insert(0,values[6])
        self.var_nationality.set(values[7])
        self.var_idproof.set(values[8])
        self.idnumber_box.insert(0,values[9])
        self.address_box.insert(0,values[10])


    def search_record(self):
        if self.combo_search.get()=="select":
            messagebox.showerror("Error","Please select an option to search",parent=self.root)
        elif self.search_box.get()=="":
            messagebox.showerror("Error","Please fill the search entry",parent=self.root)
        else:
            lookup_record=self.search_box.get()
    
            #clear the treeview
            for record in self.cust_details_table.get_children():
                    self.cust_details_table.delete(record)

            if self.combo_search.get()=="Mobile":
                sql_cmd="SELECT * FROM customers_table WHERE mobile LIKE ?"
            elif self.combo_search.get()=="Name":
                sql_cmd="SELECT * FROM customers_table WHERE name LIKE ?"
            else:
                sql_cmd="SELECT * FROM customers_table WHERE ref LIKE ?"

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute(sql_cmd,(lookup_record,))
            records=c.fetchall()
            

            global curr_iid
            curr_iid=0

            for record in records:
                if curr_iid%2==0 :
                    self.cust_details_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]),tags=('evenrow',))
                else:
                    self.cust_details_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]),tags=('oddrow',))
                curr_iid+=1


            #commit changes
            conn.commit()

            #close our connection
            conn.close()
            
    def show_all(self):
        self.fetch_data()
        self.combo_search.current(0)
        self.search_box.delete(0,END)

    def check_user(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table WHERE ref=?",(self.var_ref.get(),))
        records=c.fetchall()
        print(records)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        return records==[]


    def update_record(self):
        
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)

        
        else:
            record=self.cust_details_table.selection()

            data=(
                self.var_ref.get(),
                self.cname_box.get(),
                self.mname_box.get(),
                self.combo_gender.get(),
                self.postcode_box.get(),
                self.mobile_box.get(),
                self.email_box.get(),
                self.combo_nationality.get(),
                self.combo_idproof.get(),
                self.idnumber_box.get(),
                self.address_box.get()
            )

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute("""UPDATE customers_table SET 
                name=:name,
                mother=:mname,
                gender=:gender,
                post=:post,
                mobile =:mobile,
                email =:email,
                nationality =:nationality,
                idproof =:idproof,
                idnumber =:idnumber,
                address =:address
                WHERE ref=:ref""",
                {
                    'name':self.cname_box.get(),
                    'mname':self.mname_box.get(),
                    'gender':self.combo_gender.get(),
                    'post':self.postcode_box.get(),
                    'mobile':self.mobile_box.get(),
                    'email':self.email_box.get(),
                    'nationality':self.combo_nationality.get(),
                    'idproof':self.combo_idproof.get(),
                    'idnumber':self.idnumber_box.get(),
                    'address':self.address_box.get(),

                    'ref':self.var_ref.get()
                }
            )

            #commit changes
            conn.commit()

            #close our connection
            conn.close()


            self.cust_details_table.item(record,text="",values=data)

            self.reset_data()

            #add a little message box
            messagebox.showinfo("Updated!","Your Record updated successfully",parent=self.root)

    
    def delete_record(self):
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)
        else:
            records = self.cust_details_table.selection()
            self.cust_details_table.delete(records[0])

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute("DELETE FROM customers_table WHERE ref=?",(self.var_ref.get(),)) 

            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            self.reset_data()

            #add a little message box
            messagebox.showinfo("Deleted!","Your Record deleted successfully",parent=self.root)

    
    def create_table(self):
        #do some database stuff
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        #create a table
        c.execute("""CREATE TABLE if not exists customers_table (
            ref integer,
            name text,
            mother integer,
            gender text,
            post text,
            mobile text,
            email text,
            nationality text,
            idproof text,
            idnumber text,
            address text
        )
        """)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

    def add_data(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table WHERE ref=?",(self.var_ref.get(),))
        records=c.fetchall()

        print(records)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()
        if records!=[]:
            messagebox.showerror("Error","User already existed",parent=self.root)

        elif self.mname_box.get()=="" or self.cname_box.get()=="" or self.mname_box.get()=="" or self.combo_gender.get()=="select" or self.postcode_box.get()=="" or self.mobile_box.get()=="" or self.email_box.get()=="" or self.combo_nationality.get()=="select" or self.combo_idproof.get()=="select" or self.idnumber_box.get()=="" or self.address_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                #create a database or connect to one that exists
                conn=sqlite3.connect('tree_crm.db')

                #create a cursor
                c = conn.cursor()

                #add new record
                c.execute("INSERT INTO customers_table VALUES(:ref,:name,:mname,:gender,:post,:mobile,:email,:nationality,:idproof,:idnumber,:address)",
                {
                    'ref':self.var_ref.get(),
                    'name':self.cname_box.get(),
                    'mname':self.mname_box.get(),
                    'gender':self.combo_gender.get(),
                    'post':self.postcode_box.get(),
                    'mobile':self.mobile_box.get(),
                    'email':self.email_box.get(),
                    'nationality':self.combo_nationality.get(),
                    'idproof':self.combo_idproof.get(),
                    'idnumber':self.idnumber_box.get(),
                    'address':self.address_box.get()
                }
                ) 

                #commit changes
                conn.commit()
            
                #close our connection
                conn.close()

                messagebox.showinfo("Success","Customer Details added successfully",parent=self.root)

                self.fetch_data()

                self.reset_data()

            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        #clear the treeview
        for record in self.cust_details_table.get_children():
                self.cust_details_table.delete(record)
                
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table")
        records=c.fetchall()
        

        global curr_iid
        curr_iid=0

        for record in records:
            if curr_iid%2==0 :
                self.cust_details_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]),tags=('evenrow',))
            else:
                self.cust_details_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10]),tags=('oddrow',))
            curr_iid+=1


        #commit changes
        conn.commit()

        #close our connection
        conn.close()

    def reset_data(self):
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.cname_box.delete(0,END)
        self.mname_box.delete(0,END)
        self.combo_gender.current(0)
        self.postcode_box.delete(0,END)
        self.mobile_box.delete(0,END)
        self.email_box.delete(0,END)
        self.combo_nationality.current(0)
        self.combo_idproof.current(0)
        self.idnumber_box.delete(0,END)
        self.address_box.delete(0,END)


if __name__=="__main__":
    root=Tk()
    obj=customer_window(root)
    root.mainloop()