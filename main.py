from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from function_ import resize_custom, get_monitor,get_geometry

def login():
        if name_.get() == "" or pass_.get() == "":
            messagebox.showerror("Error", "please Enter the username and password")
        elif name_.get() =="postgres" and pass_.get() == "2110":
            root.destroy()
            import My_Routine
            My_Routine.win
        else:
            messagebox.showerror("Error", "Enter Valid one")

root=Tk()
root.title("Login Window")
get_geometry(root)
get_mon=get_monitor()

bg_icon = ImageTk.PhotoImage(file = "template/img/main_bg.jpg")
user_icon = ImageTk.PhotoImage(resize_custom('template/img/login.png', 40, 40))
pass_icon = ImageTk.PhotoImage(resize_custom('template/img/padlock.png', 44, 44))
logo_icon = ImageTk.PhotoImage(resize_custom('template/img/logo.png', 150, 150))

name_ = StringVar()
pass_ = StringVar()

bg_lable=Label(root,image=bg_icon).pack()

title=Label(root,text="Login Page",font = ("Times New Roman", 40 ),bg="#39353d",fg="white",bd=10)
title.place(x = 0, y = 0, relwidth = 1)

main_Frame=Frame(root,width=1000)
main_Frame.config(bg="#775e8a")
main_Frame.place(relx=.5,rely=.45,anchor="c")

logo=Label(main_Frame,image=logo_icon,bd=5,bg="white").grid(row=0,columnspan=2,pady=20)

userL=Label(main_Frame,text="Username",image=user_icon,compound=LEFT,font=("Times New Roman", 16 )).grid(row = 1, column = 0, padx = 20, pady = 10,sticky = "w")
userE=Entry(main_Frame,textvariable=name_,bd=2,font=("Times New Roman",15))
userE.grid(row=1,column=1,padx=20,sticky='w')
userE.focus_set()

passL=Label(main_Frame,text="Password",image=pass_icon,compound=LEFT,font=("Times New Roman", 16 )).grid(row = 2, column = 0, padx = 20, pady = 10,sticky = "w")
passE=Entry(main_Frame,textvariable=pass_,show="*",bd=2,font=("Times New Roman",15))
passE.grid(row=2,column=1,padx=20,sticky='w')

LB=Button(main_Frame,text="Login",command=login,width=15,font=("Times New Roman", 14 ))
LB.grid(row=3,columnspan=2,pady=10)

root.mainloop()




