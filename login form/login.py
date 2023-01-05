from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
from hotel_management import hotel_management_system

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rajesh\OneDrive\Desktop\login form\background.jpg")

        label_bg=Label(self.root,image=self.bg)
        label_bg.place(x=0,y=0,relwidth=1,relheight=1)

        login_frame=Frame(self.root,bg="black")
        login_frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\login_logo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        label_img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        label_img1.place(x=730,y=175,width=100,height=100)

        get_str_label=Label(login_frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str_label.place(x=95,y=100)

        #labels
        username_label=Label(login_frame,text="Email Address",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_label.place(x=40,y=155)

        self.username_box=ttk.Entry(login_frame,font=("times new roman",15))
        self.username_box.place(x=40,y=180,width=270)

        password_label=Label(login_frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_label.place(x=40,y=225)

        self.password_box=ttk.Entry(login_frame,font=("times new roman",15))
        self.password_box.place(x=40,y=250,width=270)
                

        login_bn=Button(login_frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",command=self.login)
        login_bn.place(x=110,y=300,width=120,height=35)

        register_bn=Button(login_frame,text="New user Register",command=self.register_window, font=("times new roman",10,"bold"),borderwidth=0, fg="white",bg="black",activeforeground="white",activebackground="black")
        register_bn.place(x=20,y=350,width=160)


        password_bn=Button(login_frame,text="Forgot Password",command=self.forgot_password, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        password_bn.place(x=15,y=370,width=160)

    def login(self):
        if self.username_box.get()=="" or self.password_box.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            #create a database or connect to one that exists
            conn=sqlite3.connect('register_form.db')

            #create a cursor
            c = conn.cursor()

            #create a table
            c.execute("SELECT * FROM registrations WHERE email=?", (self.username_box.get(),))
            records=c.fetchall()
            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            if records==[]:
                messagebox.showerror("Error","Invalid username ")
            else:
                if records[0][6]!=self.password_box.get():
                    messagebox.showerror("Error","Invalid Password")
                else:
                    open_register=messagebox.askyesno("YesorNO","Access only admin")
                    print(open_register)
                    if open_register!=0:
                        self.new_window=Toplevel(self.root)
                        self.app=hotel_management_system(self.new_window)
                    else:
                        if not open_register:
                            return
                        
    
    #reset password
    def reset_password(self):
        if self.combo_security.get()=="Select" or self.security_ans_box.get()=="" or self.new_password_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            #create a database or connect to one that exists
            conn=sqlite3.connect('register_form.db')

            #create a cursor
            c = conn.cursor()

            #create a table
            c.execute("SELECT * FROM registrations WHERE email=?", (self.username_box.get(),))
            records=c.fetchall()
            print(records)

            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            if self.combo_security.get()!=records[0][4] or self.security_ans_box.get()!=records[0][5]:
                messagebox.showerror("Error","Wrong security question or answer",parent=self.root2)
            else:
                #create a database or connect to one that exists
                conn=sqlite3.connect('register_form.db')

                #create a cursor
                c = conn.cursor()

                c.execute("UPDATE registrations SET password=? WHERE email=?",(self.new_password_box.get(),self.username_box.get()))

                #commit changes
                conn.commit()

                #close our connection
                conn.close()

                messagebox.showinfo("Success","Password update successfully")

    # forgot Password
    def forgot_password(self):
        if self.username_box.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            #create a database or connect to one that exists
            conn=sqlite3.connect('register_form.db')

            #create a cursor
            c = conn.cursor()

            #create a table
            c.execute("SELECT * FROM registrations WHERE email=?", (self.username_box.get(),))
            records=c.fetchall()

            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            if records==[]:
                messagebox.showerror("Error","Invalid username ")
            else:
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                title_label=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red")
                title_label.place(x=0,y=10,relwidth=1)

                securityQ_label=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"))
                securityQ_label.place(x=50,y=80)

                self.combo_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security['values']=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)

                security_ans_label=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                security_ans_label.place(x=50,y=150)
                self.security_ans_box=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_ans_box.place(x=50,y=180,width=250)

                new_password_label=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                new_password_label.place(x=50,y=220)
                self.new_password_box=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_password_box.place(x=50,y=250,width=250)

                submit_bn=Button(self.root2,text="Save",command=self.reset_password, font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
                submit_bn.place(x=110,y=300,width=120,height=35)



    # function to open register window as a toplevel
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("New Registration")
        self.root.geometry("1600x900+0+0")

        #create a database or connect to one that exists
        conn=sqlite3.connect('register_form.db')

        #create a cursor
        c = conn.cursor()

        #create a table
        c.execute("""CREATE TABLE if not exists registrations (
            first_name text,
            last_name text,
            contact text,
            email text,
            security_ques text,
            security_ans text,
            password text
        )
        """)

        #commit changes
        conn.commit()

        #close our connection
        conn.close()


        # for background image
        self.bg_register=ImageTk.PhotoImage(file=r"C:\Users\Rajesh\OneDrive\Desktop\login form\background_registration.jpg")

        label_bg_register=Label(self.root,image=self.bg_register)
        label_bg_register.place(x=0,y=0,relwidth=1,relheight=1)
        
        #frame for registration
        register_frame=Frame(self.root,bg="white")
        register_frame.place(x=420,y=100,width=800,height=550)
        
        register_label=Label(register_frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_label.place(x=20,y=20)

        #labels and entries
        fn_label=Label(register_frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fn_label.place(x=50,y=100)
        self.fn_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.fn_box.place(x=50,y=130,width=250)

        ln_label=Label(register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        ln_label.place(x=370,y=100)
        self.ln_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.ln_box.place(x=370,y=130,width=250)

        contact_label=Label(register_frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact_label.place(x=50,y=170)
        self.contact_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.contact_box.place(x=50,y=200,width=250)

        email_label=Label(register_frame,text="Email Address",font=("times new roman",15,"bold"),bg="white")
        email_label.place(x=370,y=170)
        self.email_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.email_box.place(x=370,y=200,width=250)

        securityQ_label=Label(register_frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        securityQ_label.place(x=50,y=240)

        self.combo_security=ttk.Combobox(register_frame,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security['values']=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)

        security_ans_label=Label(register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_ans_label.place(x=370,y=240)
        self.security_ans_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.security_ans_box.place(x=370,y=270,width=250)

        password_label=Label(register_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password_label.place(x=50,y=310)
        self.password_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.password_box.place(x=50,y=340,width=250)

        conf_password_label=Label(register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        conf_password_label.place(x=370,y=310)
        self.conf_password_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
        self.conf_password_box.place(x=370,y=340,width=250)


        self.check_var=IntVar()
        #checkbutton
        check_bn=Checkbutton(register_frame,text="I Agree all terms & conditions",variable=self.check_var, font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white",activebackground="white")
        check_bn.place(x=50,y=380)

        img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\register.jpg")
        img2=img2.resize((200,80),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        
        save_bn=Button(register_frame,image=self.photoimage2,command=self.save_record, borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        save_bn.place(x=10,y=420,width=300)

        img3=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\loginbn.png")
        img3=img3.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        def login_now():
            self.root.destroy()

        login_now_bn=Button(register_frame,command=login_now, image=self.photoimage3,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        login_now_bn.place(x=330,y=430,width=300)


        img4=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\clearbn.png")
        img4=img4.resize((70,30),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        clear_entries_bn=Button(register_frame,image=self.photoimage4,borderwidth=0, command=self.clear_entries,bg="white",activebackground="white")
        clear_entries_bn.place(x=440,y=380,width=300)

    #function to save the record
    def save_record(self):
        if self.fn_box.get()=="" or self.ln_box.get()=="" or self.contact_box.get()=="" or self.email_box.get()=="" or self.combo_security.get()=="Select"or self.security_ans_box.get()==""  or self.password_box.get()=="" or self.conf_password_box.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.password_box.get()!=self.conf_password_box.get():
            messagebox.showerror("Error","Password & Confirm password should match",parent=self.root)
        elif self.check_var.get()==0:
            messagebox.showerror("Error","Please agree all terms and conditions",parent=self.root)
        else:
            #create a database or connect to one that exists
            conn=sqlite3.connect('register_form.db')

            #create a cursor
            c = conn.cursor()

            #create a table
            c.execute("SELECT * FROM registrations WHERE email= ?", (self.email_box.get(),))
            record=c.fetchall()
            print(record)
            
            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            if record!=[]:
                messagebox.showerror("Error","User already existed",parent=self.root)
            else:
                #create a database or connect to one that exists
                conn=sqlite3.connect('register_form.db')

                #create a cursor
                c = conn.cursor()

                #create a table
                c.execute("INSERT INTO registrations VALUES(:first,:last,:contact,:email,:securityQ,:securityA,:password)",
                {
                    'first':self.fn_box.get(),
                    'last':self.ln_box.get(),
                    'contact':self.contact_box.get(),
                    'email':self.email_box.get(),
                    'securityQ':self.combo_security.get(),
                    'securityA':self.security_ans_box.get(),
                    'password':self.password_box.get(),
                }
                ) 
                
                #commit changes
                conn.commit()

                #close our connection
                conn.close()

                messagebox.showinfo("Success","User registerd successfully !!!",parent=self.root)

                #clear all entries
                self.fn_box.delete(0,END)
                self.ln_box.delete(0,END)
                self.contact_box.delete(0,END)
                self.email_box.delete(0,END)
                self.security_ans_box.delete(0,END)
                self.password_box.delete(0,END)
                self.conf_password_box.delete(0,END)
                self.combo_security.current('0')
    

    def clear_entries(self):
        self.fn_box.delete(0,END)
        self.ln_box.delete(0,END)
        self.contact_box.delete(0,END)
        self.email_box.delete(0,END)
        self.security_ans_box.delete(0,END)
        self.password_box.delete(0,END)
        self.conf_password_box.delete(0,END)
        self.combo_security.current('0')
        self.check_var.initialize(0)



if __name__ == "__main__":
    main()