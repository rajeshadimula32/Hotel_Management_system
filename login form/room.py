from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import random
from time import strftime
from datetime import datetime


class room_booking_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking page")
        self.root.geometry("1290x550+235+230")

        # title
        title_label=Label(self.root,text="ROOM BOOKING",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title_label.place(x=0,y=0,width=1290,height=50)


        img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\logo_hotel.jpg")
        img2=img2.resize((102,52),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label_img2=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        label_img2.place(x=0,y=0,width=102,height=52)

        #label frame
        label_frame_left=LabelFrame(self.root,bd=1,relief=RIDGE,text="RoomBooking Details",padx=4,font=("times new roman",12,"bold"))
        label_frame_left.place(x=5,y=50,width=420,height=490)

        # labels and entries
        id_label=Label(label_frame_left,text="ID Number",font=("times new roman",12,"bold"),padx=4,pady=6)
        id_label.grid(row=0,column=0,sticky=W)
        self.id_box=ttk.Entry(label_frame_left, width=20,font=("times new roman",12,"bold"))
        self.id_box.grid(row=0,column=1,sticky=W)

        fetch_bn=Button(label_frame_left,command=self.fetch_contact, text="Fetch Data", font=("times new roman",11,"bold"),bg="black",fg="gold",width=9)
        fetch_bn.place(x=315,y=4)

        checkin_label=Label(label_frame_left,text="Check in Date",font=("times new roman",12,"bold"),padx=4,pady=6)
        checkin_label.grid(row=1,column=0,sticky=W)
        self.checkin_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.checkin_box.grid(row=1,column=1)

        checkout_label=Label(label_frame_left,text="Check out Date",font=("times new roman",12,"bold"),padx=4,pady=6)
        checkout_label.grid(row=2,column=0,sticky=W)
        self.checkout_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold")) 
        self.checkout_box.grid(row=2,column=1)

        self.var_room_type=StringVar()

        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT roomtype FROM details_table")
        room_type_records=c.fetchall()
        print(room_type_records)
        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        roomtype_label=Label(label_frame_left,text="Room Type",font=("times new roman",12,"bold"),padx=4,pady=6)
        roomtype_label.grid(row=3,column=0,sticky=W)
        self.combo_roomtype=ttk.Combobox(label_frame_left,textvariable=self.var_room_type, state="readonly" ,font=("times new roman",12,"bold"),width=27)
        self.combo_roomtype['values']=room_type_records
        self.combo_roomtype.grid(row=3,column=1)
        self.combo_roomtype.current(0)

        self.var_room_no=StringVar()

        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT roomno FROM details_table")
        room_no_records=c.fetchall()
        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        available_room_label=Label(label_frame_left,text="Available Room",font=("times new roman",12,"bold"),padx=4,pady=6)
        available_room_label.grid(row=4,column=0,sticky=W)
        self.combo_roomno=ttk.Combobox(label_frame_left, textvariable=self.var_room_no, state="readonly" ,font=("times new roman",12,"bold"),width=27)
        self.combo_roomno['values']=room_no_records
        self.combo_roomno.grid(row=4,column=1)
        self.combo_roomno.current(0)

        noofdays_label=Label(label_frame_left,text="No of Days",font=("times new roman",12,"bold"),padx=4,pady=6)
        noofdays_label.grid(row=5,column=0,sticky=W)
        self.noofdays_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.noofdays_box.grid(row=5,column=1)

        paidtax_label=Label(label_frame_left,text="Paid Tax",font=("times new roman",12,"bold"),padx=4,pady=6)
        paidtax_label.grid(row=6,column=0,sticky=W)
        self.paidtax_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.paidtax_box.grid(row=6,column=1)

        subtotal_label=Label(label_frame_left,text="Sub Total",font=("times new roman",12,"bold"),padx=4,pady=6)
        subtotal_label.grid(row=7,column=0,sticky=W)
        self.subtotal_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.subtotal_box.grid(row=7,column=1)

        totalcost_label=Label(label_frame_left,text="Total Cost",font=("times new roman",12,"bold"),padx=4,pady=6)
        totalcost_label.grid(row=8,column=0,sticky=W)
        self.totalcost_box=ttk.Entry(label_frame_left,width=29,font=("times new roman",12,"bold"))
        self.totalcost_box.grid(row=8,column=1)

        #bill button
        bill_bn=Button(label_frame_left,text="Bill",command=self.total, font=("times new roman",10,"bold"),bg="black",fg="gold",width=9)
        bill_bn.grid(row=9,column=1,padx=1,sticky=E)

        #buttons
        bn_frame=Frame(label_frame_left)
        bn_frame.place(x=0,y=360,width=412,height=40)

        add_bn=Button(bn_frame,text="Add",command=self.add_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        add_bn.grid(row=0,column=0,padx=1)

        update_bn=Button(bn_frame,text="Update",command=self.update_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        update_bn.grid(row=0,column=1,padx=1)

        delete_bn=Button(bn_frame,text="Delete",command=self.delete_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        delete_bn.grid(row=0,column=2,padx=1)

        reset_bn=Button(bn_frame,text="Reset",command=self.reset_data, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        reset_bn.grid(row=0,column=3,padx=1)


        #right side image
        img3=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\logo_hotel.jpg")
        img3=img3.resize((515,300),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        label_img3=Label(self.root,image=self.photoimage3,bd=2,relief=RIDGE)
        label_img3.place(x=770,y=55,width=515,height=300)


        #table frame
        table_frame=LabelFrame(self.root,bd=1,relief=RIDGE,text="View Details and Search System",padx=4,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=280,width=850,height=490)

        search_label=Label(table_frame,text="Search by",font=("times new roman",13,"bold"),bg="brown",fg="white")
        search_label.grid(row=0,column=0,sticky=W,padx=2,pady=2)

        self.combo_search=ttk.Combobox(table_frame,state="readonly" ,font=("times new roman",13,"bold"),width=20)
        self.combo_search['values']=("Contact","Room")
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
        tree_frame.place(x=0,y=50,width=850,height=190)

        

        scroll_x=ttk.Scrollbar(tree_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tree_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(tree_frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        #define our columns
        self.room_table['columns']=("contact","checkinDate","checkoutDate","roomtype","room","noofDays","total")

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkinDate",text="Check-in")
        self.room_table.heading("checkoutDate",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("room",text="Room No")
        self.room_table.heading("noofDays",text="No of Days")
        self.room_table.heading("total",text="Total Cost")

        self.room_table["show"]="headings"
        

        self.room_table.column("contact",width=100)
        self.room_table.column("checkinDate",width=100)
        self.room_table.column("checkoutDate",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("room",width=100)
        self.room_table.column("noofDays",width=100)
        self.room_table.column("total",width=100)
        


        self.room_table.pack(fill=BOTH,expand=1)

        #create striped row tags
        self.room_table.tag_configure('oddrow',background="white")
        self.room_table.tag_configure('evenrow',background="lightblue")
        
        #delete database table
        #self.delete_table()

        #calling to create database table
        self.create_table()
        self.fetch_data()

        def clicker(e):
                self.select_record()
        #bindings
        #my_tree.bind("<Double-1>",clicker)
        self.room_table.bind("<ButtonRelease-1>",clicker)

    def search_record(self):
        if self.combo_search.get()=="select":
            messagebox.showerror("Error","Please select an option to search",parent=self.root)
        elif self.search_box.get()=="":
            messagebox.showerror("Error","Please fill the search entry",parent=self.root)
        else:
            lookup_record=self.search_box.get()
    
            #clear the treeview
            for record in self.room_table.get_children():
                    self.room_table.delete(record)

            if self.combo_search.get()=="Contact":
                sql_cmd="SELECT * FROM rooms_table WHERE contact LIKE ?"
            else:
                sql_cmd="SELECT * FROM rooms_table WHERE room LIKE ?"

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
                    self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('evenrow',))
                else:
                    self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('oddrow',))
                curr_iid+=1


            #commit changes
            conn.commit()

            #close our connection
            conn.close()
            
    def show_all(self):
        self.fetch_data()
        self.combo_search.current(0)
        self.search_box.delete(0,END)

    def delete_table(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("DROP TABLE rooms_table")

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

    def total(self):
        if self.contact_box.get()=="" or self.checkin_box.get()=="" or self.checkin_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            inDate=self.checkin_box.get()
            outDate=self.checkout_box.get()
            inDate=datetime.strptime(inDate,"%d/%m/%Y")
            outDate=datetime.strptime(outDate,"%d/%m/%Y")

            self.noofdays_box.delete(0,END)
            self.subtotal_box.delete(0,END)
            self.paidtax_box.delete(0,END)
            self.totalcost_box.delete(0,END)

            self.noofdays_box.insert(0,abs(outDate-inDate).days)

            roomcost=0.0

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute("SELECT charge FROM details_table WHERE roomtype=?",(self.combo_roomtype.get(),))
            records=c.fetchall()

            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            roomcost=records[0][0]

            subtotal=roomcost*int(self.noofdays_box.get())
            taxpaid=0.05*subtotal
            totalcost=subtotal+taxpaid

            self.subtotal_box.insert(0,subtotal)
            self.paidtax_box.insert(0,taxpaid)
            self.totalcost_box.insert(0,totalcost)

    def select_record(self):
        self.contact_box.delete(0,END)
        self.checkin_box.delete(0,END)
        self.checkout_box.delete(0,END)
        self.combo_roomtype.current(0)
        self.combo_roomno.current(0)
        self.noofdays_box.delete(0,END)
        self.totalcost_box.delete(0,END)

        #grab record number
        selected=self.room_table.focus()
        values=self.room_table.item(selected,'values')

        self.contact_box.insert(0,values[0])
        self.checkin_box.insert(0,values[1])
        self.checkout_box.insert(0,values[2])
        self.var_room_type.set(values[3])
        self.var_room_no.set(values[4])
        self.noofdays_box.insert(0,values[5])
        self.totalcost_box.insert(0,values[6])

    def check_user(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM rooms_table WHERE contact=?",(self.contact_box.get(),))
        records=c.fetchall()


        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        return records==[]


    def update_record(self):
        
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)

        
        else:
            record=self.room_table.selection()

            data=(
                self.contact_box.get(),
                self.checkin_box.get(),
                self.checkout_box.get(),
                self.var_room_type.get(),
                self.var_room_no.get(),
                self.noofdays_box.get(),
                self.totalcost_box.get()
            )

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute("""UPDATE rooms_table SET 
                checkin=:checkin,
                checkout=:checkout,
                roomtype=:roomtype,
                room=:room,
                noofDays=:noofDays,
                total=:total
                WHERE contact=:contact""",
                {
                    
                    'checkin':self.checkin_box.get(),
                    'checkout':self.checkout_box.get(),
                    'roomtype':self.var_room_type.get(),
                    'room':self.var_room_no.get(),
                    'noofDays':self.noofdays_box.get(),
                    'total':self.totalcost_box.get(),

                    'contact':self.contact_box.get(),
                }
            )

            #commit changes
            conn.commit()

            #close our connection
            conn.close()


            self.room_table.item(record,text="",values=data)

            self.reset_data()

            #add a little message box
            messagebox.showinfo("Updated!","Your Record updated successfully",parent=self.root)
        

    def delete_record(self):
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)
        else:
            response=messagebox.askyesno("Delete","Do you want to delete this customer",parent=self.root)
            if response!=0:
                records = self.room_table.selection()
                self.room_table.delete(records[0])

                #create a database or connect to one that exists
                conn=sqlite3.connect('tree_crm.db')

                #create a cursor
                c = conn.cursor()

                c.execute("DELETE FROM rooms_table WHERE contact=?",(self.contact_box.get(),)) 

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
        c.execute("""CREATE TABLE if not exists rooms_table (
            contact text,
            checkin text,
            checkout text,
            roomtype text,
            room text PRIMARY KEY,
            noofDays text,
            total text
        )
        """)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

    def check_customer(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table WHERE mobile=?",(self.contact_box.get(),))
        records=c.fetchall()


        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        return records==[]

    def add_record(self):
        if self.contact_box.get()=="" or self.checkin_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            if self.check_customer():
                messagebox.showerror("Error","Contact number not existed",parent=self.root)
            else:
                try:
                    #create a database or connect to one that exists
                    conn=sqlite3.connect('tree_crm.db')

                    #create a cursor
                    c = conn.cursor()

                    #add new record
                    c.execute("INSERT INTO rooms_table VALUES(:contact,:checkin,:checkout,:roomtype,:room,:noofDays,:total)",
                    {
                        'contact':self.contact_box.get(),
                        'checkin':self.checkin_box.get(),
                        'checkout':self.checkout_box.get(),
                        'roomtype':self.var_room_type.get(),
                        'room':self.var_room_no.get(),
                        'noofDays':self.noofdays_box.get(),
                        'total':self.totalcost_box.get()
                    }
                    ) 

                    #commit changes
                    conn.commit()
                
                    #close our connection
                    conn.close()

                    messagebox.showinfo("Success","Room booked successfully",parent=self.root)

                    self.fetch_data()

                    self.reset_data()

                except Exception as es:
                    messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    def reset_data(self):
        self.contact_box.delete(0,END)
        self.checkin_box.delete(0,END)
        self.checkout_box.delete(0,END)
        self.combo_roomtype.current(0)
        self.combo_roomno.current(0)
        self.noofdays_box.delete(0,END)
        self.subtotal_box.delete(0,END)
        self.paidtax_box.delete(0,END)
        self.totalcost_box.delete(0,END)

    def fetch_data(self):
        #clear the treeview
        for record in self.room_table.get_children():
                self.room_table.delete(record)
                
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM rooms_table")
        records=c.fetchall()

        global curr_iid
        curr_iid=0

        for record in records:
            if curr_iid%2==0 :
                self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('evenrow',))
            else:
                self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('oddrow',))
            curr_iid+=1


        #commit changes
        conn.commit()

        #close our connection
        conn.close()
    
    
    
    def fetch_contact(self):
        if self.id_box.get()=="":
            messagebox.showerror("Error","Please Enter ID number",parent=self.root)
        else:
            lookup_record=self.id_box.get()
            sql_cmd="SELECT * FROM customers_table WHERE idnumber LIKE ?"
            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute(sql_cmd,(lookup_record,))
            records=c.fetchall()

            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            if records==[]:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                show_data_frame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                show_data_frame.place(x=455,y=55,width=300,height=200)

                name_label=Label(show_data_frame,text="Name",font=("arial",12,"bold"))
                name_label.place(x=0,y=0)

                name_data=Label(show_data_frame,text=": "+records[0][1],font=("arial",12,"bold"))
                name_data.place(x=90,y=0)

                gender_label=Label(show_data_frame,text="Gender",font=("arial",12,"bold"))
                gender_label.place(x=0,y=30)

                gender_data=Label(show_data_frame,text=": "+records[0][3],font=("arial",12,"bold"))
                gender_data.place(x=90,y=30)

                email_label=Label(show_data_frame,text="Email",font=("arial",12,"bold"))
                email_label.place(x=0,y=60)

                email_data=Label(show_data_frame,text=": "+records[0][6],font=("arial",12,"bold"))
                email_data.place(x=90,y=60)

                nationality_label=Label(show_data_frame,text="Nationality",font=("arial",12,"bold"))
                nationality_label.place(x=0,y=90)

                nationality_data=Label(show_data_frame,text=": "+records[0][7],font=("arial",12,"bold"))
                nationality_data.place(x=90,y=90)

                address_label=Label(show_data_frame,text="Address",font=("arial",12,"bold"))
                address_label.place(x=0,y=120)

                address_data=Label(show_data_frame,text=": "+records[0][10],font=("arial",12,"bold"))
                address_data.place(x=90,y=120)


    

if __name__=="__main__":
    root=Tk()
    obj=room_booking_window(root)
    root.mainloop()