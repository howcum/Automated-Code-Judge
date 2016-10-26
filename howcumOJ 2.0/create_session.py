__author__ = 'howcum'
from tkinter import *
from functools import partial
import teacher_home
from tkinter import filedialog
import server
import sqlite3
import re

teachers_name = NONE
now_run_korche=NONE

class Application(Frame):
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master.title("Create Session!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)
        #self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)

        self.homeBtn=Button(self.Frame1,text="home",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

        self.bckButton=Button(self.Frame1,text="Profile")
        self.bckButton.pack(side="right",padx=10)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+teachers_name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        # self.stepZero = LabelFrame(master, text="AUTOMATED CODE JUDGE!!")
        # self.stepZero.grid(row=0, columnspan=7, sticky='WE', \
        #                    padx=5, pady=5, ipadx=5, ipady=5)
        #
        # self.homeBtn = Button(self.stepZero, text="home", command=self.homeFunction)
        # self.homeBtn.grid(row=0, columnspan=7, sticky='WE')

        self.stepOne = LabelFrame(master, text=" Enter Details: ")
        self.stepOne.pack(side="left",fill="both",padx=30,ipadx=20,expand=TRUE)

        self.helpLf = LabelFrame(master, text=" SELECT INPUT OUTPUT FILE ")
        self.helpLf.pack(side="left",fill="both",padx=30,ipadx=20,expand=TRUE)
        self.helpLbl = Label(self.helpLf, text="Help will come - ask for it.")
        self.helpLbl.pack()

        self.courseCodeLbl = Label(self.stepOne, text="Course Code:")
        self.courseCodeLbl.pack()
        self.CourseCodeText = Entry(self.stepOne)
        self.CourseCodeText.pack()

        self.YearLbl = Label(self.stepOne, text="Year:")
        self.YearLbl.pack()
        self.YearText = Entry(self.stepOne)
        self.YearText.pack()

        self.SessionNameLbl = Label(self.stepOne, text="Session Name:")
        self.SessionNameLbl.pack()
        self.SessionNameText = Entry(self.stepOne)
        self.SessionNameText.pack()

        self.ProblemCountLbl = Label(self.stepOne, text="Number Of Problem:")
        self.ProblemCountLbl.pack()
        self.ProblemCountText = Entry(self.stepOne)
        self.ProblemCountText.pack()

        self.SubmitBtn = Button(self.stepOne, text="Submit!!", command=self.SubmitNow)
        self.SubmitBtn.pack()









    def SubmitNow(self):
        self.akhon = int(str(self.ProblemCountText.get()))

        c_code = str(self.CourseCodeText.get())
        y_year = str(self.YearText.get())
        c_id = c_code + y_year
        self.CC_ID=c_id

        numm = str(self.SessionNameText.get())
        n_p = int(str(self.ProblemCountText.get()))
        s_id = c_id + numm
        self.SS_ID=s_id
        global now_run_korche
        now_run_korche=self.SS_ID
        self.conn = sqlite3.connect('mydatabase.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT joined_student from Course where course_id= ?',(c_id,))
        self.now = self.c.fetchone()
        # print(self.now)
        string = str(self.now)
        # print([x.strip() for x in string.split("',)('")])
        res=''
        cnt=0

        i=0
        k=0
        while i< len(string):
            print(i)
            if string[i]>='0' and string[i]<='9':
                j=i
                cnt+=1
                while string[j]>='0' and string[j]<='9':
                    res+=string[j]
                    k+=1
                    j+=1
                    i+=1

                res+='00,'
                k+=1
            else:
                i+=1

        print(res)

        try:
            self.conn.execute("INSERT INTO Session (session_id,title,NP) \
            VALUES (?,?,?)", (s_id, numm, n_p));
            # format(tn=table_name, idf=id_column, cn=column_name))

        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(s_id))


        self.conn.execute("INSERT INTO Problems (course_id,session_id,NP,p1,p2,p3,p4,p5) VALUES(?,?,?,?,?,?,?,?)",(c_id,s_id,n_p,res,res,res,res,res))

        # self.c=self.conn.cursor()
        #
        # self.c.execute('SELECT joined_student from Course where course_id= ?',(c_id,))
        # self.now=self.c.fetchone()
        #
        # self.sp=[]
        # self.sp.split("',)(")
        # for st in self.sp:
        #     print(st)

        self.conn.commit()
        self.conn.close()

        for i in range(self.akhon):
            self.q = i
            self.helpLf.buttonPS = Button(self.helpLf, text="Problem Statement for Problem "+str(i+1), command=partial(self.PSFile, i))
            self.helpLf.buttonPS.pack(pady=5)
            self.helpLf.buttonIn = Button(self.helpLf, text="Input File for Problem "+str(i+1), command=partial(self.inButton, i))
            self.helpLf.buttonIn.pack(pady=5)
            self.helpLf.buttonOut = Button(self.helpLf, text="Output File for Problem "+str(i+1),
                                           command=partial(self.outButton, i))
            self.helpLf.buttonOut.pack(pady=5)

        self.RunBtn = Button(self.helpLf, text="Run Session Now", command=self.runNow)
        self.RunBtn.pack(pady=5)
        pass

    def PSFile(self, p):
        print(p)
        print("input file selected!!")
        filename = filedialog.askopenfilename(initialdir="E:/Images", title="choose your file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(filename)
        a_file = open(filename, "r")
        ext = str(p)
        b_file = open("problem" + ext + ".txt", "w")
        str1 = a_file.read()
        print(str1)
        b_file.write(str1)
        a_file.close()
        pass

    def inButton(self, p):
        print(p)
        print("input file selected!!")
        filename = filedialog.askopenfilename(initialdir="E:/Images", title="choose your file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(filename)
        a_file = open(filename, "r")
        ext = str(p)
        b_file = open("input" + ext + ".txt", "w")
        str1 = a_file.read()
        print(str1)
        b_file.write(str1)
        a_file.close()
        pass

    def outButton(self, p):
        print(p)
        print("output file selected!!")
        filename = filedialog.askopenfilename(initialdir="E:/Images", title="choose your file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(filename)
        a_file = open(filename, "r")
        b_file = open("output" + str(p) + ".txt", "w")
        str1 = a_file.read()
        print(str1)
        b_file.write(str1)
        a_file.close()
        pass

    def homeFunction(self):
        print("back a ja ga")
        self.master.destroy()
        teacher_home.call(teachers_name)
        pass

    def runNow(self):
        print("Run kor na vai")

        now_run_korche=self.SS_ID

        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor()
        print(now_run_korche)
        try:
            self.c.execute("UPDATE NowRunning SET session_id =? where p=1",(str(now_run_korche),))
        except:
            print("update hocche na")
        #self.master.destroy()
        self.conn.commit()
        self.conn.close()
        server.Main_server(self.CC_ID,self.SS_ID)

        pass

        # #self.conn=sqlite3.connect('mydatabase.db')


def call(u):
    print("ashchi" + u)
    global teachers_name
    teachers_name = u
    root = Tk()
    root.configure(background="light blue")
    root.geometry("1000x500")
    app = Application(root)
    app.mainloop()


if __name__ == '__main__':
    print("home")
    call("hello")
else:
    print("pepe")
