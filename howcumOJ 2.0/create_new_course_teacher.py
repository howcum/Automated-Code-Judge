__author__ = 'howcum'

from tkinter import *
from functools import partial
import teacher_home
import sqlite3
from tkinter import messagebox

teachers_name=NONE

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Create New Course!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+teachers_name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame4=Frame(master,bg="light blue")
        self.Frame4.pack(side="left",expand=TRUE,pady=10,fill="both",padx=20)

        self.stepOne = LabelFrame(self.Frame4, text=" Enter details: ")
        self.stepOne.pack(side="left",expand=TRUE,pady=10,fill="both",padx=20)

        self.courseCodeLbl = Label(self.stepOne, text="Course Code:")
        self.courseCodeLbl.pack(pady=10,expand=FALSE)
        self.CourseCodeText = Entry(self.stepOne)
        self.CourseCodeText.pack(pady=10,expand=FALSE)

        self.YearLbl = Label(self.stepOne, text="Year:")
        self.YearLbl.pack(pady=10)
        self.YearText = Entry(self.stepOne)
        self.YearText.pack(pady=10)

        self.SubmitBtn= Button(self.stepOne,text="Create this Course!!",command=partial(self.createIt,2))
        self.SubmitBtn.pack(pady=20)



    def homeFunction(self):
        self.master.destroy()
        teacher_home.call(teachers_name)
        pass

    def createIt(self,p):
        print("join koro"+str(p))
        self.conn=sqlite3.connect('mydatabase.db')
        c_code=str(self.CourseCodeText.get())
        y_year=str(self.YearText.get())
        c_id=c_code+y_year
        j_st='201314025'
        try:
            self.conn.execute("INSERT INTO Course (course_id, course_code, year,joined_student) \
            VALUES (?,?,?,?)",(c_id,c_code,y_year,j_st))
            msg=messagebox.showinfo('',"Course Successfully Created!!")

        except sqlite3.IntegrityError:
            msg=messagebox.showinfo('',"Course already exists")
            print('ERROR: ID already exists in PRIMARY KEY column {}')

        self.conn.commit()
        self.conn.close()
        pass


def call(u):
    global teachers_name
    teachers_name=u
    print(u)
    root=Tk()
    root.configure(background="light blue")
    root.geometry("1000x500")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call("howcum")
else:
    print("baje")