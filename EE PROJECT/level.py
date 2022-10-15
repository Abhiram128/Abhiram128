from tkinter import *
global b
b=0
def easy():
    global b
    b=1
    L.destroy()
def hard():
    global b
    b=3
    L.destroy()
def medium():
    global b
    b=2
    L.destroy()
def quit():
    global b
    b=0
    L.destroy()


def levels():
    global L
    L= Tk()
    L.title("Snake Game")
    L.geometry("2000x2000")
    img=PhotoImage(file="lbg.png")
    label = Label(L, image=img)
    label.pack()
    s1 = PhotoImage(file ="s1.png")
    s2 = PhotoImage(file="s2.png")
    s3= PhotoImage(file="s3.png")
    s4 = PhotoImage(file="s4.png")
    Button(L, text="EASY", image =s1, bd="8", command=easy, padx=20, pady=3).place(x=550, y=300)
    Button(L, text="MEDIUM", image =s2, bd="8", command=medium, padx=14, pady=3).place(x=550, y=370)
    Button(L, text="HARD", image =s3, bd="8", command=hard, padx=20, pady=3).place(x=550, y=440)
    Button(L, text="QUIT", image =s4, bd="8", command=quit, padx=20, pady=3).place(x=550, y=510)
    mainloop()
    if b==1:
        return 0.25
    if b==2:
        return 0.15
    if b==3:
        return 0.05
    if b==0:
        return -1