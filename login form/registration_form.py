from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("New Registration")
root.geometry("1600x900+0+0")

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

'''
#connect to mysql
mydb=mysql.connector.connect(
host="localhost",
user="root",
passwd="Raje@2020",
database="databs"
)

#check to see if connection to MySQL was created
#print(mydb)

#create a cursor
my_cursor=mydb.cursor()

#create a database
#my_cursor.execute("CREATE DATABASE databs")

# test to see if databbase was created
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
    #   print(db)

#create a table

my_cursor.execute("""CREATE TABLE register_table(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact VARCHAR(255),
    email VARCHAR(255) PRIMARY KEY,
    security_ques VARCHAR(255),
    security_ans VARCHAR(255),
    password VARCHAR(255)
)
""")

#alter table
my_cursor.execute("""ALTER TABLE customers ADD(
    email VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    phone VARCHAR(255)
)""")

#show table
my_cursor.execute("SELECT * FROM register_table")
ans=""
for data in my_cursor.description:
    ans+=data[0]+","
print(ans)
'''



# for background image
bg_register=ImageTk.PhotoImage(file=r"C:\Users\Rajesh\OneDrive\Desktop\login form\background_registration.jpg")

label_bg_register=Label(root,image=bg_register)
label_bg_register.place(x=0,y=0,relwidth=1,relheight=1)

#frame for registration
register_frame=Frame(root,bg="white")
register_frame.place(x=420,y=100,width=800,height=550)

register_label=Label(register_frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
register_label.place(x=20,y=20)

#labels and entries
fn_label=Label(register_frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
fn_label.place(x=50,y=100)
fn_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
fn_box.place(x=50,y=130,width=250)

ln_label=Label(register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
ln_label.place(x=370,y=100)
ln_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
ln_box.place(x=370,y=130,width=250)

contact_label=Label(register_frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
contact_label.place(x=50,y=170)
contact_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
contact_box.place(x=50,y=200,width=250)

email_label=Label(register_frame,text="Email Address",font=("times new roman",15,"bold"),bg="white")
email_label.place(x=370,y=170)
email_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
email_box.place(x=370,y=200,width=250)

securityQ_label=Label(register_frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
securityQ_label.place(x=50,y=240)

combo_security=ttk.Combobox(register_frame,font=("times new roman",15,"bold"),state="readonly")
combo_security['values']=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
combo_security.place(x=50,y=270,width=250)
combo_security.current(0)

security_ans_label=Label(register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
security_ans_label.place(x=370,y=240)
security_ans_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
security_ans_box.place(x=370,y=270,width=250)

password_label=Label(register_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
password_label.place(x=50,y=310)
password_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
password_box.place(x=50,y=340,width=250)

conf_password_label=Label(register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
conf_password_label.place(x=370,y=310)
conf_password_box=ttk.Entry(register_frame,font=("times new roman",15,"bold"))
conf_password_box.place(x=370,y=340,width=250)


check_var=IntVar()
#checkbutton
check_bn=Checkbutton(register_frame,text="I Agree all terms & conditions",variable=check_var, font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white",activebackground="white")
check_bn.place(x=50,y=380)

img2=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\register.jpg")
img2=img2.resize((200,80),Image.Resampling.LANCZOS)
photoimage2=ImageTk.PhotoImage(img2)

#function to save the record
def save_record():
    if fn_box.get()=="" or ln_box.get()=="" or contact_box.get()=="" or email_box.get()=="" or combo_security.get()=="Select"or security_ans_box.get()==""  or password_box.get()=="" or conf_password_box.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif password_box.get()!=conf_password_box.get():
        messagebox.showerror("Error","Password & Confirm password should match")
    elif check_var.get()==0:
        messagebox.showerror("Error","Please agree all terms and conditions")
    else:
        #create a database or connect to one that exists
        conn=sqlite3.connect('register_form.db')

        #create a cursor
        c = conn.cursor()

        #create a table
        c.execute("SELECT * FROM registrations WHERE email LIKE ?", ('%' + email_box.get() + '%',))
        record=c.fetchall()
        print(record)
        
        #commit changes
        conn.commit()

        #close our connection
        conn.close()

        if record!=[]:
            messagebox.showerror("Error","User already existed")
        else:
            #create a database or connect to one that exists
            conn=sqlite3.connect('register_form.db')

            #create a cursor
            c = conn.cursor()

            #create a table
            c.execute("INSERT INTO registrations VALUES(:first,:last,:contact,:email,:securityQ,:securityA,:password)",
            {
                'first':fn_box.get(),
                'last':ln_box.get(),
                'contact':contact_box.get(),
                'email':email_box.get(),
                'securityQ':combo_security.get(),
                'securityA':security_ans_box.get(),
                'password':password_box.get(),
            }
            ) 
            
            #commit changes
            conn.commit()

            #close our connection
            conn.close()

            messagebox.showinfo("Success","User registerd successfully !!!")

            #clear all entries
            fn_box.delete(0,END)
            ln_box.delete(0,END)
            contact_box.delete(0,END)
            email_box.delete(0,END)
            security_ans_box.delete(0,END)
            password_box.delete(0,END)
            conf_password_box.delete(0,END)
            combo_security.current('0')




save_bn=Button(register_frame,image=photoimage2,command=save_record, borderwidth=0,cursor="hand2",bg="white",activebackground="white")
save_bn.place(x=10,y=420,width=300)

img3=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\loginbn.png")
img3=img3.resize((200,100),Image.Resampling.LANCZOS)
photoimage3=ImageTk.PhotoImage(img3)

login_now_bn=Button(register_frame,image=photoimage3,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
login_now_bn.place(x=330,y=430,width=300)

def clear_entries():
    fn_box.delete(0,END)
    ln_box.delete(0,END)
    contact_box.delete(0,END)
    email_box.delete(0,END)
    security_ans_box.delete(0,END)
    password_box.delete(0,END)
    conf_password_box.delete(0,END)
    combo_security.current('0')
    check_var.initialize(0)


img4=Image.open(r"C:\Users\Rajesh\OneDrive\Desktop\login form\clearbn.png")
img4=img4.resize((70,30),Image.Resampling.LANCZOS)
photoimage4=ImageTk.PhotoImage(img4)

clear_entries_bn=Button(register_frame,image=photoimage4,borderwidth=0, command=clear_entries,bg="white",activebackground="white")
clear_entries_bn.place(x=440,y=380,width=300)


root.mainloop()