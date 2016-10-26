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
        #self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.bckButton=Button(self.Frame1,text="Profile")
        self.bckButton.pack(side="right",padx=10)

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

        # self.picFrame=LabelFrame(self.personalInfo,bg="light blue")
        # self.picFrame.pack(side="left",padx=10,expand=FALSE)
        #
        # self.propic=PhotoImage(file="profile.png")
        # self.propiclabel = Label(self.picFrame,image=self.propic)
        # self.propiclabel.pack(padx=10)
        #
        # self.changePropicLbl1=Frame(self.picFrame)
        # self.changePropicLbl1.pack(side="bottom",pady=10)

        self.Frame2=LabelFrame(master,bg="#8b9dc3")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="x")



        # self.changePropic=Button(self.changePropicLbl1,text="Choose file to change pic")
        # self.changePropic.pack(padx=10,side="bottom")
        #
        # self.changePropicLbl=Label(self.changePropicLbl1,text="No file chosen")
        # self.changePropicLbl.pack(fill="x",padx=10,side="bottom")



        # self.session_create= Button(self.Frame2,text="Join New Course",font=15,command=self.course_join)
        # self.session_create.pack(padx=10,pady=90)

        self.session_running= Button(self.Frame2,text="Running Session",font=15,command=self.session_run,bg="#dfe3ee")
        self.session_running.pack(padx=10,pady=10,fill="x")

        self.Frame3=LabelFrame(master,bg="#8b9dc3",text="List of ALL Course")
        self.Frame3.pack(side="left",expand=FALSE,pady=10,fill="y",padx=30)

        # self.txt=Label(self.Frame3,text="No courses joined")
        # self.txt.pack(pady=50,fill="y",padx=20)

        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor();
        self.c.execute('SELECT * from Course')
        self.allrows=self.c.fetchall()
        #print('1): ',self.allrows)
        i=0
        for row in self.allrows:
            #self.q=i
            self.Frame3.buttonIn = Button(self.Frame3, text = "Course "+str(row[1]))
            self.Frame3.buttonIn.grid(row=6+i, column=0, sticky=W+E,padx=20,pady=10)
            self.Frame3.buttonOut = Button(self.Frame3, text = "Join it".format(i),command=partial(self.joinIt,row[0],row[2],i))
            self.Frame3.buttonOut.grid(row=6+i, column=1, sticky=W+E,padx=20,pady=10)
            #self.i=self.i +1
            i=i+1
        self.conn.commit()
        self.conn.close()

    def joinIt(self,p,q,btn):
        pp=str(p)
        print("join koro"+str(p))
        qq=str(q)+str(Student_roll)
        #print(qq,p)
        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor();
        self.c.execute('SELECT joined_student from Course WHERE course_id = ?',(p,))
        # #self.c.execute("SELECT * from Teacher WHERE username = ? AND password= ?",(uname_,pass_));
        self.now=self.c.fetchone()
        self.updated_joind_student=str(self.now)+','+str(Student_roll)
        # print(self.now)
        self.c.execute('UPDATE Course SET joined_student=? where course_id=?',(self.updated_joind_student,p))
        self.conn.commit()
        self.conn.close()

        self.Frame3.buttonOut = Button(self.Frame3, text = "Joined")
        self.Frame3.buttonOut.grid(row=6+btn, column=1, sticky=W+E,padx=20,pady=10)

        pass






        # self.list_of_course= Button(self.Frame1,text="List of Joined Course",font=15)
        # self.list_of_course.grid()

        #self.conn=sqlite3.connect('mydatabase.db')

    def course_join(self):
        self.master.destroy()
        Rank_List.call(student_name)
    def session_run(self):
        self.master.destroy()
        running_session_home.call(student_name,Student_roll)


def call(u):
    print("ashchi" + u)
    global student_name
    student_name=u
    root=Tk()
    root.configure(background="light blue")
    root.geometry("700x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    print("home")

    call("howcum")
else:
    print("pepe")