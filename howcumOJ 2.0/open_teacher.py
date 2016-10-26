__author__ = 'howcum'

from tkinter import *
import login_page
import signup_page

root = Tk()

def login():
    root.destroy()
    login_page.cnt=login_page.cnt+1;
    login_page.func()

def signup():
    root.destroy()
    signup_page.cnt=signup_page.cnt+1;
    signup_page.func1()

root.geometry("1000x500")
bckgnd=PhotoImage(file="1.png")
bglabel = Label(root,image=bckgnd)
bglabel.place(x=0, y=0, relwidth=1, relheight=1)
Frame3 = Frame(root,bg="black")
Frame3.place(x=550,y=180)
inst= Label(Frame3,text="Welcome To AUTOMATED CODE JUDGE!!\n\n...Login/SignUp to Continue...",bg='gray',font=("Helvetica",16))
inst.pack()
logImg=PhotoImage(file="login.png")
login_btn = Button(Frame3,image=logImg,bg="black",command=login)
login_btn.pack()

signIMG=PhotoImage(file="sign.png")
signup_btn = Button(Frame3,image=signIMG,bg="black",command=signup)
signup_btn.pack()

root.mainloop()