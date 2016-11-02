
from tkinter import *
from tkinter import filedialog
from functools import partial
import tkinter as tk

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if column%3==0:
                    label = tk.Button(self, text="File",
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
    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master.title("test!!")
        self.helpLf = LabelFrame(master, text=" SELECT INPUT OUTPUT FILE ")
        self.helpLf.pack(side="left",fill="both",ipadx=20,expand=TRUE)
        self.helpLf1 = LabelFrame(master, text=" SELECTED FILES ")
        self.helpLf1.pack(side="left",fill="both",ipadx=20,expand=TRUE)
        self.helpLbl = Label(self.helpLf, text="Fill Out the primary details")
        self.helpLbl.pack()
        # self.buttonPS
        # self.buttonIn
        # self.buttonOut

        for i in range(3):
            self.q = i
            self.helpLf.buttonPS = Button(self.helpLf, text="Problem Statement for Problem "+str(i+1), command=partial(self.PSFile, i))
            self.helpLf.buttonPS.pack(pady=5)
            self.helpLf.buttonIn = Button(self.helpLf, text="Input File for Problem "+str(i+1), command=partial(self.inButton, i))
            self.helpLf.buttonIn.pack(pady=5)
            self.helpLf.buttonOut = Button(self.helpLf, text="Output File for Problem "+str(i+1),
                                           command=partial(self.outButton, i))
            self.helpLf.buttonOut.pack(pady=5)

        # t = SimpleTable(self.helpLf, 3*3,2)
        # t.pack(side="top", fill="x")

        # for i in range(3*3):
        #     now=int(i/3 +1)
        #     if i%3==0:
        #         t.set(i,0,"problem "+str(now))
        #     elif i%3==1:
        #         t.set(i,0,"input file of problem "+ str(now))
        #     else:
        #         t.set(i,0,"output file of problem "+ str(now))

        # t = SimpleTable(self.helpLf, 3*3,2)
        # t.pack(side="top", fill="x")
        #
        # for i in range(3*3):
        #     now=int(i/3 +1)
        #     if i%3==0:
        #         t.set(i,0,"problem "+str(now))
        #     elif i%3==1:
        #         t.set(i,0,"input file of problem "+ str(now))
        #     else:
        #         t.set(i,0,"output file of problem "+ str(now))

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
        self.helpLf1.selectedPS = Button(self.helpLf1, text=str(filename))
        self.helpLf1.selectedPS.pack(pady=5)
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
        self.helpLf1.selectedIN = Button(self.helpLf1, text=str(filename))
        self.helpLf1.selectedIN.pack(pady=5)
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
        self.helpLf1.selectedOUT = Button(self.helpLf1, text=str(filename))
        self.helpLf1.selectedOUT.pack(pady=5)
        pass


root = Tk()
root.configure(background="light blue")
root.geometry("1000x500")
app = Application(root)
app.mainloop()