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
def jumb():
    global b
    b=4
    L.destroy()
def quit():
    global b
    b=0
    L.destroy()

def menug():
    global L
    L= Tk()
    L.title("MENU")
    L.geometry("500x600")
    L.resizable(False, False)
    img=PhotoImage(file="OIP.png")
    label = Label(L, image=img)
    label.pack()
    img1 = PhotoImage(file ="IMG1.png")
    img3 = PhotoImage(file = "IMG3.png")
    img4 = PhotoImage(file="img4.png")
 #   img1 = img1.subsample(3,3)
    img2 = PhotoImage(file = "img2.png")
#    img2 = img2.subsample(3, 3)

    Button(L, text="RANDOM NUMBER", image = img1, bd="0", command=easy, padx=20, pady=3).place(x=150, y=200)
    Button(L, text="SNAKE GAME", image = img2, bd="0", command=medium, padx=14, pady=3).place(x=150, y=270)
    Button(L, text="TIC-TAC-TOE",image =img3, bd="0", command=hard, padx=20, pady=3).place(x=150, y=340)
    Button(L, text="JUMBLED WORDS", image=img4, bd="0", command=jumb, padx=20, pady=3).place(x=150, y=410)
    Button(L, text="QUIT", fg="Black", bd="8", command=quit, padx=20, pady=3).place(x=150, y=510)
    mainloop()
    if b==1:
        return 1
    if b==2:
        return 2
    if b==3:
        return 3
    if b==4:
        return 4
    else:
        return -1
