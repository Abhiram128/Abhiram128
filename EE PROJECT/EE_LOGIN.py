# Program to check membership
import sys
from tkinter import *
from tkinter import messagebox
import menu
#import PIL
from tkinter.font import Font
def login():
    userid = e1.get()
    password = e2.get()
    if (userid == "" and password == ""):
        messagebox.showerror("Error", "Blank not allowed")
    elif userid == "":
        messagebox.showerror("Error", "Please enter userid")
    elif password == "":
        messagebox.showerror("Error", "Please enter Password")
    else:
        obj1 = LoginId(userid, password)
        k = l1.Check(obj1)
        if k == False:
            print("false")
            messagebox.showerror("Error", "Invalid Details")
        else:
            messagebox.showinfo("Success", "Logged in")
            Login.destroy()
            a=False
            k=menu.menu1(k)
            if k==-1:
                n=3
class LoginId:
    def __init__(self, Id, password, name="None"):
        self.id = Id
        self.password = password
        self.name = name
        self.next = None

    def nodecmp(self, obj):
        if self.id == obj.id and self.password == obj.password:
            return True
        else:
            return False
class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, obj):
        if self.head == None:
            self.head = obj
            self.length += 1
        else:
            cn = self.head
            while cn.next != None:
                cn = cn.next
            cn.next = obj
            self.length += 1

    def printlist(self):
        cn = self.head
        while cn != None:
            print(cn.id, cn.password)
            cn = cn.next

    def Check(self, obj):
        cn = self.head
        while cn != None:
            if obj.nodecmp(cn):
                return cn
            else:
                cn = cn.next
        return False

    def compare(self, i):
        cn = self.head
        while cn != None:
            if cn.id == i:
                return True
            cn = cn.next
        return False
def register():
    name = r1.get()
    userid = r2.get()
    password = r3.get()
    if (userid == "" and password == "" and name == ""):
        messagebox.showerror("Error", "Blank not allowed")
    elif userid == "":
        messagebox.showerror("Error", "Please enter userid")
    elif password == "":
        messagebox.showerror("Error", "Please enter Password")
    elif name == "":
        messagebox.showerror("Error", "Please enter Name")
    else:
        r = l1.compare(userid)
        if r == True:
            messagebox.showerror("Error", "Id already exists")
        else:
            obj1 = LoginId(userid, password, name)
            l1.push(obj1)
            messagebox.showinfo("Success", "REGISTERED")
            L.destroy()
l1 = List()
a = 0
k = []
s = []
p = []
n = []
f = open("data1.txt", "a")
f.close()
f = open("data1.txt", "r")
for i in f:
    k.append(i)
k = "".join(k)
k = k.split()
for i in k:
    if a == 0:
        I = i
        a = 1
    elif a == 1:
        P = i
        a = 2
    elif a == 2:
        N = i
        a = 0
        obj = LoginId(I, P, N)
        l1.push(obj)
f.close()
a=  True
while (a==True):
  #  n = int(input("\nEnter 1 to register and 2 to login and 3 to exit"))
    n=1
    if n == 1:
        L = Tk()
        L.title("LOGIN PAGE")
        L.geometry("450x280")
        L.resizable(False,False)
        #customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        #customtkinter.set_default_color_theme("blue")
        img = PhotoImage(file="2.png")
        label=Label(L,image= img)
        label.pack()
        #label = Label(L,image = img)
        #label.pack(fill="both",expand=True)
        #canvas=Canvas(L,width=450,height=310)
        #canvas.pack(fill="both", expand=True)
        #canvas.create_text(200,15,text="MENU DRIVEN LOGIN PAGE",font=("Helvetica 15 bold"),fill= "white")
        Label(L, text="MENU DRIVEN LOGIN PAGE", font=("Manga bey", "20"),relief ="flat",bg= "#323234", fg="white").place(x=50,y=15)
        Label(L, text="REGISTER", font="Helvetica 10 bold", bg="#323234", fg="White").place(x=150, y=70)
        Label(L, text="NAME", font="Serif 8 bold", bg="#323234", fg="White").place(x=110, y=100)
        Label(L, text="USER ID", font="Serif 8 bold ", bg="#323234", fg="White").place(x=110, y=150)
        Label(L, text="PASSWORD", font="Serif 8 bold", bg="#323234", fg="White").place(x=110, y=200)
       # canvas.create_text(0, 15, text="MENU DRIVEN LOGIN PAGE", font=("Helvetica 15 bold"), fill="white")
        #canvas.create_text(150, 50, text="REGISTER", font=("Helvetica 12 bold"), fill="white")
        ##canvas.create_text(120, 110, text="NAME", font=("Helvetica 8 bold"), fill="white")
        ##canvas.create_text(120, 160, text="USERID", font=("Helvetica 8 bold"), fill="white")
        #canvas.create_text(120, 210, text="PASSWORD", font=("Helvetica 8 bold"), fill="white")
        r1 = Entry(L, bd="2", )
        r1.place(x=180, y=100)
        r2 = Entry(L, bd="2")
        r2.place(x=180, y=150)
        r3 = Entry(L, bd="2", show="*")
        r3.place(x=180, y=200)
        Button(L, text="REGISTER", bg='black', fg="White", command=register).place(x=185, y=245)
        mainloop()
        n+=1

    if n == 2:
        Login = Tk()
        Login.title("LOGIN PAGE")
        Login.geometry("450x280")
        Login.resizable(False, False)
        img1 = PhotoImage(file="R.png")
        label = Label(Login, image=img1)
        label.pack()
        Label(Login, text="MENU DRIVEN LOGIN PAGE", font="Serif 20 bold", bg="#1a1a1a", fg="white").place(x=50,y=15)
        Label(Login, text="USER ID", font="Serif 8 bold", bg="#1a1a1a", fg="White").place(x=110, y=150)
        Label(Login, text="PASSWORD", font="Serif 8 bold", bg="#1a1a1a", fg="White").place(x=110, y=200)
        e1 = Entry(Login, bd="0", )
        e1.place(x=180, y=150)
        e2 = Entry(Login, bd="0", show="*")
        e2.place(x=180, y=200)
        Button(Login, text="LOGIN", bg='black', fg="White", command=login).place(x=185, y=250)
        mainloop()
        a = False
    # i=input("Enter your id ")
    # p = input("Enter your password")
    # obj1 = LoginId(i,p)
    # k=l1.Check(obj1)
    ##   print("INCORRECT DETAILS PLEASE TRY AGAIN")
    # else:
    #   print("Logged In")
    #  menu.menu1(k)
    # break
    # games(obj1)

    elif n == 3:
        break
    else:
        print("Enter a valid input")
f = open("data1.txt", "a")
cn = l1.head
while cn != None:
    f.write(cn.id)
    f.write(" ")
    f.write(cn.password)
    f.write(" ")
    f.write(cn.name)
    f.write(" ")
    cn = cn.next
f.close()