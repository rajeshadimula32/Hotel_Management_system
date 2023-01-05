from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
from customer import customer_window
from room import room_booking_window
from details import Details_room

class hotel_management_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\first_hotel.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        label_img1=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        label_img1.place(x=0,y=0,width=1550,height=140)

        img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\logo_hotel.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        label_img2=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        label_img2.place(x=0,y=0,width=230,height=140)


        # title
        title_label=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        title_label.place(x=0,y=140,width=1550,height=50)

        #main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #menu label
        menu_bn=Button(main_frame,text="MENU",command=self.level_destroy, font=("times new roman",16,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        menu_bn.place(x=0,y=5,width=230)

        #button frame
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=40,width=230,height=220)

        customer_bn=Button(button_frame,text="CUSTOMER",command=self.cust_details, font=("times new roman",15,"bold"),bg="black",fg="gold",width=19)
        customer_bn.grid(row=0,column=0,pady=2)

        room_bn=Button(button_frame,text="ROOM",command=self.room_booking, font=("times new roman",15,"bold"),bg="black",fg="gold",width=19)
        room_bn.grid(row=1,column=0,pady=2)

        details_bn=Button(button_frame,text="DETAILS",command=self.details_room, font=("times new roman",15,"bold"),bg="black",fg="gold",width=19)
        details_bn.grid(row=2,column=0,pady=2)

        report_bn=Button(button_frame,text="REPORT",command=self.report, font=("times new roman",15,"bold"),bg="black",fg="gold",width=19)
        report_bn.grid(row=3,column=0,pady=2)

        logout_bn=Button(button_frame,text="LOGOUT",command=self.logout_project, font=("times new roman",15,"bold"),bg="black",fg="gold",width=19)
        logout_bn.grid(row=4,column=0,pady=2)
        
        
        #right side image
        img3=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\img3.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        label_img3=Label(main_frame,image=self.photoimage3,bd=4,relief=RIDGE)
        label_img3.place(x=225,y=0,width=1310,height=590)

    def report(self):
        new=Toplevel(self.root)
        new.title("Report")
        new.geometry("400x200+240+230")

        matter="""
                You can contact
                Adimula Rajesh
                contact No:8297273248
                email:rajeshadimula@gmail.com
        """

        label_text=Label(new,text=matter,font=("times new roman",15,"bold"))
        label_text.pack()

    def logout_project(self):
        response=messagebox.askyesno("Question","Are you sure to logout",parent=self.root)
        if response:
            self.root.destroy()

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer_window(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=room_booking_window(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=Details_room(self.new_window)
        
    def level_destroy(self):
        self.new_window.destroy()




if __name__=="__main__":
    root=Tk()
    obj=hotel_management_system(root)
    root.mainloop()