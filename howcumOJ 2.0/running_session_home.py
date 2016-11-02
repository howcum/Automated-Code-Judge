__author__ = 'howcum'
from tkinter import *
import student_home
from functools import partial
from tkinter import filedialog
import socket
import tkinter.scrolledtext as tkst
import Rank_List
import my_submission
import sqlite3
from tkinter import messagebox

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

Student_name=NONE
Roll_number=[]
NOW_OPEN=0

class Application(Frame):
    def __init__(self,master=NONE):
        Frame.__init__(self,master)
        self.master.title("Running Session!!")

        self.Frame1=LabelFrame(master,bg="#3b5998")
        self.Frame1.pack(side="top", fill="x", expand=FALSE)

        self.homeBtn=Button(self.Frame1,text="Back",command=self.homeFunction)
        self.homeBtn.pack(side="left",padx=20)

        self.heading= Label(self.Frame1,text="AUTOMATED CODE JUDGE!!",font=100)
        self.heading.pack(side="top",pady=10)

        self.welcome= Label(self.Frame1,text="Welcome "+Student_name+" !",font=30)
        self.welcome.pack(side="bottom",pady=10)

        self.Frame4=Frame(master,bg="light blue")
        self.Frame4.pack(side="left",expand=FALSE,pady=10,fill="both",padx=20)

        self.leftFrame=LabelFrame(self.Frame4,bg="light blue",text="Session Information:")
        self.leftFrame.pack(fill="y",side="top",expand=FALSE)

        self.overviewBtn=Button(self.leftFrame,text="Overview")
        self.overviewBtn.pack(side="left",fill="x",pady=10,padx=20)
        self.mySubmission=Button(self.leftFrame,text="My Submission",command=self.submission_page)
        self.mySubmission.pack(side="left",fill="x",padx=20)
        self.rankList=Button(self.leftFrame,text="Rank List",command=self.rank_page)
        self.rankList.pack(side="left",fill="x",pady=10,padx=20)

        self.midInleftFrame=LabelFrame(self.Frame4,text="Overview")
        self.midInleftFrame.pack(expand=FALSE,fill="x")

        self.showP=Label(self.midInleftFrame,text="Problems")
        self.showP.pack()

        self.conn=sqlite3.connect('mydatabase.db')
        self.c=self.conn.cursor()
        s_id=[]
        try:
            self.c.execute("SELECT * from NowRunning where p=1")
            self.nppp=self.c.fetchone()
            s_id=str(self.nppp[0])
            print(s_id)
        except:
            print("ekhane")
        #self.master.destroy()

        self.c.execute('SELECT NP from Session where session_id=?',(s_id,))
        self.temp=self.c.fetchone()
        self.cnt=int(self.temp[0])
        print("cnt",self.cnt)
        self.conn.commit()
        self.conn.close()

        for i in range(self.cnt):
            self.midInleftFrame.problemBtn=Button(self.midInleftFrame,text="Problem "+ str(i+1),command=partial(self.ProblemShow, i))
            self.midInleftFrame.problemBtn.pack(side="left",padx=20,pady=20)

        self.Frame5=LabelFrame(master,bg="light blue",text="Code Editor: ")
        self.Frame5.pack(side="right",expand=FALSE,pady=10,fill="y",padx=20)

        self.ProblemArea = tkst.ScrolledText(self.Frame4,undo=True)
        self.ProblemArea.pack()

        filename="Problem0.txt"
        a_file = open(filename, "r")
        str1 = a_file.read()
        a_file.close()

        self.ProblemArea.insert(INSERT,str1)

        self.CodeArea = tkst.ScrolledText(self.Frame5)
        self.CodeArea.pack(fill="y")

        self.choosefilelabel=Label(self.Frame5,text="or Choose file here")
        self.choosefilelabel.pack(pady=10)

        self.choosefileBtn=Button(self.Frame5,text="Browse",command=partial(self.solutionFile,NOW_OPEN))
        self.choosefileBtn.pack(pady=5)

        self.SubmitBtn= Button(self.Frame5,text="Submit",command=partial(self.submitIt,NOW_OPEN))
        self.SubmitBtn.pack(pady=20)


    def submission_page(self):
        self.master.destroy()
        my_submission.call(Student_name,Roll_number)
        pass

    def rank_page(self):
        self.master.destroy()
        Rank_List.call(Student_name,Roll_number)
        pass

    def ProblemShow(self,p):
        filename="problem"+str(p)+".txt"
        a_file = open(filename, "r")
        NOW_OPEN=p
        str1 = a_file.read()
        a_file.close()
        self.ProblemArea.edit_undo()
        self.ProblemArea.insert(INSERT,str1)
        pass

    def donothing(self):
        print("do nothing!!")
        pass



    def homeFunction(self):
        self.master.destroy()
        student_home.call(Roll_number,Student_name)
        pass

    def solutionFile(self,p):
        print(p)
        print("file selected!!")
        filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("cpp","*.cpp"),("all files","*.*")))
        a_file = open(filename,"r")
        ext=str(p)
        b_file=open("solution"+ext+".cpp","w")
        str1=a_file.read()
        print(str1)
        b_file.write(str1)
        a_file.close()

        self.CodeArea.edit_undo()
        self.CodeArea.insert(INSERT,str1)
        pass

    def submitIt(self,p):
        filename="solution"+str(p)+".cpp"

        str2=str(self.CodeArea.get(0.0,END))
        b_file=open(filename,"w")
        b_file.write(str2)
        b_file.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        l='//'+str(Roll_number)+ ' ' +str(p)+'\r\n'
        s.send(l.encode('ascii'))
        with open(filename, 'rb') as f:
             print ('file opened')
             while True:
                    l = f.read(BUFFER_SIZE)
                    while (l):
                        s.send(l)
                        print('Sent ',repr(l))
                        l = f.read(BUFFER_SIZE)
                    if not l:
                        f.close()
                        s.close()
                        break
        print('Successfully send the file')
        s.close()
        print('connection closed')
        messagebox.showinfo("title","Successfully Submitted!!! See My Submission to see the verdict")
        pass


def call(u,v):
    global Roll_number
    global Student_name
    Student_name=u
    Roll_number=v
    root=Tk()
    root.configure(background="light blue")
    root.geometry("2000x1000")
    app=Application(root)
    app.mainloop()

if __name__ == '__main__':
    call("test","201314010")
else:
     print("hello")