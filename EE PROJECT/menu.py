#Menu module
import randomgame
import menugui
def menu1(obj1):
    s="0"
    p=0
    k=""
    f=open("score.txt","a")
    f.close()
    f = open("score.txt","r")
    for k in f:
        pass
    if k!="":
        for i in k:
            if i==" ":
                break
            else:
                s=s+i
    f.close()        
    s=int(s)

    while 1:
        c = menugui.menug()
        if c==1:
            p=randomgame.randomgame1()
            if p<=s:
                f=open("score.txt","r")
                for i in f:
                    print(i,end="")
                f.close()
                continue
            p=str(p)
            f=open("score.txt","w")
            f.write(p)
            f.write(" is the Highest Score secured by ")
            f.write(obj1.name)
            f.close()
            f=open("score.txt","r")
            for i in f:
                print(i,end="")
            f.close()
        if c==2:
            from s_game import snake_game
            snake_game()

        if c==3:
            import tic
        if c==-1:
            return
        if c==4:
            import jumb
        else:
            print("Please enter a valid input")