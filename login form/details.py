from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import random
from time import strftime
from datetime import datetime


class Details_room:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1290x550+235+230")

        # title
        title_label=Label(self.root,text="ROOM ADDING DEPARTMENT",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title_label.place(x=0,y=0,width=1290,height=50)


        img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\logo_hotel.jpg")
        img2=img2.resize((102,52),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label_img2=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        label_img2.place(x=0,y=0,width=102,height=52)

        #label frame
        label_frame_left=LabelFrame(self.root,bd=1,relief=RIDGE,text="New Room Add",padx=4,font=("times new roman",15,"bold"))
        label_frame_left.place(x=20,y=100,width=500,height=380)

        floor_label=Label(label_frame_left,text="Floor",font=("times new roman",12,"bold"),padx=4,pady=6)
        floor_label.grid(row=0,column=0,sticky=W,padx=20,pady=2)
        self.floor_box=ttk.Entry(label_frame_left, width=20,font=("times new roman",12,"bold"))
        self.floor_box.grid(row=0,column=1,sticky=W,padx=20)

        roomno_label=Label(label_frame_left,text="Room No",font=("times new roman",12,"bold"),padx=4,pady=6)
        roomno_label.grid(row=1,column=0,sticky=W,padx=20,pady=2)
        self.roomno_box=ttk.Entry(label_frame_left, width=20,font=("times new roman",12,"bold"))
        self.roomno_box.grid(row=1,column=1,sticky=W,padx=20)

        roomtype_label=Label(label_frame_left,text="Room Type",font=("times new roman",12,"bold"),padx=4,pady=6)
        roomtype_label.grid(row=2,column=0,sticky=W,padx=20,pady=2)
        self.roomtype_box=ttk.Entry(label_frame_left, width=20,font=("times new roman",12,"bold"))
        self.roomtype_box.grid(row=2,column=1,sticky=W,padx=20)

        charge_label=Label(label_frame_left,text="Charges Per Day",font=("times new roman",12,"bold"),padx=4,pady=6)
        charge_label.grid(row=3,column=0,sticky=W,padx=20,pady=2)
        self.charge_box=ttk.Entry(label_frame_left, width=20,font=("times new roman",12,"bold"))
        self.charge_box.grid(row=3,column=1,sticky=W,padx=20)


        #buttons
        bn_frame=Frame(label_frame_left)
        bn_frame.place(x=0,y=250,width=412,height=40)

        add_bn=Button(bn_frame,text="Add",command=self.add_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        add_bn.grid(row=0,column=0,padx=1)

        update_bn=Button(bn_frame,text="Update",command=self.update_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        update_bn.grid(row=0,column=1,padx=1)

        delete_bn=Button(bn_frame,text="Delete",command=self.delete_record, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        delete_bn.grid(row=0,column=2,padx=1)

        reset_bn=Button(bn_frame,text="Reset",command=self.reset_data, font=("times new roman",12,"bold"),bg="black",fg="gold",width=9)
        reset_bn.grid(row=0,column=3,padx=1)

        #table frame
        tree_frame=LabelFrame(self.root,bd=1,relief=RIDGE,text="Show Room",padx=4,font=("times new roman",15,"bold"))
        tree_frame.place(x=600,y=100,width=600,height=380)


        #Add some style
        style=ttk.Style()

        #chage selected color
        style.map('Treeview',background=[('selected',"#447711")])
        
        

        scroll_x=ttk.Scrollbar(tree_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tree_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(tree_frame,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        #define our columns
        self.room_table['columns']=("floor","roomno","roomtype","charge")

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("charge",text="Charges per Day")
        

        self.room_table["show"]="headings"
        

        self.room_table.column("floor",width=80,anchor=CENTER)
        self.room_table.column("roomno",width=80,anchor=CENTER)
        self.room_table.column("roomtype",width=80,anchor=CENTER)
        self.room_table.column("charge",width=80,anchor=CENTER)


        self.room_table.pack(fill=BOTH,expand=1)

        #create striped row tags
        self.room_table.tag_configure('oddrow',background="white")
        self.room_table.tag_configure('evenrow',background="lightblue")

        #self.delete_table()
        self.create_table()
        self.fetch_data()

        def clicker(e):
                self.select_record()
        #bindings
        #my_tree.bind("<Double-1>",clicker)
        self.room_table.bind("<ButtonRelease-1>",clicker)
    
    def delete_table(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("DROP TABLE details_table")

        #commit changes
        conn.commit()

        #close our connection
        conn.close()
    
    def select_record(self):
        self.floor_box.delete(0,END)
        self.roomno_box.delete(0,END)
        self.roomtype_box.delete(0,END)
        self.charge_box.delete(0,END)
        
        #grab record number
        selected=self.room_table.focus()
        values=self.room_table.item(selected,'values')

        self.floor_box.insert(0,values[0])
        self.roomno_box.insert(0,values[1])
        self.roomtype_box.insert(0,values[2])
        self.charge_box.insert(0,values[3])
    
    def check_user(self):
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM details_table WHERE roomno=?",(self.roomno_box.get(),))
        records=c.fetchall()

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        return records==[]

    def delete_record(self):
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)
        else:
            response=messagebox.askyesno("Delete","Do you want to delete record",parent=self.root)
            if response!=0:
                records = self.room_table.selection()
                self.room_table.delete(records[0])

                #create a database or connect to one that exists
                conn=sqlite3.connect('tree_crm.db')

                #create a cursor
                c = conn.cursor()

                c.execute("DELETE FROM details_table WHERE roomno=?",(self.roomno_box.get(),)) 

                #commit changes
                conn.commit()

                #close our connection
                conn.close()

                self.reset_data()

                #add a little message box
                messagebox.showinfo("Deleted!","Your Record deleted successfully",parent=self.root)
    
    def update_record(self):
        if self.check_user():
            messagebox.showerror("Error","Please select a record",parent=self.root)
        else:
            record=self.room_table.selection()

            data=(
                self.floor_box.get(),
                self.roomno_box.get(),
                self.roomtype_box.get(),
                self.charge_box.get()
            )

            #create a database or connect to one that exists
            conn=sqlite3.connect('tree_crm.db')

            #create a cursor
            c = conn.cursor()

            c.execute("""UPDATE details_table SET 
                floor=:floor,
                roomtype=:roomtype,
                charge=:charge
    
                WHERE roomno=:roomno""",
                {
                    
                    'floor':self.floor_box.get(),
                    'roomtype':self.roomtype_box.get(),
                    'charge':self.charge_box.get(),

                    'roomno':self.roomno_box.get()
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

    def add_record(self):
        if self.floor_box.get()=="" or self.roomno_box.get()=="" or self.roomtype_box.get()=="" or self.charge_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                #create a database or connect to one that exists
                conn=sqlite3.connect('tree_crm.db')

                #create a cursor
                c = conn.cursor()

                #add new record
                c.execute("INSERT INTO details_table VALUES(:floor,:roomno,:roomtype,:charge)",
                {
                    'floor':self.floor_box.get(),
                    'roomno':self.roomno_box.get(),
                    'roomtype':self.roomtype_box.get(),
                    'charge':self.charge_box.get()
                }
                ) 

                #commit changes
                conn.commit()
            
                #close our connection
                conn.close()

                messagebox.showinfo("Success","New Room Added successfully",parent=self.root)

                self.fetch_data()

                self.reset_data()

            except Exception as es:
                messagebox.showwarning("Warning","Room is already added",parent=self.root)

    def reset_data(self):
        self.floor_box.delete(0,END)
        self.roomno_box.delete(0,END)
        self.roomtype_box.delete(0,END)
        self.charge_box.delete(0,END)

    def fetch_data(self):
        #clear the treeview
        for record in self.room_table.get_children():
                self.room_table.delete(record)
                
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM details_table")
        records=c.fetchall()

        global curr_iid
        curr_iid=0

        for record in records:
            if curr_iid%2==0 :
                self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3]),tags=('evenrow',))
            else:
                self.room_table.insert(parent='',index='end',iid=curr_iid,text="",values=(record[0],record[1],record[2],record[3]),tags=('oddrow',))
            curr_iid+=1


        #commit changes
        conn.commit()

        #close our connection
        conn.close()
    
    def create_table(self):
        #do some database stuff
        #create a database or connect to one that exists
        conn=sqlite3.connect('tree_crm.db')

        #create a cursor
        c = conn.cursor()

        #create a table
        c.execute("""CREATE TABLE if not exists details_table (
            floor text,
            roomno text PRIMARY KEY,
            roomtype text,
            charge integer
        )
        """)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Details_room(root)
    root.mainloop()