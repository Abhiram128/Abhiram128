from tkinter import *
global n
n=0
global m
m=0
global m1
m1=0
def fun():
    global n
    n = en.get()
    I.destroy()
def fun1():
    global m
    m = en1.get()
    H.destroy()
def fun2():
    global m1
    m1 = en2.get()
    M.destroy()


def easy(s,j=None):
    global I
    I = Tk()
    global en
    en=0
    I.title("Easy level")
    I.configure(bg="#FDF5DF")
    I.geometry('1100x1000')
    I.resizable(False, False)
    img = PhotoImage(file="1.png")
    label = Label(I, image=img)
    label.place(x=0, y=0)
    if s==-1:
        Label(I, text="You Lose!!", font="Times 20", bg="black", fg="white").place(x=360, y=450)
        mainloop()
        return
    if int(n)==s:
        if j==0:
            Label(I, text="***You get 5 points as you guessed it in the first time***", font="Times 20", bg="black", fg="white").place(x=360, y=450)
            mainloop()
            return
        if j==1:
            Label(I, text="***You get 3 points as you guessed it in the second time***", font="Times 20", bg="black",
                  fg="white").place(x=360, y=450)
            mainloop()
            return
        if j==2:
            Label(I, text="***You get 2 points as you guessed it in the third time***", font="Times 20", bg="black",
                  fg="white").place(x=360, y=450)
            mainloop()
            return

    en = Entry(I, bd="2")
    en.place(x=350, y=370)
    Button(I, text="SUBMIT", fg="Black", bd="8", command=fun, padx=14, pady=3).place(x=400, y=550)
   # if int(n)==s:
    #    Label(I, text="You have guessed it correctly!!", font="Times 20", bg="black", fg="white").place(x=360, y=450)
    if int(n)>s :
        Label(I, text="Enter a lower value", font="Times 20", bg="black", fg="white").place(x=360, y=450)
    if int(n)<s and n!= 0:
        Label(I, text="Enter a higher value", font="Times 20", bg="black", fg="white").place(x=360, y=450)
    mainloop()
    return n
def hard(s,j,h):
    global H
    H = Tk()
    global en1
    en1=0
    H.title("Hard level")
    H.configure(bg="#FDF5DF")
    H.geometry('1100x1000')
    H.resizable(False, False)
    img = PhotoImage(file="1M.png")
    label = Label(H, image=img)
    label.place(x=0, y=0)
    if s==-1:
        Label(H, text="You Lose!!", font="Times 20", bg="black", fg="white").place(x=360, y=450)
        mainloop()
        return
    if int(m1)==s:
        if j==0:
            Label(H, text="***You get 50 points as you guessed it in the first time***", font="Times 15", bg="black", fg="white").place(x=360, y=420)
            mainloop()
            H.destroy()
            return
        if j==1:
            Label(H, text="***You get 30 points as you guessed it in the second time***", font="Times 15", bg="black",
                  fg="white").place(x=360, y=420)
            mainloop()
            H.destroy()
            return
        if j==2:
            Label(H, text="***You get 20 points as you guessed it in the third time***", font="Times 15", bg="black",
                  fg="white").place(x=360, y=420)
            mainloop()
            H.destroy()
            return
    en1 = Entry(H, bd="2")
    en1.place(x=350, y=370)
    Button(H, text="SUBMIT", fg="Black", bd="8", command=fun1, padx=14, pady=3).place(x=400, y=500)
    if int(m)>s :
        Label(H, text="Enter a lower value", font="Times 15", bg="black", fg="white").place(x=360, y=430)
        if j==1:
            Label(H,text="Hint Hundreds place of: "+h,font="Times 15",bg="black",fg="White").place(x=360,y=470)
        if j==2:
            Label(H,text="Hint Tens place of: "+h,font="Times 15",bg="black",fg="White").place(x=360,y=470)
    if int(m)<s and m!= 0:
        Label(H, text="Enter a higher value", font="Times 10", bg="black", fg="white").place(x=350, y=430)
        if j==1:
            Label(H,text="Hint Hundreds place of: "+h,font="Times 10",bg="black",fg="White").place(x=360,y=470)
        if j==2:
            Label(H,text="HINT : For tens place"+h,font="Times 10",bg="black",fg="White").place(x=350,y=470)
    mainloop()
    return m
def medium(s,j,h):
    global M
    M = Tk()
    global en2
    en2=0
    M.title("Medium level")
    M.configure(bg="#FDF5DF")
    M.geometry('1100x1000')
    M.resizable(False, False)
    img = PhotoImage(file="2M.png")
    label = Label(M, image=img)
    label.place(x=0, y=0)
    if s==-1:
        Label(M, text="You Lose!!", font="Times 20", bg="black", fg="white").place(x=360, y=450)
        mainloop()
        return
    if int(m1)==s:
        if j==0:
            Label(M, text="***You get 10 points as you guessed it in the first time***", font="Times 15", bg="black", fg="white").place(x=360, y=420)
            mainloop()
            M.destroy()
            return
        if j==1:
            Label(M, text="***You get 6 points as you guessed it in the second time***", font="Times 15", bg="black",
                  fg="white").place(x=360, y=420)
            mainloop()
            M.destroy()
            return
        if j==2:
            Label(M, text="***You get 4 points as you guessed it in the third time***", font="Times 15", bg="black",
                  fg="white").place(x=360, y=420)
            mainloop()
            M.destroy()
            return
    en2 = Entry(M, bd="2")
    en2.place(x=350, y=400)
    
    Button(M, text="SUBMIT", fg="Black", bd="8", command=fun2, padx=14, pady=3).place(x=450, y=500)
    if int(m1)>s :
        Label(M, text="Enter a lower value", font="Times 15", bg="black", fg="white").place(x=360, y=430)
        if j==2:
            Label(M,text="Hint Tens place of: "+h,font="Times 15",bg="black",fg="White").place(x=360,y=470)
    if int(m1)<s and m1!= 0:
        Label(M, text="Enter a higher value", font="Times 10", bg="black", fg="white").place(x=350, y=430)
        if j==2:
            Label(M,text="HINT : For tens place"+h,font="Times 10",bg="black",fg="White").place(x=350,y=470)
            
    mainloop()
    return m1
