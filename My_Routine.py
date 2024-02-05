from tkinter import *
from datetime import date
import time
import back
from function_ import get_monitor,get_geometry
from PIL import ImageTk

def get_selected_row(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    print(selected_row)
    e1.delete(0,END)
    e1.insert(END,selected_row[0])
    e2.delete(0,END)
    e2.insert(END,selected_row[1])
    e3.delete(0,END)
    e3.insert(END,selected_row[2])
    e4.delete(0,END)
    e4.insert(END,selected_row[3])
    e5.delete(0,END)
    e5.insert(END,selected_row[4])
    e6.delete(0,END)
    e6.insert(END,selected_row[5])

def delete_command():
    back.delete(selected_row[1])

def view_command():
    list.delete(0,END)
    for row in back.view():
        list.insert(END,row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def search_command():
    list.delete(0,END)
    for row in back.search(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get()):
        list.insert(END,row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def add_command():
    back.insert(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get())
    list.delete(0,END)
    list.insert(END,(date_text.get(),time_text.get(),study_text.get(),hour_text.get(),note_text.get(),log_text.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)


win = Tk()
win.title("MY Daily Database")
get_geometry(win)
get_mon=get_monitor()

main_icon = ImageTk.PhotoImage(file = "template/img/daily.jpg")
bg_main=Label(win,image=main_icon).grid(row=0,column=0)
title=Label(win,text="MY ROUTINE",font = ("Times New Roman", 40 ),bg="#39353d",fg="white",bd=10)
title.place(x = 0, y = 0, relwidth = 1)

main_Frame=Frame(win,width=1000,height=600,bd=50)
main_Frame.config(bg="#564c61")
main_Frame.place(relx=.5,rely=.45,anchor="c")

l1 = Label(main_Frame, text='Date ',bg="#39353d",fg="white",width=8,font = ("Times New Roman", 11 ))
l1.grid(row=0,column=0)

l2 = Label(main_Frame, text='Time ',bg="#39353d",fg="white",width=8,font = ("Times New Roman", 11 ))
l2.grid(row=1,column=0)

l3 = Label(main_Frame, text='Topic of Study',bg="#39353d",fg="white",width=14,font = ("Times New Roman", 11 ))
l3.grid(row=0,column=2)

l4 = Label(main_Frame, text="How many hour's?",bg="#39353d",fg="white",width=14,font = ("Times New Roman", 11 ))
l4.grid(row=1,column=2)

l5 = Label(main_Frame, text="Note ",bg="#39353d",fg="white",width=8,font = ("Times New Roman", 11 ))
l5.grid(row=2,column=0)

l6 = Label(main_Frame, text="Today's log ",bg="#39353d",fg="white",width=14,font = ("Times New Roman", 11 ))
l6.grid(row=2,column=2)

date_text = StringVar()
today = date.today()
e1 = Entry(main_Frame, textvariable = date_text,font = ("Times New Roman", 10 ))
e1.grid(row=0, column= 1)
e1.delete(0, END)
e1.insert(0, str(today))

time_text = StringVar()
time = time.strftime("%H:%M:%S")
e2 = Entry(main_Frame, textvariable = time_text,font = ("Times New Roman", 10 ))
e2.grid(row=1, column= 1)
e2.delete(0, END)
e2.insert(0, str(time))

study_text = StringVar()
e3 = Entry(main_Frame, textvariable = study_text,font = ("Times New Roman", 10 ))
e3.grid(row=0, column= 3)

hour_text = StringVar()
e4 = Entry(main_Frame, textvariable = hour_text,font = ("Times New Roman", 10 ))
e4.grid(row=1, column= 3)

note_text = StringVar()
e5 = Entry(main_Frame, textvariable = note_text,font = ("Times New Roman", 10 ))
e5.grid(row=2, column= 1)

log_text = StringVar()
e6 = Entry(main_Frame, textvariable = log_text,font = ("Times New Roman", 10 ))
e6.grid(row=2, column=3)

b1 = Button(main_Frame,text='ADD',width=12,pady=5,command= add_command,font = ("Times New Roman", 12 ))
b1.grid(row=3,column=4)

b2 = Button(main_Frame,text='Search',width=12,pady=5,command= search_command,font = ("Times New Roman", 12 ))
b2.grid(row=4,column=4)

b3 = Button(main_Frame,text='Delete',width=12,pady=5, command= delete_command,font = ("Times New Roman", 12 ))
b3.grid(row=5,column=4)

b4 = Button(main_Frame,text='View all',width=12,pady=5, command= view_command,font = ("Times New Roman", 12 ))
b4.grid(row=6,column=4)

b5 = Button(main_Frame,text='Close',width=12,pady=5,command = win.destroy,font = ("Times New Roman", 12 ))
b5.grid(row=7,column=4)

list = Listbox(main_Frame,height=8,width=60)
list.grid(row=3,column=0,rowspan=9,columnspan=3)

sb = Scrollbar(main_Frame)
sb.grid(row=3,column=3,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

win.mainloop()
