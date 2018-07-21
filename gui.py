#Designing a simple GUI Tinkter App
#Importing the library first
from tkinter import *
root=Tk()
# whatToPrint=input("Ente The Text You Want To Print")
# label=Label(root,text=whatToPrint)
# label.pack()
##Adding Frames Here
upperFrame=Frame(root)
upperFrame.pack(side=TOP)
lowerFrame=Frame(root)
lowerFrame.pack(side=BOTTOM)
##Adding the Buttons Here
redButton=Button(upperFrame,text="Click Here",fg="Red")
blueButton=Button(lowerFrame,text="Click Here",fg="Blue")
#Packing the buttons
redButton.pack()
blueButton.pack()
root.mainloop()