from tkinter import *

#using Classes Concept Here
class tkinterMenu():
    def __init__(self,newRoot):
        self.frame=Frame(newRoot)
        self.frame.pack

        self.printButton=Button(newRoot,text="This will Print Something on Console",command=self.printSomething)
        self.printButton.pack()

        self.quitButton=Button(newRoot,text="X",command=self.frame.quit)
        self.quitButton.pack()

    def printSomething(self):
        print("Something")
root=Tk()
b=tkinterMenu(root)
root.mainloop()