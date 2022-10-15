from tkinter import *
from tkinter import messagebox
b=0
def easy():
    global b
    b=1
    R.destroy()
def hard():
    global b
    b=3
    R.destroy()
def medium():
    global b
    b=2
    R.destroy()
def quit():
    global b
    b=0
    R.destroy()
def gui():
    global R
    R= Tk()
    R.title("GUESS ME!!")
    R.configure(bg="#FDF5DF")
    R.geometry('1100x1000')
    R.resizable(False,False)
    img = PhotoImage(file="12.png")
    label=Label(R,image=img)
    label.place(x=0,y=0)
    Button(R,text="EASY",fg="Black",bd= "8",command=easy,padx=20,pady=3).place(x=400,y=380)
    Button(R,text="MEDIUM",fg="Black",bd = "8",command=medium,padx=14,pady=3).place(x=400,y=450)
    Button(R,text="HARD",fg="Black",bd="8",command=hard,padx=20,pady=3).place(x=400,y=520)
    Button(R,text="QUIT",fg="Black",bd="8",command=quit,padx=20,pady=3).place(x=400,y=590)
    mainloop()
    if b == 1:
        return 1
    if b == 2:
        return 2
    if b == 3:
        return 3
    if b==0:
        return -1
    #text=Text(R,height=10,width=53)
    #text.place(x=30,y=50)
    #Label(R,text="GUESS ME!!",font="Helvetica 30 bold",bg="#FDF5DF",fg="#5EBEC4").place(x=50,y=10)
    #utton(L, text="REGISTER", bg='black', fg="White", command=register).place(x=185, y=245)
