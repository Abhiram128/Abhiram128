#random number
import HINT
import random
import tkinter
from tkinter import *
from tkinter import messagebox
import input
import guir
def ten(n):
    if n//100 !=0:
        n=n//10
        return n%10
    else:
        return n//10
def hundred(n):
    return n//100
def randomgame1():
    points=0
    while 1:
        i=guir.gui()

        #i = int(input("Enter the difficulty 1 for easy(1 to 100)\n2 for medium(1 to 100)\n3 for hard(1 to 1000)\nEnter -1 to stop\n"))
        if i==1:
            print("Level EASY")
            k=random.randint(1,10)
            for j in range(3):
                flag=1
                n=0
                n = input.easy(k)
                n=int(n)
                if n==k:
                    s = 1
                    flag=2
                    input.easy(k,j)
                    break
                elif n>k and j!=2:
                    s = 1
                elif n<k and j!=2:
                    s = 3
            if j==0:

                print("***You get 5 points as you guessed it in the first time***\n")
                points+=5
            elif j==1:
                print("***You get 3 points as you guessed it in the second time***\n")
                points+=3
            elif j==2 and flag==2:
                print("***You get 2 points as you guessed it in third time***\n")
                points+=2
            else:
                input.easy(-1)
                break
                print("***You get no points as you didnt guess the number in the required number of chances***\n")
        elif i==2:
            print("Level Medium")
            k=random.randint(1,100)
            for j in range(3):
                z=0
                h=""
                flag =2
                if j==2:
                    z=ten(k)
                    print("HINT : For Tens place of the number:")
                    h=HINT.hint(z)

                n = int(input.medium(k,j,h))
                if n==k:
                    print("You have guessed it correctly\n")
                    flag=1
                    input.medium(k,j,h)
                elif n>k and j!=2:
                    print("Enter a lower value\n")
                elif n<k and j!=2:

                    print("Enter a higher value\n")
            if j==0:
                print("You get 10 points as you guessed it in the first time\n")
                points+=10
            elif j==1:
                print("You get 6 points as you guessed it in the second time\n")
                points+=6
            elif j==2 and flag==1:
                input.medium(k,j,h)
                print("You get 4 points as you guessed it in third time\n")
                points+=4
            else:
                input.medium(-1,j,h)
                print(k)
                print("You get no points as you didnt guess the number in the required number of chances\n")
        elif i==3:
            print("Level Hard")
            k=random.randint(1,1000)
            for j in range(3):
                h=""
                flag=2
                if j==2:
                    z = ten(k)
                    print("HINT : For tens place of the number:")
                    h=HINT.hint(z)
                if j==1:
                    z=hundred(k)
                    print("HINT : For Hundreds place of the number:")
                    h=HINT.hint(z)
                n = input.hard(k,j,h)
                n = int(n)
                if n==k:
                    print("You have guessed it correctly\n")
                    flag=1
                    break
                elif n>k and j!=2:
                    print("Enter a lower value")
                elif n<k and j!=2:
                    print("Enter a higher value")
            if j==0:
                print("***You get 50 points as you guessed it in the first time***\n")
                input.hard(k,j,h)
                points+=50
            elif j==1:
                input.hard(k,j,h)
                print("***You get 30 points as you guessed it in the second time***\n")
                points+=30
            elif j==2 and flag==1:
                input.hard(k,j,h)
                print("***You get 20 points as you gussed it in third time***\n")
                points+=20
            else:
                input.hard(-1,j,h)
                print("You get no points as you didnt guess the number in the required number of chances\n")
                print("ANSWER : ",k)

        elif i == -1:
            print("The total points scored are : ",points)
            return points
            break
        else:
            print("Enter a valid input\n")
    return 0
