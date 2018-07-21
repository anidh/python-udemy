#Designing a simple GUI Tinkter App
#Importing the library first
from tkinter import *
root=Tk()
whatToPrint=input("Ente The Text You Want To Print")
label=Label(root,text=whatToPrint)
label.pack()
label.mainloop()