__author__ = 'howcum'
from tkinter import *
import sqlite3
import login_page_student
from tkinter import messagebox


class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Sign Up now!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

        self.bckButton=Button(self.Frame1,text="Profile")
        self.bckButton.pack(side="right",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Sign Up!",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame2=LabelFrame(master,bg="light blue")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.rname = Label(self.Frame2,text="Name",bg='cyan',font=("Helvetica",16))

        self.entrname=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.rname.pack()
        # username.place(x=200,y=200)
        self.entrname.pack()

        self.username = Label(self.Frame2,text="Username",bg='cyan',font=("Helvetica",16))
        self.entusername=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.username.pack()
        # username.place(x=200,y=200)
        self.entusername.pack()

        self.password = Label(self.Frame2,text="Password",bg='cyan',font=("Helvetica",16))
        self.entpassword=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.password.pack()
        self.entpassword.pack()

        self.roll = Label(self.Frame2,text="Roll Number",bg='cyan',font=("Helvetica",16))
        self.rollText=Entry(self.Frame2,bg='white',font=("Helvetica",16))
        self.roll.pack()
        self.rollText.pack()

        self.login_btn = Button(self.Frame2,command=self.submit,text="Signup")
        self.login_btn.pack(pady=20)

        # self.back = Button(master,command=self.bck,text="back")
        # self.back.grid()

    def homeFunction(self):
        self.master.destroy()
        login_page_student.func()
        pass

    def submit(self):
        print("clicked!!")
        uname_=str(self.entusername.get())
        name_=str(self.entrname.get())
        pass_=str(self.entpassword.get())
        roll_=str(self.rollText.get())
        self.conn=sqlite3.connect('mydatabase.db')
        try:
            self.conn.execute("INSERT INTO Student (username, password, Name,roll) \
            VALUES (?,?,?,?)",(uname_,pass_,name_,roll_));

        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(uname_))
            messagebox.showinfo("message box","ID already exists!!")

        self.conn.commit()
        self.conn.close()
        pass


def func():
    root=Tk()
    root.geometry("1000x500")

    app=Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    print("hello")
    func()
else:
    print("signup")
    # root=Tk()
    # root.geometry("1000x500")
    # root.mainloop()
