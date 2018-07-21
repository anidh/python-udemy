#Designing a simple GUI Tinkter App
#Importing the library first
from tkinter import *
def printFull():
    print("The Full Name Is:")
root=Tk()
#Using The Grid Layout Here!
labelFirst=Label(root, text="Enter First Name")
labelLast=Label(root, text="Enter Last Name")
entryFirst=Entry(root)
entryLast=Entry(root)
labelFirst.grid(row=0, column=0)
labelLast.grid(row=1, column=0)
entryFirst.grid(row=0, column=1)
entryLast.grid(row=1, column=1)
#Adding Buttons
buttonOk=Button(root,text="OK",command=printFull)
buttonOk.grid(row=2,column=0)
root.mainloop()