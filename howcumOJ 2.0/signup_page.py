__author__ = 'howcum'
from tkinter import *
import sqlite3
import login_page
from tkinter import messagebox
import teacher_home

cnt=0
role=0

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Sign Up now!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.bck)
        self.homeBtn.pack(side="left",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Sign Up!",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame2=LabelFrame(master,bg="light blue")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.rname = Label(self.Frame2,text="Name",bg='cyan',font=("Helvetica",16))

        self.entrname=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.rname.pack()
        self.entrname.pack()

        self.username = Label(self.Frame2,text="Username",bg='cyan',font=("Helvetica",16))
        self.entusername=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.username.pack()
        self.entusername.pack()

        self.password = Label(self.Frame2,text="Password",bg='cyan',font=("Helvetica",16))
        self.entpassword=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.password.pack()
        self.entpassword.pack()

        self.login_btn = Button(self.Frame2,command=self.submit,text="Signup")
        self.login_btn.pack(pady=20)

    def submit(self):
        print("clicked!!")
        print(role)
        uname_=str(self.entusername.get())
        name_=str(self.entrname.get())
        pass_=str(self.entpassword.get())
        self.conn=sqlite3.connect('mydatabase.db')
        try:
            self.conn.execute("INSERT INTO Teacher (username, password, Name) \
            VALUES (?,?,?)",(uname_,pass_,name_))

        except sqlite3.IntegrityError:
            self.master.withdraw()
            msg=messagebox.showinfo("message box","Username already exists!!")
            print('ERROR: ID already exists in PRIMARY KEY column {}')

        self.conn.commit()
        self.conn.close()
        teacher_home.call(uname_)
        pass

    def bck(self):
        self.master.destroy()
        login_page.func()
        pass


def func1():
    root=Tk()
    root.geometry("1000x500")

    app=Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    func1()
else:
    print("ki j bolona")
