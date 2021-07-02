from tkinter import *
import random

root = Tk()
root.configure(width="70m", height = "100m")

def get_number():
    global Lb1
    getnumber = []
    while(len(getnumber) != 6):
        number = random.randint(1, 45)
        if number not in getnumber:
            getnumber.append(number)
    getnumber.sort()
    Lb1 = Label(root, text=getnumber)
    Lb1.place(x = 50, y = 110, width = 150, height = 60)
    
def initialize():
    global Lb1
    Lb1.destroy()
    Lb1 = Label(root, text="")
    Lb1.place(x = 50, y = 110, width = 150, height = 60)

def maker():
    Lb2 = Label(root, text="제작자 : 채종훈")
    Lb2.place(x = 50, y = 250, width = 150, height = 60)

Button(root, text = "추첨", command=get_number).place(
    x = 10, y = 60, width = 110, height = 30)

Button(root, text = "초기화", command=initialize).place(
    x = 130, y = 60, width = 110, height = 30)

Button(root, text = "제작자", command=maker).place(
    x = 80, y = 200, width = 100, height = 30)

Lb1 = Label(root)

root.mainloop()