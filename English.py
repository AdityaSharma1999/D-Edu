import tkinter as tk
import API2
import json
from readcall import *
from writecall import *
import sys

#initialize global variables
questionTitles=[]
sentenceTitles=[]
questions=[]
answers=[["" for x in range(10)] for y in range(10)]
entries=[]
labels=[]
noStrings=10
questionCounter=0
maxPoints=0
grade=0
foo=0
studentHash=0
noStrings=5

def getSentenceTitle(count):
    #Get sentences from blockchain
    #print(readBC("getStudentName(address)", [0x5e8d910869c97eb5d23e03a7c4f95548c676f776], 'string'))
    return readBC("getEnglishQuestion(uint256)",[count],"string")
    #return "Joe went to the store"


def getQuestion(count):
    #Get String from Language API
    return sentenceTitles[count].split()


def getAnswer(count):
    #get answer from Language API
    dat=json.loads(API2.run(sentenceTitles[count]))
    try:
        data=dat[0]['result'][0]
    except Exception as e:
        data=[]
        for x in range(len(questions[count])):
            data.append("noun")
        print(e)
    return data


def fixAnswers():
    #Changes answer format from Microsoft to english
    for x in range(len(answers)):
        for y in range(len(answers[x])):
            if answers[x][y]=="NNP":answers[x][y]="pronoun"
            elif (answers[x][y]=="VBD")|(answers[x][y]=="VBP")|(answers[x][y]=="VB")|(answers[x][y]=="VBZ"):answers[x][y]="verb"
            elif (answers[x][y]=="TO")|(answers[x][y]=="IN"):answers[x][y]="preposition"
            elif (answers[x][y]=="DT")|(answers[x][y]=="PRP")|(answers[x][y]=="PRP$"):answers[x][y]="determiner"
            elif (answers[x][y]=="NN")|(answers[x][y]=="NNS"):answers[x][y]="noun"
            elif answers[x][y]=="CC":answers[x][y]="conjunction"
            elif answers[x][y]=="RB":answers[x][y]="adverb"
            elif answers[x][y]=="JJ":answers[x][y]="adjective"
            elif answers[x][y]=="CD":answers[x][y]="numeral"
            elif answers[x][y]=="EX":answers[x][y]="existential"
            elif answers[x][y]=="FW":answers[x][y]="foreign"


def focus_next_window(event):
    #focus next event
    event.widget.tk_focusNext().focus()
    return "break"


def checkAnswers():
    #sets maxPoints and returns points
    points=0
    if(len(questions[questionCounter]))==0:return 0
    global maxPoints
    maxPoints+=len(questions[questionCounter])
    for x in range(len(answers[questionCounter])):
        #print(str(x)+" in range: "+str(len(answers[questionCounter])))
        for y in range(len(entries)):
            #print(str(y)+" in range: "+str(len(entries)))
            ans=answers[questionCounter][x]
            ent=entries[y]
            if (x==y)&(ans==((ent.get(1.0,'end-1c')).lower())):points+=1
    return points

def main(stuHash, name):
    global foo
    global studentHash
    print(studentHash)
    global noStrings
    studentHash=stuHash
    print(name)
    noStrings=int(readBC("getEnglishProblemTotal()",[],"uint256"))
    print(noStrings)
    if(foo==0):
        for i in range(int(noStrings)):
            #from 0-4 update the arrays
            questionTitles.append("Correctly identify part of speech ("+str(i+1)+"):")
            sentenceTitles.append(getSentenceTitle(i+1))
            questions.append(getQuestion(i))
            answers[i]=getAnswer(i)
            foo=1
    fixAnswers()
    print(sentenceTitles)
    print(questions)
    print(answers)
    global root
    global app
    root=tk.Tk()
    root.resizable(width=False,height=False)
    app=Application(master=root)
    app.master.title(name+"-ENGLISH")
    app.mainloop()


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        global entries
        global labels

        #initialize question & sentence and add to grid
        self.question=tk.Label(self,font=("Times New Roman",45))
        self.question.grid(row=0,columnspan=5,sticky='N')
        self.sentence=tk.Label(self,font=("Times New Roman",45))
        self.sentence.grid(row=1,columnspan=5,sticky='N')

        #initialize labels and entries and assign them to grid spaces
        self.label0=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry0=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label0.grid(row=2,column=0)
        self.entry0.grid(row=3,column=0)

        self.label1=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry1=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label1.grid(row=2,column=1)
        self.entry1.grid(row=3,column=1)

        self.label2=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry2=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label2.grid(row=2,column=2)
        self.entry2.grid(row=3,column=2)

        self.label3=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry3=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label3.grid(row=2,column=3)
        self.entry3.grid(row=3,column=3)

        self.label4=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry4=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label4.grid(row=2,column=4)
        self.entry4.grid(row=3,column=4)

        self.label5=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry5=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label5.grid(row=4,column=0)
        self.entry5.grid(row=5,column=0)

        self.label6=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry6=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label6.grid(row=4,column=1)
        self.entry6.grid(row=5,column=1)

        self.label7=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry7=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label7.grid(row=4,column=2)
        self.entry7.grid(row=5,column=2)

        self.label8=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry8=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label8.grid(row=4,column=3)
        self.entry8.grid(row=5,column=3)

        self.label9=tk.Label(self,height=1,width=15,font=("Times New Roman",25))
        self.entry9=tk.Text(self,height=1,width=15,font=("Times New Roman",25))
        self.label9.grid(row=4,column=4)
        self.entry9.grid(row=5,column=4)

        entries=[self.entry0,self.entry1,self.entry2,self.entry3,self.entry4,self.entry5,self.entry6,self.entry7,
            self.entry8,self.entry9]
        labels=[self.label0,self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,
            self.label8,self.label9]

        #assign function buttons
        self.submit=tk.Button(self,borderwidth="3",text="Submit",font=("Times New Roman",30),command=self.post)
        self.quit=tk.Button(self,text="QUIT",fg="red",borderwidth="3",font=("Times New Roman",30),command=self.end)
        self.submit.bind('<Return>',self.post)
        self.quit.bind('<Return>',self.end)
        self.submit.grid(row=6,column=0,columnspan=2,sticky='S')
        self.quit.grid(row=6,column=3,columnspan=2,sticky='S')

        #pack & create
        self.pack()
        self.create_widgets()
        #set cursor to first entry box

    def create_widgets(self):
        self.question["text"]=questionTitles[questionCounter]
        self.sentence["text"]=sentenceTitles[questionCounter]

        for x in range(len(entries)):
            #removes any text in entry box
            (entries[x]).delete(1.0,"end")
            #Tab goes to next entry box
            (entries[x]).bind("<Tab>",focus_next_window)
            #If there is another word, update entry with
            if len(questions[questionCounter])>=x+1:
                (labels[x])["text"]=questions[questionCounter][x]
            else:
                (labels[x])["text"]=""
        self.entry0.focus()

    def post(self,*args):
        global app
        global root
        global questionCounter
        global grade

        #Check answers
        grade+=checkAnswers()
        print("GRADE: "+str(grade))
        print("OUT OF: "+str(maxPoints))

        questionCounter+=1
        print("questionCounter: "+str(questionCounter)+" noStrings: "+str(noStrings))
        if questionCounter==noStrings:
            self.end()
        else:
            self.create_widgets()
            app.master.update()


    def end(*args):
        global studentHash
        global maxPoints
        #posts grades to blockchain
        print("post to chain")
        writeBC('addEnglishScore',studentHash,grade,maxPoints)
        #quits
        print("quitting")
        root.destroy()
        exit(0)
