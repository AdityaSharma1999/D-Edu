import face_recognition
import tkinter as tk
from readcall import *
import os
import English
import MathTest
#0xbdc0741e5a6c2e3a329bf7cf7571d4e67d7e71bf
studentHash=""
name=""
entries=[]
def checkHash(self,selection):
    studentHash=(self.hashEntry.get(1.0,'end-1c'))
    name=readBC("getStudentName(address)",[int(self.hashEntry.get(1.0,'end-1c'),16)],"string")
    print(studentHash)
    print(name)
    if((name!="")&(selection==1)):English.main(studentHash,name)
    elif((name!="")&(selection==2)):MathTest.main(studentHash,name)
    return 1

class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        global entries
        self.hashLabel=tk.Label(self,font=("Times New Roman",45),text="Enter hash: ")
        self.hashEntry=tk.Text(self,font=("Times New Roman",45),height="1",width="25")
        entries.append(self.hashEntry)
        self.submitEnglish=tk.Button(self,borderwidth="3",text="English",font=("Times New Roman",30),command=self.postEnglish)
        self.submitMath=tk.Button(self,borderwidth="3",text="Math",font=("Times New Roman",30),command=self.postMath)
        self.quit=tk.Button(self,text="QUIT",fg="red",borderwidth="3",font=("Times New Roman",30),command=self.end)
        self.submitEnglish.bind('<Return>',self.postEnglish)
        self.submitMath.bind('<Return>',self.postMath)
        self.quit.bind('<Return>',self.end)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hashLabel.pack()
        self.hashEntry.pack()
        self.submitEnglish.pack(side="left")
        self.submitMath.pack(side="right")
        self.quit.pack()

    def postEnglish(self,*args):
        global name
        print("checking hash")
        checkHash(self,1)

    def postMath(self,*args):
        global name
        print("checking hash")
        checkHash(self,2)


    def end(self,*args):
        #quits
        print("quitting")
        root.destroy()
        exit(0)

root=tk.Tk()
root.resizable(width=False,height=False)
app=Application(master=root)
app.master.title("Login")
app.mainloop()
