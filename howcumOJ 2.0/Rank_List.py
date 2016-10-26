__author__ = 'howcum'

from tkinter import *
from functools import partial
import student_home
import tkinter as tk
import sqlite3
import running_session_home

Student_roll=NONE
Student_Name=NONE

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Rank List")

        # self.stepZero=LabelFrame(master,text="AUTOMATED CODE JUDGE!!")
        # self.stepZero.grid(row=0, columnspan=7, sticky='WE', \
        #              padx=5, pady=5, ipadx=5, ipady=5)

        # self.homeBtn=Button(self.stepZero,text="home",command=self.homeFunction)
        # self.homeBtn.grid(row=0,columnspan=7,sticky='WE')

        # self.stepOne = LabelFrame(master, text=" List of Courses: ")
        # self.stepOne.grid(row=1, columnspan=7, sticky='W', \
        #              padx=5, pady=5, ipadx=5, ipady=5)

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)
        #self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.homeBtn=Button(self.Frame1,text="home",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

        self.bckButton=Button(self.Frame1,text="Profile")
        self.bckButton.pack(side="right",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+Student_Name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame4=Frame(master,bg="light blue")
        self.Frame4.pack(side="top",expand=TRUE,pady=10,fill="y")

        self.conn = sqlite3.connect('mydatabase.db')
        self.c = self.conn.cursor()

        self.c.execute("SELECT session_id from NowRunning where p=1")
        self.now_session=self.c.fetchone()
        print(self.now_session[0])

        self.c.execute("SELECT * from Session where session_id=?",(str(self.now_session[0]),))
        self.akhon=self.c.fetchone()
        print(self.akhon)
        self.c.execute("SELECT * from Session_Progress where session_id=?",(str(self.now_session[0]),))
        self.row_ache=self.c.fetchall()
        row_sss=0
        user=[]
        for row in self.row_ache:
            row_sss+=1
            user+=str(row[1])
        print(row_sss,str(user))
        t = SimpleTable(self.Frame4, row_sss+1,int(self.akhon[2])+2)
        t.pack(side="top", fill="x")
        t.set(0,0,"Rank")
        t.set(0,1,"Roll")
        it=1;
        for row in self.row_ache:
            it2=1
            for col in range(int(self.akhon[2])+1):
                pp=str(row[it2])
                t.set(it,it2,pp)
                it2+=1
            it+=1
        it=1

        # for row in self.row_ache:
        #     pp=str(row[2])
        #     t.set(it,2,pp)
        #     it+=1
        #
        # it=1
        # for row in self.row_ache:
        #     pp=str(row[3])
        #     t.set(it,3,pp)
        #     it+=1
        #
        #
        # it=1
        # for row in self.row_ache:
        #     pp=str(row[4])
        #     t.set(it,4,pp)
        #     it+=1
        #
        #
        # it=1
        # for row in self.row_ache:
        #     pp=str(row[5])
        #     t.set(it,5,pp)
        #     it+=1
        #
        # it=1
        # for row in self.row_ache:
        #     pp=str(row[6])
        #     t.set(it,6,pp)
        #     it+=1

        for i in range(int(self.akhon[2])):
            t.set(0,i+2,"problem "+ str(i+1))

        self.conn.commit()
        self.conn.close()

        self.Frame2=LabelFrame(master,bg="light blue")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="y")




    def homeFunction(self):
        print("back a ja ga")
        self.master.destroy()
        running_session_home.call(Student_Name,Student_roll)
        pass



def call(u,v):
    print(u)
    global Student_roll
    global Student_Name
    Student_roll = v
    Student_Name=u
    root=Tk()
    root.configure(background="light blue")
    root.geometry("700x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call("howcum","201314021")
else:
    print("baje")