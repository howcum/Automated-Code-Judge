__author__ = 'howcum'

from tkinter import *
from functools import partial
import student_home
import sqlite3
import create_session

Student_roll=NONE

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("join New Course!!")

        self.stepZero=LabelFrame(master,text="AUTOMATED CODE JUDGE!!")
        self.stepZero.grid(row=0, columnspan=7, sticky='WE', \
                     padx=5, pady=5, ipadx=5, ipady=5)

        self.homeBtn=Button(self.stepZero,text="home",command=self.homeFunction)
        self.homeBtn.grid(row=0,columnspan=7,sticky='WE')

        self.stepOne = LabelFrame(master, text=" List of Student solved problem: ")
        self.stepOne.grid(row=1, columnspan=7, sticky='W', \
                     padx=5, pady=5, ipadx=5, ipady=5)

        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor();
        #self.c.execute('SELECT * from Problems where session_id=?',(create_session.now_run_korche,))

        self.c.execute('SELECT * from Problems where session_id=30220162')
        self.allrows=self.c.fetchall()

        # for row in self.allrows:
        #
        #
        # print('1): ',self.allrows)
        i=0
        for i in range(5):
            #print(row)
            row=self.c.fetchone()
            #self.q=i
            self.stepOne.buttonIn = Label(self.stepOne, text = "Problem "+str(i))
            self.stepOne.buttonIn.grid(row=6, column=0+i, sticky=W+E)
            self.stepOne.buttonOut = Button(self.stepOne, text =str(row[i+3]))
            self.stepOne.buttonOut.grid(row=6, column=0+i, sticky=W+E)
            #self.i=self.i +1
            i=i+1

    def homeFunction(self):
        print("back a ja ga")
        self.master.destroy()
        student_home.call("hello")
        pass

    # def joinIt(self,p,q):
    #     pp=str(p)
    #     print("join koro"+str(p))
    #     qq=str(q)+str(Student_roll)
    #     #print(qq,p)
    #     self.c.execute('SELECT joined_student from Course WHERE course_id = ?',(p,))
    #     # #self.c.execute("SELECT * from Teacher WHERE username = ? AND password= ?",(uname_,pass_));
    #     self.now=self.c.fetchone()
    #     self.updated_joind_student=str(self.now)+','+str(Student_roll)
    #     # print(self.now)
    #     self.c.execute('UPDATE Course SET joined_student=? where course_id=?',(self.updated_joind_student,p))
    #     self.conn.commit()
    #     self.conn.close()
    #     pass


def call():
    #print(u)
    #global Student_roll
    #Student_roll = u
    root=Tk()
    root.configure(background="black")
    root.geometry("1000x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call()
else:
    print("baje")