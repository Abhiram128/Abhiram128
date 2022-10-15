import random
from tkinter import *
top=Tk()
jimg = PhotoImage(file = "jimg.png")
label = Label(image=jimg)
A=['manchester','environment','migration','institute','technology','management','colony','mobile','penguin','sweden','sentence']
time=150
score=0
jq = PhotoImage(file ="JQ.png")
#but1 = Button(top, text="QUIT", padx=20, pady=3, comand =top.destroy(),image=jq)
#but1.place(x=300,y=300)
def start_Game(event):
    if time==150:
        time_left()
    wordgenerator()
def wordgenerator():
    global time
    global score
    if time>0:
        e.focus_set()
        for i in A:
            if e.get().lower()==i:
                score+=1
        e.delete(0,END)
        b=random.choice(A)
        k=''.join(random.sample(b,len(b)))
        label.config(text=k)
        scorelabel.config(text='score: '+str(score))
def time_left():
    global time
    if time>0:
        time-=1
        timeLabel.config(text='Time Left: '+str(time))
        timeLabel.after(1000,time_left)
top.geometry('600x400')
top.resizable(False,False)
top.title('Jumbled Words')
label.pack()
#instructions=Label(top,text='Guess the correct sequence of word')
#instructions.place(x=150,y=100)
scorelabel=Label(top,text='Press enter to start')
scorelabel.place(x=150,y=150)
label=Label(top)
label.place(x=150,y=200)
timeLabel=Label(text='Time Left: '+str(time))
timeLabel.place(x=150,y=250)
e=Entry(top)
top.bind('<Return>',start_Game)
e.place(x=150,y=300)
e.focus_set()
top.mainloop()
