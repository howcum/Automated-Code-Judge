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
                label = tk.Label(self, text="NONE",
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
        self.master.title("My Submission!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

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

        self.c.execute("SELECT * from Session where session_id=?",(str(self.now_session[0]),))
        self.akhon=self.c.fetchone()
        t = SimpleTable(self.Frame4, 2,int(self.akhon[2])+2)
        t.pack(side="top", fill="x")
        self.c.execute("SELECT * from Session_Progress where session_id=? and roll_number=?",(str(self.now_session[0]),Student_roll))
        self.row_ache=self.c.fetchone()
        t.set(0,0,"My submission")
        t.set(0,1,"Roll")
        t.set(1,0,"1")
        t.set(1,1,str(self.row_ache[1]))
        it=2
        for i in range(int(self.akhon[2])):
            t.set(1,it,self.row_ache[it])
            it+=1

        for i in range(int(self.akhon[2])):
            t.set(0,i+2,"problem "+ str(i+1))
        self.Frame2=LabelFrame(master,bg="light blue")
        self.Frame2.pack(side="left",expand=TRUE,pady=10,fill="y")

        self.conn.commit()
        self.conn.close()



    def homeFunction(self):
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
    call("howcum","201314025")
else:
    print("baje")