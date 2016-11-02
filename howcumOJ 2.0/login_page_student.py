__author__ = 'howcum'
from tkinter import *
import sqlite3
import student_home
from tkinter import messagebox
cnt=0

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Login!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.bck)
        self.homeBtn.pack(side="left",padx=20)

        self.bckButton=Button(self.Frame1,text="Profile")
        self.bckButton.pack(side="right",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Sign Up!",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame2=LabelFrame(master,bg="light blue")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.username = Label(self.Frame2,text="ROLL",bg='cyan',font=("Helvetica",16))
        self.entusername=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.username.pack()
        # username.place(x=200,y=200)
        self.entusername.pack()

        self.password = Label(self.Frame2,text="Password",bg='cyan',font=("Helvetica",16))
        self.entpassword=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.password.pack()
        self.entpassword.pack()

        self.login_btn = Button(self.Frame2,command=self.submit,text="Login")
        self.login_btn.pack()


    def submit(self):
        print("clicked!!")
        uname_=str(self.entusername.get())

        pass_=str(self.entpassword.get())
        self.conn=sqlite3.connect('mydatabase.db')
        try:
            self.c=self.conn.cursor()
            self.c.execute("SELECT * from Student WHERE username = ? AND password= ?",(uname_,pass_));
            id_exists=self.c.fetchone()
            if id_exists:
                print("welcome!!")
                self.master.destroy()
                student_home.call(uname_,str(id_exists[2]))
            else:
                messagebox.showinfo("message box","ID or Password incorrect!!")

        except sqlite3.IntegrityError:
            print('ERROR: login error')

        self.conn.commit()
        self.conn.close()
        pass

    def bck(self):
        self.master.destroy()
        pass


def func():
    root=Tk()
    root.geometry("1000x500")

    app=Application(master=root)
    app.mainloop()


if __name__ == '__main__':

    func()
else:
    print("login")
