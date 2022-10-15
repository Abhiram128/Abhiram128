import sys
from tkinter import *
top = Tk()
top.title("Tic Tac Toe")
t1 = PhotoImage(file="t1.png")
label = Label(image=t1)
label.pack()
top.geometry("1000x570")
top.resizable(False,False)
top.configure(bg='red')
tic_p = PhotoImage(file ="tic1_p.png")
t2= PhotoImage(file ="t2.png")
t3 = PhotoImage(file ="t3.png")
but1 = Button(top, text="player vs player", padx=20, pady=3, image=tic_p, command=lambda: startgame())
but3 = Button(top, text="player vs computer", padx=20, pady=3, image =t2, command=lambda: game2())
but2 = Button(top, text="Exit Game", padx=20, pady=3 ,image = t3, command=lambda: top.destroy())
but1.place(x=400, y=200)
but3.place(x=400, y=300)
but2.place(x=400, y=400)


def startgame():
    win = Toplevel(top)
    win.title = ("Tic Tac Toe")
    t1 = PhotoImage(file = "t1.png")
    label = Label(win,image = t1)
    label.pack()
    win.geometry('1000x570')
    win.resizable(False,False)
   # win.configure(bg='red')
#   img = PhotoImage(file ="tback.png")
  # label = Label(win
    li = [None] * 9
    li1 = []
    li2 = []
    global count
    count = 1

    def click(number):
        global count
        if number in li:
            print("number already entered")
        else:
            Table(number)
            li[count - 1] = number
            if count % 2 != 0:
                li1.append(number)
                listb[number - 1]['text'] = 'O'
            else:
                li2.append(number)
                listb[number - 1]['text'] = 'X'
            if count > 4 and count < 10:
                check(li1, li2)
            count += 1

    from itertools import permutations
    global count1
    count1 = 4

    def check(li1, li2):
        global count1
        count1 += 1
        list1 = []
        list2 = []
        list11 = []
        list22 = []
        l7 = [123, 213, 231, 132, 312, 321, 147, 174, 417, 471, 741, 714, 159, 195, 951, 915, 591, 519, 258, 285, 825,
              852, 582, 528, 369, 396, 639, 693, 936, 963, 357, 375, 537, 573, 735, 753, 456, 465, 546, 564, 654, 645,
              789, 897, 879, 798, 987, 978]
        c = []
        id = []
        d = []
        e = []
        for i in permutations(li1, 3):
            list1.append(i)
        for i in permutations(li2, 3):
            list2.append(i)
        for i in list1:
            a = list(i)
            list11.append(a)
        for i in list2:
            a = list(i)
            list22.append(a)
        for i in list11:
            a = ''
            for j in i:
                a = a + str(j)
            c.append(a)
        print(c)
        for i in list22:
            a = ''
            for j in i:
                a = a + str(j)
            d.append(a)
        print(d)
        for i in c:
            a = int(i)
            id.append(a)
        for i in d:
            a = int(i)
            e.append(a)
        print(id)
        print(e)
        for a in id:
            if a in l7:
                label = Label(win, text="player 1 is the winner").place(x=50, y=50)
                # win.destroy()
                # top.destroy()
                return
            else:
                pass
        for a in e:
            if a in l7:
                Label(win, text="player 2 is the winner").place(x=50, y=50)
                # win.destroy()
                # top.destroy()
                return
            else:
                pass
        print(count1)
        if count1 == 9:
            Label(win, text="the game is tied").place(x=50, y=50)
            # win.destroy()
            # top.destroy()
            return

    button9 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(9))
    button8 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(8))
    button7 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(7))
    button6 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(6))
    button5 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(5))
    button4 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(4))
    button3 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(3))
    button2 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(2))
    button1 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(1))
    listb = []
    listb.append(button1)
    listb.append(button2)
    listb.append(button3)
    listb.append(button4)
    listb.append(button5)
    listb.append(button6)
    listb.append(button7)
    listb.append(button8)
    listb.append(button9)
    button1.place(x=100, y=100)
    button2.place(x=200, y=100)
    button3.place(x=300, y=100)

    button4.place(x=100, y=200)
    button5.place(x=200, y=200)
    button6.place(x=300, y=200)

    button7.place(x=100, y=300)
    button8.place(x=200, y=300)
    button9.place(x=300, y=300)
    global num
    num = 1

    def Table(number):
        global num
        row = (number - 1) // 3
        column = (number + 2) % 3
        if num % 2 != 0:
            print("O")
        else:
            print("X")
        num += 1

    win.mainloop()


def game2():
    import random
    win = Toplevel(top)
    win.title = ("Tic Tac Toe")
    win.geometry('1000x570')
    win.resizable(False,False)
    win.configure(bg='red')
    t1 = PhotoImage(file = "t1.png")
    label = Label(win,image = t1)
    label.pack()
    li = [None] * 9
    li1 = []
    li2 = []
    global count
    count = 1
    list9 = [None] * 9

    def click(number):
        global count
        if number in li:
            print("number already entered")
         #   l = Label(win, text='number already entered').pack()
        else:
            Table(number)
            li[count - 1] = number
            if count % 2 != 0:
                li1.append(number)
                listb[number - 1]['text'] = 'O'
            else:
                li2.append(number)
                print(number)
                listb[number - 1]['text'] = 'X'
            if count > 4 and count < 10:
                check(li1, li2)
            count += 1
        if count % 2 == 0:
            move = make_move(li, li2)
            print('first')
            if not move:
                move = make_move(li, li1)
                print('second')
            if not move:
                move = random.randint(1, 9)
                print('third')
            click(move)

    from itertools import permutations
    import itertools
    global count1

    def make_move(li, moves):
        list6 = []
        win = [123, 213, 231, 132, 312, 321, 147, 174, 417, 471, 741, 714, 159, 195, 951, 915, 591, 519, 258, 285, 825,
               852, 582, 528, 369, 396, 639, 693, 936, 963, 357, 375, 537, 573, 735, 753, 456, 465, 546, 564, 654, 645,
               789, 897, 879, 798, 987, 978]
        for i in win:
            a = [int(x) for x in str(i)]
            list6.append(a)
        for a in itertools.combinations(moves, 2):
            for i in list6:
                if all(item in i for item in a):
                    move = set(i).difference(set(a)).pop()
                    if move not in li:
                        return move
        return None

    count1 = 4

    def check(li1, li2):
        global count1
        count1 += 1
        list1 = []
        list2 = []
        list11 = []
        list22 = []
        l7 = [123, 213, 231, 132, 312, 321, 147, 174, 417, 471, 741, 714, 159, 195, 951, 915, 591, 519, 258, 285, 825,
              852, 582, 528, 369, 396, 639, 693, 936, 963, 357, 375, 537, 573, 735, 753, 456, 465, 546, 564, 654, 645,
              789, 897, 879, 798, 987, 978]
        c = []
        id = []
        d = []
        e = []
        for i in permutations(li1, 3):
            list1.append(i)
        for i in permutations(li2, 3):
            list2.append(i)
        for i in list1:
            a = list(i)
            list11.append(a)
        for i in list2:
            a = list(i)
            list22.append(a)
        for i in list11:
            a = ''
            for j in i:
                a = a + str(j)
            c.append(a)
        print(c)
        for i in list22:
            a = ''
            for j in i:
                a = a + str(j)
            d.append(a)
        print(d)
        for i in c:
            a = int(i)
            id.append(a)
        for i in d:
            a = int(i)
            e.append(a)
        print(id)
        print(e)
        for a in id:
            if a in l7:
                label = Label(win, text="player 1 is the winner").place(x=50, y=50)
                # win.destroy()
                # top.destroy()
                return
            else:
                pass
        for a in e:
            if a in l7:
                Label(win, text="Computer is the winner").place(x=50, y=50)
                # win.destroy()
                # top.destroy()
                return
            else:
                pass
        print(count1)
        if count1 == 9:
            Label(win, text="the game is tied").place(x=50, y=50)
            # win.destroy()
            # top.destroy()
            return

    button9 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(9))
    button8 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(8))
    button7 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(7))
    button6 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(6))
    button5 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(5))
    button4 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(4))
    button3 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(3))
    button2 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(2))
    button1 = Button(win, text="", padx=40, pady=20, bg='pink', command=lambda: click(1))
    listb = []
    listb.append(button1)
    listb.append(button2)
    listb.append(button3)
    listb.append(button4)
    listb.append(button5)
    listb.append(button6)
    listb.append(button7)
    listb.append(button8)
    listb.append(button9)
    button1.place(x=100, y=100)
    button2.place(x=200, y=100)
    button3.place(x=300, y=100)

    button4.place(x=100, y=200)
    button5.place(x=200, y=200)
    button6.place(x=300, y=200)

    button7.place(x=100, y=300)
    button8.place(x=200, y=300)
    button9.place(x=300, y=300)
    global num
    num = 1

    def Table(number):
        global num
        row = (number - 1) // 3
        column = (number + 2) % 3
        if num % 2 != 0:
            print("O")
        else:
            print("X")
        num += 1

    win.mainloop()


top.mainloop()
