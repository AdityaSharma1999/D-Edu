import tkinter as tk
from tkinter import IntVar
from readcall import *
from writecall import *

noProblems=0
instructions=["" for x in range(10)]
problems=[]
options=[["","",""] for x in range(10)]
answers=[0 for x in range(10)]
grade=0
problemCounter=0
radioVarValue=0

def getInstructions():
    for x in range(len(instructions)):
        instructions[x]=("Evaluate the expression ("+str(x+1)+")")
    print(instructions)


def getProblems():
    for x in range(noProblems):
        print(x)
        problems.append(readBC("getMathQuestion(uint256)",[x],"string"))
    print(problems)


def getOptions():
    for x in range(noProblems):
        options[x][0]=readBC("getMathChoice1(uint256)",[x],"string")
        options[x][1]=readBC("getMathChoice2(uint256)",[x],"string")
        options[x][2]=readBC("getMathChoice3(uint256)",[x],"string")
    print(options)


def getAnswers():
    for x in range(len(answers)):
        answers[x]=int(readBC("getMathCorrect(uint256)",[x],"uint256"))
    print(answers)


def main(stuHash, na):
    global studentHash
    global name
    global noProblems

    studentHash=stuHash
    name=na
    noProblems=int(readBC("getMathProblemTotal()",[],"uint256"))
    print(noProblems)
    # instructions=["" for x in range(noProblems)]
    getInstructions()
    getProblems()
    getOptions()
    getAnswers()
    print(instructions)
    print(problems)
    print(options)
    print(answers)
    global root
    global app
    root=tk.Tk()
    root.resizable(width=False,height=False)
    #root.geometry('{}x{}'.format(1080,480))
    app=Application(master=root)
    app.master.title("Math")
    app.mainloop()


def checkAnswers():
    if answers[problemCounter]==radioVarValue:return 1
    return 0


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.instruction=tk.Label(self,height=1,font=("Times New Roman",45))
        self.instruction.grid(row=0,columnspan=7,sticky='N')

        self.problem=tk.Label(self,height=1,font=("Times New Roman",45))
        self.problem.grid(row=1,columnspan=7,sticky='N')

        self.radio0=tk.Radiobutton(self,font=("Times New Roman",45),borderwidth="3")
        self.radio1=tk.Radiobutton(self,font=("Times New Roman",45),borderwidth="3")
        self.radio2=tk.Radiobutton(self,font=("Times New Roman",45),borderwidth="3")
        self.radio0.grid(row=2,column=0,columnspan=7,sticky='N')
        self.radio1.grid(row=3,column=0,columnspan=7,sticky='N')
        self.radio2.grid(row=4,column=0,columnspan=7,sticky='N')

        #assign function buttons
        self.submit=tk.Button(self,text="Submit",font=("Times New Roman",30),borderwidth="3",command=self.post)
        self.submit.grid(row=7,column=0,columnspan=2,sticky='S')

        self.quit=tk.Button(self,text="QUIT",fg="red",font=("Times New Roman",30),borderwidth="3",command=self.end)
        self.quit.grid(row=7,column=5,columnspan=2,sticky='S')

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global instructions
        self.instruction["text"]=instructions[problemCounter]

        self.problem["text"]=problems[problemCounter]

        self.radioVar=IntVar(root)
        self.radioVar.set(0)
        self.radio0["text"]=options[problemCounter][0]
        self.radio1["text"]=options[problemCounter][1]
        self.radio2["text"]=options[problemCounter][2]
        self.radio0["value"]=0
        self.radio1["value"]=1
        self.radio2["value"]=2
        self.radio0["variable"]=self.radioVar
        self.radio1["variable"]=self.radioVar
        self.radio2["variable"]=self.radioVar
        self.radio0["command"]=self.updateradioVar
        self.radio1["command"]=self.updateradioVar
        self.radio2["command"]=self.updateradioVar

        self.submit.bind('<Return>',self.post)
        self.quit.bind('<Return>',self.end)

    def updateradioVar(self):
        global radioVarValue
        print("updating: "+str((self.radioVar).get()))
        radioVarValue=(self.radioVar).get()

    def post(self,*args):
        global radioVarValue
        global noProblems
        global grade

        print("post")
        print(radioVarValue)
        global problemCounter
        #Check answers
        grade+=checkAnswers()
        print("GRADE: "+str(grade))
        print("OUT OF: "+str(noProblems))

        problemCounter+=1
        if problemCounter==noProblems:
            self.end()
        else:
            self.radioVar.set(0)
            self.create_widgets()
            app.master.update()


    def end(self,*args):
        print("post to chain")
        writeBC('addMathScore',studentHash,grade,noProblems)
        print("quitting")
        root.destroy()
        exit(0)
