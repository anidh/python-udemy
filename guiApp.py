#Designing a simple GUI Tinkter App
#Importing the library first
from tkinter import *

#Creating a root window first'
rootWindow=Tk()
string=str(input("Enter Your Name\n"))
label=Label(rootWindow,text=string)
label.pack()
rootWindow.mainloop()