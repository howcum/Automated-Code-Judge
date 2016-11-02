__author__ = 'howcum'
from tkinter import *
import Rank_List
import running_session_home
import sqlite3
from functools import partial

student_name=NONE
Student_roll=201314025
FLAG=0

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Student Home!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+student_name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame4=Frame(master,bg="light blue")
        self.Frame4.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.personalInfo=LabelFrame(self.Frame4,text="Personal Information:",bg="#8b9dc3")
        self.personalInfo.pack(fill="y",side="right",expand=TRUE)

        self.NameLbl=Label(self.personalInfo,text="Name : "+student_name,)
        self.NameLbl.pack(fill="x",pady=10)
        self.RollLbl=Label(self.personalInfo,text="Roll : "+str(Student_roll))
        self.RollLbl.pack(fill="x")

        self.Frame2=LabelFrame(master,bg="#8b9dc3")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="x")

        self.session_running= Button(self.Frame2,text="Running Session",font=15,command=self.session_run,bg="#dfe3ee")
        self.session_running.pack(padx=10,pady=10,fill="x")

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
            self.Frame3.buttonOut = Button(self.Frame3, text = "Join it".format(i),command=partial(self.joinIt,row[0],row[2],i))
            self.Frame3.buttonOut.grid(row=6+i, column=1, sticky=W+E,padx=20,pady=10)
            i+=1
        self.conn.commit()
        self.conn.close()

    def joinIt(self,p,q,btn):
        pp=str(p)
        qq=str(q)+str(Student_roll)
        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor();
        self.c.execute('SELECT joined_student from Course WHERE course_id = ?',(p,))
        self.now=self.c.fetchone()
        self.updated_joind_student=str(self.now)+','+str(Student_roll)
        self.c.execute('UPDATE Course SET joined_student=? where course_id=?',(self.updated_joind_student,p))
        self.conn.commit()
        self.conn.close()

        self.Frame3.buttonOut = Button(self.Frame3, text = "Joined")
        self.Frame3.buttonOut.grid(row=6+btn, column=1, sticky=W+E,padx=20,pady=10)

        pass

    def course_join(self):
        self.master.destroy()
        Rank_List.call(student_name)
        pass
    def session_run(self):
        self.master.destroy()
        running_session_home.call(student_name,Student_roll)
        pass


def call(u,v):
    global student_name
    global Student_roll
    Student_roll=u
    student_name=v
    root=Tk()
    root.configure(background="light blue")
    root.geometry("700x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call("201314025","howcum")
else:
    print("pepe")