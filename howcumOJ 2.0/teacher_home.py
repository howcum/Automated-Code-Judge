__author__ = 'howcum'
from tkinter import *
import create_new_course_teacher
import create_session
from functools import partial
import sqlite3


teachers_name=NONE
class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Teacher Home!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+teachers_name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame4=Frame(master,bg="light blue")
        self.Frame4.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.course_create= Button(self.Frame4,text="Create New Course",font=15,command=self.new_course_create)
        self.course_create.pack(side="left",padx=20)

        self.session_create= Button(self.Frame4,text="Create New Session",font=15,command=self.new_session_create)
        self.session_create.pack(side="left",padx=20)

        self.Frame3=LabelFrame(master,bg="#8b9dc3",text="List of ALL Course")
        self.Frame3.pack(side="left",expand=FALSE,pady=10,fill="y",padx=30)

        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor();
        self.c.execute('SELECT * from Course')
        self.allrows=self.c.fetchall()
        i=0
        for row in self.allrows:
            #self.q=i
            self.Frame3.buttonIn = Button(self.Frame3, text = "Course "+str(row[1]))
            self.Frame3.buttonIn.grid(row=6+i, column=0, sticky=W+E,padx=20,pady=10)
            # self.Frame3.buttonOut = Button(self.Frame3, text = "See Progress Upto Now".format(i),command=partial(self.joinIt,row[0],row[2],i))
            # self.Frame3.buttonOut.grid(row=6+i, column=1, sticky=W+E,padx=20,pady=10)
            #self.i=self.i +1
            i=i+1
        self.conn.commit()
        self.conn.close()

    def joinIt(self,p,q,btn):
        pp=str(p)
        #qq=str(q)+str(Student_roll)
        #print(qq,p)
        # self.conn=sqlite3.connect('mydatabase.db')
        # self.c=self.conn.cursor();
        # self.c.execute('SELECT joined_student from Course WHERE course_id = ?',(p,))
        # # #self.c.execute("SELECT * from Teacher WHERE username = ? AND password= ?",(uname_,pass_));
        # self.now=self.c.fetchone()
        # self.updated_joind_student=str(self.now)+','+str(Student_roll)
        # # print(self.now)
        # self.c.execute('UPDATE Course SET joined_student=? where course_id=?',(self.updated_joind_student,p))
        # self.conn.commit()
        # self.conn.close()
        #
        # self.Frame3.buttonOut = Button(self.Frame3, text = "Joined")
        # self.Frame3.buttonOut.grid(row=6+btn, column=1, sticky=W+E,padx=20,pady=10)

        pass

    def new_course_create(self):
        self.master.destroy()
        create_new_course_teacher.call(teachers_name)

    def new_session_create(self):
        self.master.destroy()
        create_session.call(teachers_name)


def call(u):
    global teachers_name
    teachers_name=u
    root=Tk()
    root.configure(background="light blue")
    root.geometry("1000x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call("hello")
else:
    print("pepe")