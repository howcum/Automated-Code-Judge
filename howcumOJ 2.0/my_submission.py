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
        self.master.title("My Submission!!")

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

        t = SimpleTable(self.Frame4, 10,4)
        t.pack(side="top", fill="x")
        t.set(0,0,"Hello, world")

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